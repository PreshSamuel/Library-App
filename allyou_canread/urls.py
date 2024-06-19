from django.urls import path
from .views import Choosen_Genre, AYCR_Genre_Pick, NoneValue

app_name = 'allyou_canread'
urlpatterns = [
    path('genre/', AYCR_Genre_Pick, name='genre'),
    path('library/', Choosen_Genre, name='library'),
    path('novalue/', NoneValue, name='no_value'),
]