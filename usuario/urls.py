from django.urls import path
from .views import login_view, index_view

urlpatterns = [
    path('', login_view, name='login'),  
    path('index/', index_view, name='index'),  
]
