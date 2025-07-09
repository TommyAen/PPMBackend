from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pic", blank=True, null=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def friends(self):
        accepted_from = FriendRequest.objects.filter(from_user=self, status='accepted').values_list('to_user',flat=True)
        accepted_to = FriendRequest.objects.filter(to_user=self, status='accepted').values_list('from_user', flat=True)
        return CustomUser.objects.filter(id__in=list(accepted_from) + list(accepted_to))

    def is_friend_with(self, other_user):
        return other_user in self.friends()

class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f'{self.from_user.username} -> {self.to_user.username} ({self.status})'

