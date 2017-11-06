from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'full_name', 'is_admin', 'email')
        read_only_fields = ('full_name', 'is_admin', 'email')
