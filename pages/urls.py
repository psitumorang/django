from django.urls import path
from .views import home_page_view, signup

urlpatterns = [
    path('', home_page_view),
    path('signup', signup, name='signup')
]