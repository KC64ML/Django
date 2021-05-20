from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import LoginModels
from .serializers import LoginSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate

# Create your views here.


class LoginViewSet(viewsets.ModelViewSet):
    queryset = LoginModels.objects.all()
    serializer_class = LoginSerializer

    @csrf_exempt
    def app_login(request):
        if request.method == 'POST':
            print("리퀘스트 로그" + str(request.body))
            id = request.POST.get('userid', '')
            pw = request.POST.get('userpw', '')
            print("id = " + id + " pw = " + pw)

            result = authenticate(username=id, password=pw)

            if result:
                print("로그인 성공!")
                return JsonResponse({'code': '0000', 'msg': '로그인성공입니다.'}, status=200)

            else:
                print("실패")
                return JsonResponse({'code': '1001', 'msg': '로그인실패입니다.'}, status=200)


#     # app 로그인
