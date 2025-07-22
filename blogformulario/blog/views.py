from django.shortcuts import render, redirect
from .forms import PostForm  # 👈 esto soluciona el error

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Procesa los datos enviados
        if form.is_valid():
            form.save()  # Guarda en la base de datos
            return redirect('post_exito')  # Redirecciona a otra vista
    else:
        form = PostForm()  # Muestra un formulario vacío
    return render(request, 'blog/crear_post.html', {'form': form})

def post_exito(request):
    return render(request, 'blog/post_exito.html')