from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser, FriendRequest



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile-detail', pk=user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(CustomUser, id=user_id)
    if to_user != request.user:
        FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect('profile-detail', pk=to_user.id)

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    friend_request.status = 'accepted'
    friend_request.save()
    return redirect('friends_list')

@login_required
def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    friend_request.status = 'rejected'
    friend_request.save()
    return redirect('friends_list')
