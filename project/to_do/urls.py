from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Register_view, name='register'),
    path('login/', views.Login_view, name='login'),
    path('home/', views.Home_view, name='home'),
    path('create/', views.create_task, name='create'),
    path('<int:id>/update/', views.update_task, name='update'),
    path('<int:id>/delete/', views.delete_task, name='delete'),
    path('logout', views.Logout_view, name='logout')
]