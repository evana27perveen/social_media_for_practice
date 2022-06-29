from django.urls import path
from App_main import views

app_name = 'App_main'


urlpatterns = [
    path('', views.home, name='home'),
    path('new-story/', views.story, name='new-story'),
]
