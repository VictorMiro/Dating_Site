from django.conf import settings

from datingcore.models import Friend, CustomUser


def friend_list(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    return {'users': users, 'friends': friends}
