# REST API

* Representational State Transfer
* REST란?
  * http의 url 과 http method(GET, POST, PUT, DELETE)를 사용해서 API 가독성을 높인 구조화된 시스템 아키텍쳐(framework)라고 생각하면 된다.
  * 하나의 URL로 최소 4가지의 HTTP method를 전송할 수 있다.
  * 스마트폰 등장으로 웹으로만 서비스를 제공하는 것에 한계가 있어 등장하게 되었다.
  * JSON, XML 등과 같은 형식을 통해서 데이터를 다루는 별도의 API 서버를 담당한다.
  * Restful 아키텍처를 HTTP Method와 함께 사용해 웹, 데스크탑 앱, 스마트폰 어플들까지 하나의 API 서버를 생성할 수 있다.
  * View 클래스 자체가 RESTful 한 서버를 만들기에 최적화된 framework이다.
*  DRF(Django Rest Framework)
  * Django 안에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리이다.
  * Serializer
    * 직렬화된 클래스로서, 사용자의 DB안에 사용자 프로필 사진, 이메일, 이름, 성별이 있다고 가정하면 사용자 모델 인스턴스를 JSON 형태 또는 Dictionary 형태로 직렬화 할 수 있다.
    * ex)로 아래와 같은 User가 있다고 가정한다.
    * DRF의 serializer를 통해 모델 인스턴스를 직렬화 할 수 있다.
    * ![DRF serializer](D:\Computer_Science\Study\Django\Django\write\Day 3\사진4\DRF serializer.png)
    * 사용자 정보를 열람하는 URL : /serializer/user/<user id>/
    * View에서는 user_id의 해당하는 모델 인스턴스의 정보를 리턴한다.
    * 이럴 경우, /serializer/user/1/이라는 URL로 요청했을 때, user_id가 1인 사용자의 정보를 JSON 형태로 응답받을 수 있다.
    * 정리하자면, 사용자 프로필 페이지에 접근했을 때 사용하는 View라고 하면, 사용자 페이지에 들어갈 때마다 해당하는 사용자의 user_id만 URL에 입력하게되면 각 사용자의 정보를 JSON 형태로 응답 받을 수 있다.
    * 이러한 기능을 하는 Serializer를 ModelSerializer이라고 부른다.
  * DRF 실제 설치
    * pip install djangorestframework
    * ![djangorestframework 설치](D:\Computer_Science\Study\Django\Django\write\Day 3\사진4\djangorestframework 설치.png)
    * rest framework 추가
    * ![rest framework app 추가](D:\Computer_Science\Study\Django\Django\write\Day 3\사진4\rest framework app 추가.png)



* Moblie, Django?
  * 모바일에서 장고를 사용하는 이유는
    * 프론트엔드와 백엔드간의 REST 기반의 통신 아키텍처로 완전한 Decoupling을 용이하게 할 수 있어 사용한다.
    * Decoupling : app을 다시 배치하지 않고도 parameters(매개 변수)를 변경할 수 있게 설정을 구성해준다. 
  * ![django json api](D:\Computer_Science\Study\Django\Django\write\Day 3\사진4\django json api.png)
    * 안드로이드에서는 Http API를 요청하고, Backend에서는 Json으로 응답한다.
    * Android에서는 Component Renderer, View Controller가 필요하고
    * BackEnd에서는 API View, ORM, Serializer이 필요하다. 



# 실습

```bash
- django-admin startproject studyrestframework
: 프로젝트 생성
- cd studyrestframework/
: 프로젝트 디렉터리로 이동
- pip install djangorestframework
: djangorestframework 설치(안드로이드와 연동할 때 사용)
- python manage.py migrate
: migrations(이동, 이주)를 적용 또는 취소, DB를 초기화
- python manage.py createsuperuser
: 슈퍼 유저 만듦
- python manage.py showmigrations
: 현재 상황을 추척

```

### Serializer 생성

* JSON, XML 파일등으로 바꾸어 준다.

```python
# crudproject/phoneapp/seralizer.py

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # HyperlinkedModelSerializer
    class Meta:
        model = Group
        fields = ('url', 'name')

```

* HyperlinkedModelSerializer이외 다른 것을 사용할 수 있지만, hyperlink를 하는게 좋은 RESTful 디자인이다.

### Views.py

```python
# crudproject/phoneapp/views.py
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from phoneapp.seralizer import UserSerializer, GroupSerializer

# project 경로 설정할 필요 없다.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

```

* viewsets : view들을 결합
  * 여러 가지 API 기능을 통합해서 하나의 API Set로 제공하는 것
  * 하나의 Model을 가지고 list, detail 등 각각의 API를 만들어 보면, 중복되는 로직이 많다.
    * 이럴 때, ViewSet을 쓰게 되면 중복되는 로직의 코드를 줄일 수 있어 코드의 효율성을 높일 수 있다.
  * list(), create() 액션을 제공
  * Viewsets을 위한 method 핸들러들은 as_view()함수를 사용해 view가 끝나는 시점에 해당하는 행동을 취할 때 바인딩한다.
  * 일반적으로 url 설정 내에서 viewset들의 view를 명시적으로 하는 것보다 router클래스로 viewset을 등록하는 것이 좋다.

### urls.py

```python
# crudproject/crudproject/urls.py

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from phoneapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

```

* view대신 viewset을 사용해서 자동적으로 URLconf를 우리의 API에 생성
* router클래스에 등록해주기만 하면 된다.
* API, URL들을 기본 제공하는 기능에서 추가하고 싶을 때 URLconf를 명시해주면 된다.
  * URLconf : url 요청이 들어오면 어떤 views.py의 함수를 실행시킬지 정희하는 단계
  * __path('클라이언트로 받는 요청 URL', views.py에 정의되어있는 함수)__
  * 해당 프로젝트 app 마다 urls.py를 생성 후 각각 관리하기가 매우 좋은 방법
  * Django는 기본적으로 라우팅을 위해 urls.py를 찾을 때 프로젝트 디렉터리 안에 있는 urls.py를 찾는다.
    * 이때, include을 사용한다.
    * path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
      * include를 사용 위치경로 설정, rest_framework 하위의 urls.py 파일을 찾아 실행한다. namespace는 rest_framework로 되어 있다.

### # settings.py

```python
# crudproject/crudproject/settings.py

INSTALLED_APPS = [
    ~
    'rest_framework',   # 추가
]


~

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### 실행 및 결과

```bash
python manage.py runserver
```

![Api Root](D:\Computer_Science\Study\Django\Django\write\Day 3\사진5\Api Root.png)





참고 자료 : https://jong-seok-ap.tistory.com/32

참고 자료 : https://butter-shower.tistory.com/50

참고 자료 : https://butter-shower.tistory.com/52

