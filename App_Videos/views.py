from django.shortcuts import HttpResponseRedirect, render, redirect
from django.urls import reverse
from App_Videos.models import *
from App_Videos.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def videos(request):
    videos = Video.objects.all()
    result = False
    if request.method == 'POST':
        search = request.POST.get('search')
        search = search.strip()
        if search:
            videos = Video.objects.filter(title__icontains=search)
            result = search
    return render(request, 'App_Videos/videos.html', {'videos': videos, 'result': result})


def video_details(request, pk):
    video = Video.objects.get(pk=pk)
    video.views += 1
    video.save()
    comments = Comment.objects.filter(video=video)
    likes = Likes.objects.filter(video=video)
    isLiked = False
    if request.user.is_authenticated:
        isLiked = Likes.objects.filter(video=video, user=request.user)
        
    if request.method == 'POST':
        if not request.user.is_authenticated:
            first = reverse('App_Auth:login')
            next = reverse('App_Videos:video_details', kwargs={'pk': pk})
            return redirect("{}?next={}".format(first, next))
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            messages.success(request,"Comment Added!")
            return HttpResponseRedirect(reverse('App_Videos:video_details', kwargs={'pk': pk}))
    else:
        form = CommentForm()
    return render(request, 'App_Videos/video_details.html', context={'video': video, 'comments': comments, 'likes': likes, 'isLiked': isLiked, 'form': form})

@login_required
def like(request, pk):
    video = Video.objects.get(pk=pk)
    isLiked = Likes.objects.filter(video=video, user=request.user)
    if isLiked:
        isLiked.delete()
        messages.warning(request,"Like Removed")
    else:
        like = Likes(video=video, user=request.user)
        like.save()
        messages.success(request,"Liked Successfully")
    return HttpResponseRedirect(reverse('App_Videos:video_details', kwargs={'pk': pk}))

