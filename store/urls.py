from django.urls import path
from .views import home_view, signup_view, login_view, verification_view

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('activate/<uid64><token>/', verification_view, name='activate'),
]
