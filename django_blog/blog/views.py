from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'blog/register.html', context)
    
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
        context = {'user': user, 'form': form}
        return render(request, 'blog/profile.html', context)

def home(request):
    return render(request, 'blog/home.html')

@login_required
def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context)