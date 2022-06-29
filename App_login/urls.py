from django.urls import path
from App_login import views

app_name = 'App_login'


urlpatterns = [
    path('new_user/', views.signup_sys, name='signup'),
    path('login/', views.login_sys, name='login'),
    path('logout/', views.logout_sys, name='logout',)

]
