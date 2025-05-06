from django.urls import path
from .views import home_page_view, signup, signin, logout, settings

urlpatterns = [
    path('', home_page_view),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('settings', settings, name='settings')
]