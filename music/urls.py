from django.urls import path
from music.controllers import auth_controller, library_controller, song_controller

urlpatterns = [
    path('', auth_controller.landing_page),
    path('login/', auth_controller.login_page),

    path('library/', library_controller.library_page),

    path('song/generate/', song_controller.generate_song_page),
    path('song/create/', song_controller.create_song),
]