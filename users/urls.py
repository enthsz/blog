from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registro_usuarios/', views.registro, name='registro-usuarios'),
    path('signout/', views.signout, name='signout'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('perfil/', views.profile, name='perfil'),
    path('ver-perfil/<str:username>/', views.ver_perfil, name='ver-perfil'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)