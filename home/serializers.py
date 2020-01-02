from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TrainerInfo,Trainer,EmailSend
import myapp.views #import email
import uuid


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # ff = "sd"
    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'password','is_staff','is_active','token']
        extra_kwargs = {'password': {'write_only':True, 'required':True}}

    def create(self, validated_data):
        # random_str = str(uuid.uuid4())
        # random_str = random_str.upper()
        # random_str = random_str[:6]
        # print(validated_data)
        user = User.objects.create_user(**validated_data)
        # print(user.pk)
        
        q = User.objects.filter(username=user)
        q.update(is_active=False)
        # q.update(token=random_str)
        myapp.views.email(validated_data,user)
        # tt = uuid
        # print(user.token)
        # print(user)
        # print(user.token+"injkn")
        return user

class TrainerInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainerInfo
        fields = "__all__"
        # extra_kwargs = {'password': {'write_only':True, 'required':True}}

    # def create(self, validated_data):
    #     user = TrainerInfo.objects.create_user(**validated_data)
    #     return user


class TrainerName(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailSend
        fields = "__all__"


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['token']
        # extra_kwargs = {'password': {'write_only':True, 'required':True}}
