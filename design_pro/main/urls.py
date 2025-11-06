from django.urls import path
from .views import home, register, user_login, user_logout, dashboard, submit_request

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('submit_request/', submit_request, name='submit_request'),
]
