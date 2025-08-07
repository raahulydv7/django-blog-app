from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import CustomUserCreationForm,CustomLoginForm,UserProfileForm, PostForm,PostUpdateForm
from .models import Posts,UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def home(request):
    user_profile = request.user.userprofile
    following_profiles = user_profile.following.all()
    posts = Posts.objects.filter(user__userprofile__in=following_profiles).order_by('-created_at')
    return render(request, 'blog_app/home.html', {'posts': posts})

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'User created and logged in!')
                return redirect('home')  
        else:
            messages.error(request, "Can't create user. Please check the form.")

    else:
        form = CustomUserCreationForm()
    return render(request, 'blog_app/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = CustomLoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'blog_app/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.error(request, 'You have been logged out successfully.')
    return  redirect('login')

@login_required
def user_profile(request):
    profile = request.user.userprofile
    posts = Posts.objects.filter(user=request.user).order_by('-created_at')
    form = UserProfileForm(instance=profile)
    return render(request, 'blog_app/user_profile.html', {'form': form, 'posts': posts,'profile':profile})

@login_required
def update_user_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('user-profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'blog_app/user_profile_update.html', {'form': form})

@login_required
def follow(request, pk):
    target_user = get_object_or_404(User, id=pk)
    target_profile = get_object_or_404(UserProfile, user=target_user)
    current_user_profile = get_object_or_404(UserProfile, user=request.user)

    if target_user == request.user:
        messages.warning(request, "You can't follow yourself.")
    else:
        current_user_profile.following.add(target_profile)
        messages.success(request, f"You are now following {target_user.username}.")

    return redirect('search-users-profile', target_user.id)


@login_required
def unfollow(request, pk):
    target_user = get_object_or_404(User, id=pk)
    target_profile = get_object_or_404(UserProfile, user=target_user)
    current_user_profile = get_object_or_404(UserProfile, user=request.user)

    current_user_profile.following.remove(target_profile)
    messages.info(request, f"You unfollowed {target_user.username}.")

    return redirect('search-users-profile', target_user.id)

@login_required
def search_users(request):
    query = request.GET.get('q')
    users = []
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(userprofile__fname__icontains=query) 
        ).distinct()
    return render(request, 'blog_app/search_users.html', {'users': users, 'query': query})

@login_required
def search_users_profile(request,user_id):
    target_user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=target_user)
    posts = Posts.objects.filter(user=target_user).order_by('-created_at')

    return render(request, 'blog_app/search_user_profile.html', {
        'user': target_user,
        'profile': profile,
        'posts': posts
    })

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error creating post. Please check the form.')
    else:
        form = PostForm()
    
    return render(request, 'blog_app/create_post.html', {'form': form})

@login_required
def update_post(request,post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)

    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('home')
    else:
        form = PostUpdateForm(instance=post)

    return render(request, 'blog_app/update_post.html', {'form': form})

@login_required
def delete_post(request,post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('home')
    return render(request, 'blog_app/confirm_delete.html', {'post': post})
