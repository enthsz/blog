from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('criar-post', views.criar_post, name='criar-post'),
    path('atualizar-post/<int:pk>/', views.atualizar_post, name='atualizar-post'),
    path('deletar-post/<int:pk>/', views.deletar_post, name='deletar-post'),
    path('ver_posts', views.ver_posts, name='ver-posts')

]
