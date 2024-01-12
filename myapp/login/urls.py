from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.login, name='main'),
    path('register', views.register, name='submit'),
    path('register/', views.login, name='main'),
    path('recipe',include('recipe.urls'))
]