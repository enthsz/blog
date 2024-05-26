from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
# Create your views here.
def home_view(request):
    post = Post.objects.all()
    context = {
        'titulo':'Pagina Inicial',
        'posts': post,
    }
    return render(request, 'blog/home.html', context)


@login_required
def criar_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = CreatePostForm()     
    context = {
        'forms': form,
        'titulo': 'Criar Posts'
    }
    return render(request, 'blog/criar_post.html', context)


@login_required
def atualizar_post(request, pk):
    post = Post.objects.get(id=pk)

    if post.author != request.user:
        return HttpResponseForbidden('BLOQUEADO')
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    else:
        form = CreatePostForm(instance=post)
    
    context = {
        'forms':form,
        'titulo': 'Atualizar Post',
    }

    return render(request, 'blog/atualizar_post.html', context)


@login_required
def deletar_post(request, pk):
    post = Post.objects.get(id=pk)

    if post.author != request.user:
        return HttpResponseForbidden('BLOQUEADO')

    if request.method == 'POST':
        post.delete()
        return redirect('/')
    
    context = {
        'post':post
    }
    return render(request, 'blog/deletar_post.html', context)
    

def ver_posts(request):
    post_usuario = Post.objects.filter(author=request.user)

    context = {
        'titulo':"Meus Posts",
        'post_usuario':post_usuario
    }

    return render(request, 'blog/ver_posts.html', context)

