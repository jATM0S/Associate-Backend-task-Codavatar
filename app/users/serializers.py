from rest_framework import serializers
from users.models import CustomUser


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        ref_name = "User"
        fields = ["first_name","last_name", "date_joined", "email", "password","phone_no"]