from rest_framework import serializers
from firststartapp.models import LoginModel


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginModel
        fields = ('useridx', 'userid', 'userpassword')
