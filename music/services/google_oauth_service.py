import os
import json
import requests
from django.conf import settings
from music.models import User
from google.auth.transport.requests import Request
from google.oauth2.id_token import verify_oauth2_token

class GoogleOAuthService:
    GOOGLE_OAUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
    GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"

    @staticmethod
    def get_authorization_url():
        """Generate Google OAuth authorization URL"""
        params = {
            "client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            "redirect_uri": settings.GOOGLE_OAUTH_REDIRECT_URI,
            "response_type": "code",
            "scope": "openid profile email",
            "access_type": "offline"
        }
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        return f"{GoogleOAuthService.GOOGLE_OAUTH_URL}?{query_string}"

    @staticmethod
    def get_access_token(code):
        """Exchange authorization code for access token"""
        data = {
            "client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            "client_secret": settings.GOOGLE_OAUTH_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": settings.GOOGLE_OAUTH_REDIRECT_URI
        }
        response = requests.post(GoogleOAuthService.GOOGLE_TOKEN_URL, data=data)
        return response.json()

    @staticmethod
    def get_user_info(access_token):
        """Get user information from Google"""
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(GoogleOAuthService.GOOGLE_USERINFO_URL, headers=headers)
        return response.json()

    @staticmethod
    def authenticate_user(code):
        """Main authentication flow: code -> user"""
        try:
            # Step 1: Exchange code for token
            token_data = GoogleOAuthService.get_access_token(code)
            if "error" in token_data:
                return None, token_data.get("error_description")
            
            access_token = token_data.get("access_token")
            
            # Step 2: Get user info
            user_info = GoogleOAuthService.get_user_info(access_token)
            
            # Step 3: Create or get user
            user, created = User.objects.get_or_create(
                email=user_info.get("email"),
                defaults={
                    "username": user_info.get("email").split("@")[0],
                    "first_name": user_info.get("given_name", ""),
                    "last_name": user_info.get("family_name", ""),
                }
            )
            return user, None
        except Exception as e:
            return None, str(e)