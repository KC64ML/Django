from rest_framework import serializers
from assignment1.firststartapp.models import Sign_Up_Modle


class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sign_Up_Modle
        fields = ('usernumber', 'username', 'userpassword',
                  'userage', 'useraddress', 'user_disability_rating', 'login_usernumber')
