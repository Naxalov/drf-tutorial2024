
from django.urls import path
from .views import Index, home, AddTask
urlpatterns = [
path('', Index.as_view(), name='index'),
path('home/', home, name='home'),
path('add/', AddTask.as_view(), name='add'),
]
