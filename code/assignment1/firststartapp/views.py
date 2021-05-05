from rest_framework import viewsets
from firststartapp.seralizer import LoginSerializer
from firststartapp.models import LoginModel

# Create your views here.


class LoginViewSet(viewsets.ModelViewSet):
    queryset = LoginModel.objects.all()
    serializer_class = LoginSerializer
