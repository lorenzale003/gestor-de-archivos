from django.urls import include, path
from . import views

 
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('dashboard/', include('dashboard.urls'))
]