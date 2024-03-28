
from django.urls import path
from .views import Index, home
urlpatterns = [
path('', Index.as_view(), name='index'),
path('home/', home, name='home'),
]
