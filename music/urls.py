from django.urls import path
from music.controllers import auth_controller, library_controller, song_controller

app_name = 'music'

urlpatterns = [
    path('', auth_controller.landing_page, name='landing'),
    path('login/', auth_controller.login_page, name='login'),
    path('library/', library_controller.library_page, name='library'),
    path('song/generate/', song_controller.generate_song, name='generate_song'),
    path('song/review/', song_controller.song_review, name='song_review'),
    path('song/create/', song_controller.create_song, name='song_create'),
    path('song/<int:song_id>/', song_controller.song_detail, name='song_detail'),
]