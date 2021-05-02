from rest_framework import viewsets
from firststartapp.seralizer import SignUpSerializer
from firststartapp.models import Sign_Up_Modle

# Create your views here.


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = Sign_Up_Modle.objects.all()
    serializer_class = SignUpSerializer
