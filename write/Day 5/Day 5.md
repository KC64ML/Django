## 처음 만난 오류

![질문내용](D:\Computer_Science\Study\Django\Django\write\Day 5\사진\질문내용.jpg)

* File "D:\ ~ py", line 24, in setup apps.populate(settings.INSTALLED_APPS)
  * apps.populate(settings.INSTALLED_APPS) 설정에서 File "~"을 실행
* File "D:\ ~ py", line 91, in populate app_config = Appconfig.create(entry)
  * app_config에 넣기.
* if mod_path and cls_name[0].isupper(): 
  * 를 실행하여 생성할 때 IndexError가 발생
* 이를 추측한다. 위를 보면, IndexError가 발생 다음 윗줄은 app을 만든다.
* 그 다음으로는  settings.INSTALLED_APPS 설정을 한다.
  * 설정? 이를 확인해본 결과
  * ![ok](D:\Computer_Science\Study\Django\Django\write\Day 5\사진\ok.png)
  * 'firststartapp.apps.Firststartappconfig.'
    * '.'처리가 잘못되었다.
  * 그러므로 settings.INSTALLED_APPS에서 잘못된 것이었다.

* django.db.utils.ProgrammingError (1146 ~ 에러 발생시)
  * ![ProgrammingError](D:\Computer_Science\Study\Django\Django\write\Day 5\사진\ProgrammingError.png)
  * 이는 migration을 생성하지 않았기에 발생한 에러이다.



## mysql와 연동하기 위해 Django에서는

* settings.py

  * ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DisabledDB',  # DB명
            'USER': 'root',    # DB 계정
            'PASSWORD': 'chang960626',  # 계정 비밀번호
            'HOST': 'localhost',    # 데이터베이스 주소(IP)
            'PORT': '3306',         # 데이터베이스 포트(보통 3306)
            'OPTIONS': {
                'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
            }
        }
    }
    ```

  * 

* python manage.py inspectdb

  * mysql로 부터 어떠한 테이블이 전달되었는지  확인한다.
  * ![inspectdb](D:\Computer_Science\Study\Django\Django\write\Day 5\사진\inspectdb.png)

* models.py

  * ```python
    from django.db import models
    # Create your models here.
    
    
    class LoginModel(models.Model):
        useridx = models.AutoField(primary_key=True)
        userid = models.CharField(max_length=45)
        userpassword = models.CharField(max_length=45)
    
    ```

* seralizer.py

  * ```python
    from rest_framework import serializers
    from firststartapp.models import LoginModel
    
    
    class LoginSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = LoginModel
            fields = ('useridx', 'userid', 'userpassword')
    
    ```

* views.py

  * ```python
    from rest_framework import viewsets
    from firststartapp.seralizer import LoginSerializer
    from firststartapp.models import LoginModel
    
    # Create your views here.
    
    
    class SignUpViewSet(viewsets.ModelViewSet):
        queryset = LoginModel.objects.all()
        serializer_class = LoginSerializer
    
    ```

* urls.py

  * ```python
    from django.contrib import admin
    from django.urls import include, path
    from rest_framework import routers
    from firststartapp import views
    
    router = routers.DefaultRouter()
    router.register(r'SignUp', views.SignUpViewSet)
    
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('admin/', admin.site.urls),
    ]
    
    ```

* python manage.py makemigrations

  * 테이블 생성하기 위한 주문서를 만듦

* python manage.py migrate

  * 주문서 내역대로 테이블 생성

* python manage.py runserver

  * ![실행결과](D:\Computer_Science\Study\Django\Django\write\Day 5\사진\실행결과.png)
  * Get을 눌려서 Login List로 넘어갔을 때
    * ![login](D:\Computer_Science\Study\Django\Django\write\Day 5\사진\login.png)
  * 







