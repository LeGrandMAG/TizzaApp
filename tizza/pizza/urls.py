from django.urls import include, path

from .views import index

urlpatterns = [
    path('<int:pid>', index, name='pizza'),
    path('random', index, name='random'),
]