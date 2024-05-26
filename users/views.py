from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, PhotoUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Post


class LoginView(LoginView, SuccessMessageMixin):
    template_name = 'users/login.html'
    success_message = 'Usuario logado com sucesso'

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Login'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Registrado com sucesso')
            return redirect('login')
        
    else:
        form = RegisterForm()

    context = {
        'titulo': 'Registro Usuarios',
        'forms':form,
    }

    return render(request, 'users/registrar.html', context)


@login_required
def signout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        photo_form = PhotoUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if 'delete_image' in request.POST:
            if not request.user.profile.is_default_image():
                request.user.profile.delete_old_image()
                request.user.profile.image = 'fotos/padrao.jpg'
                request.user.profile.save()
            messages.success(request, 'A imagem do perfil foi excluída.')
            return redirect('perfil')


        if user_form.is_valid() and photo_form.is_valid():
            if 'image' in request.FILES: 
                if not request.user.profile.is_default_image():
                    request.user.profile.delete_old_image()

            user_form.save()
            photo_form.save()
            messages.success(request, 'Sua conta foi atualizada')
            return redirect('perfil')

    
    user_form = UserUpdateForm(instance=request.user)
    photo_form = PhotoUpdateForm(instance=request.user.profile)

    context = {
        'titulo':'Perfil',
        'user_form': user_form,
        'photo_form': photo_form,
    }
    return render(request, 'users/profile.html', context)



def ver_perfil(request, username):
    usuario = get_object_or_404(User, username=username)

    context = {
        'usuario':usuario
    }

    return render(request, 'users/ver_perfil.html', context)
