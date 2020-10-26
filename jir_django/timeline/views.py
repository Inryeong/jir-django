from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from dsuser.models import Dsuser
from tag.models import Tag
from django.core.paginator import Paginator
from django.http import Http404


def timeline(request):
    user_id = request.session.get('user')
    dsuser = None
    if user_id:
        dsuser = Dsuser.objects.get(pk=user_id)
    return render(request, 'timeline.html')

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

def post_upload(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            dsuser = Dsuser.objects.get(pk=user_id)
            tags = form.cleaned_data['tags'].split(',')

            post = Post()
            post.writer = dsuser
            post.image_url = form.cleaned_data['image_url']
            post.contents = form.cleaned_data['contents']
            post.save()

            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post_upload.html', {'form': form})