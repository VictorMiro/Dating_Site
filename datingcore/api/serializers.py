from rest_framework import serializers

from datingcore.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'gender',
            'email',
            'password',
            'avatar'
        )
