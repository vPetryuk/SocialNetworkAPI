from rest_framework import serializers
# from users.models import NewUser
from .models import User, photos
from django.contrib.auth.models import User as NewUser
# class PhotosSerializer(serializers.Serializer):
#     smallphoto = serializers.CharField(max_length=1000, required=False)
#     bigphoto = serializers.CharField(max_length=1000, required=False)


class UserSerializer(serializers.ModelSerializer):
    photos = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=photos.objects.all()
    )
    class Meta:
        model = User
        fields ='__all__'
        depth = 1

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance