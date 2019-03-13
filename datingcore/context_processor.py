from django.conf import settings
from django.contrib.auth.decorators import login_required

from datingcore.models import Friend, CustomUser


def friend_list(request):
    users = []
    friends = []
    if request.user.is_authenticated:
        users = CustomUser.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

    return {'users': users, 'friends': friends}

