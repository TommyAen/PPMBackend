from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser



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
