from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import postMessage, replyMessage


def initialPage(request):
  lista_posts = postMessage.objects.all().order_by('-timePost')
  paginator = Paginator(lista_posts, 10)

  page_number = request.GET.get('page')
  posts = paginator.get_page(page_number)

  context = {'posts': posts}
  return render(request, 'index.html', context)

def adminPage(request):
    return render(request, 'admin.html')

def sendPost(request):
    if request.method == "POST":
        titlePost = request.POST.get('title') # Pega o título
        textPost = request.POST.get('contentPost')
        ip_usuario = request.META.get('REMOTE_ADDR') # Já aproveita e salva o IP que seu model exige
        
        if textPost:
            postMessage.objects.create(
                title=titlePost,
                message=textPost,
                ipUser=ip_usuario
            )
            
    return redirect("initialPage_Name")

from django.shortcuts import get_object_or_404, redirect
from .models import postMessage, replyMessage

def send_reply(request, post_id):
    if request.method == 'POST':
        post_pai = get_object_or_404(postMessage, id=post_id)
        texto_resposta = request.POST.get('contentPost')
        ip_usuario = request.META.get('REMOTE_ADDR')
        
        if texto_resposta:
            replyMessage.objects.create(
                post=post_pai,
                message=texto_resposta,
                ipUser=ip_usuario
            )
            
    return redirect('initialPage_Name')

from django.core.paginator import Paginator
from .models import postMessage

def listar_posts(request):
  lista_posts = postMessage.objects.all().order_by('-id')
  paginator = Paginator(lista_posts, 10)  # Define 10 posts por página

  page_number = request.GET.get('page')
  posts = paginator.get_page(page_number)

  return render(request, 'posts.html', {'posts': posts})