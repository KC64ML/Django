# 시작하기에 앞서

* 가장 먼저 해야할 것
  * 현재 myvenv 디렉터리 메모리가 매우 커 git디렉터리 밖에 나두었다.
  * 현재 디렉터리 경로에서 cd를 이용하여 myvenv가 있는 디렉터리(한 칸위 디렉터리로) 이동한 후
  * source myvenv/Scripts/activate를 입력하여 가상머신을 실행한 후
  * 다시 project가 있는 디렉터리로 돌아와 
  * python manage.py runserver를 입력하면 실행이 된다.

# Django 모델링

* project 디렉터리에서

  * __init__.py
    * package임을 알려주는 모듈
  * setting.py
    * Django의 설정을 담당하는 부분
    * 가장 중요한 것
      * 현재 최상위 디렉터리(프로젝트) -> 현재 최상위 디렉터리(프로젝트)-> setting.py
      * INSTALLED_APPS에 현재 crudapp이 설치되었다는 것을 알려줘야 한다.
      * ![INSTALLED_APPS](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\INSTALLED_APPS.png)
  * urls.py
    * app 경로설정
  * wsgi.py
    * webserver 게이트웨이 인터페이스, 배포할 때 파이프라인 연결하는 구간
  * manage.py
    * 다양한 명령어가 저장되어 있는 곳 

* 모델링을 통한 테이블 생성

  * models.py에서 모델링을 한다.
  * python manage.py makemigrations로 주문서를 만든다.
  * python manage.py migrate로 주문서 내역대로 테이블을 생성한다.

* app 생성

  * 최상위 프로젝트에서 python manage.py startapp app이름
    * 이렇게 할시, app이 만들어지고 안에는 밑과 같이 py가 생성됨
    * ![startappname](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\startappname.png)

* app 디렉터리

  * admin.py : 관리자 페이지 설정 관련 모듈

  * views.py : request를 처리해서 response를 내놓은 곳

  * models.py : 모델을 표현하는 곳이다.

    * ![Postclass](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\Postclass.png)

    * ```python
      from django.db import models
      
      
      \# Create your models here.
      
      
      class Post(models.Model): # 모델 상속
      
        title = models.CharField(max_length=200)
      
        \# CharField() : 문자열 데이터 타입
      
        \# max_length : 최대 길이
      
        content = models.TextField()
      
        \# TextField : 1000자 정도의 문자열 데이터 타입
      
        view_count = models.IntegerField(default=0)
      
        \# IntegerField = 정수형 데이터 타입
      
        \# default : 기본값 (초기화 값)
      
      
      
        \# DateTimeField : 시간 날짜 데이터 타입
      
        \# auto_now_add : 생성될 때 현재시간 저장
      
        \# auto_now : 생성, 수정될 때 현재시간 저장
      
        create_at = models.DateTimeField(auto_now_add=True) # 언제 생성
      
        update_at = models.DateTimeField(auto_now=True) # 언제 업데이트 되었는지
      ```

    * 현재 최상위 project 밑 setting에서 app 설정을 완료한 상태라면 실행시, model이 생성된다.

    * python manage.py makemigrations로 주문서를 만든다.

    * ![app 생성](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\app 생성.png)

    * ![migration생성](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\migration생성.png)

    * ![migration init](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\migration init.png)

    * id : 기본키(primary key), 고유 식별 가능한 정보

      * 한 table 안에 동일한 id (primary key)를 갖는 객체는 없어야 한다.

    * title, content, view_count, create_at, update_at은 models.py에서 입력한 것

    *  python manage.py migrate : DB에 테이블 형태로 Post을 만든다.

    * python manage.py migrate로 주문서 내역대로 테이블을 생성한다.

    * ![주문서](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\주문서.png)

    * ``` database
      python manage.py shell : shell에 진입한다.(이후)
      * shell에서 객체 생성 및 조회할 수 있다.
      
      from crudapp.models import Post   
      * crudapp : app 이름, Post : DB에 생성한 Table 이름
      
      Post.objects.create(title="간장게장 담그는 법",content="알이 꽉찬 꽃게")
      * ORM, 이를 통해 SQL과 소통을 한다.
      
      Post.objects.all() : 모든 host 테이블 안에 있는 객체들을 불러온다.
      
      # ORM을 통해 조금 전 생성한 id = 1을 갖는 객체를 변수에 담아 속성들을 출력해보기
      post = Post.objects.get(id=1)
      - Post object들 중에서 id를 1로 갖는 object를 post에 저장한다.
      post.title
      - post의 title을 호출한다.
      post.content
      - post의 content을 호출한다.
      post.view_count
      - post의 view_count을 호출한다.
      post.create_at
      - post의 create_at을 호출한다.(생성된 날짜가 출력된다.)
      exit()
      - 쉘에서 나올 때 사용
      ```

    * ![post create](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\post create.png)

      * <Post: Post object (1)> : 1이라는 id 값을 갖는 게시글의 객체라는 뜻이다.

    * ![Post object 조회](D:\Computer_Science\Study\Django\Django\write\Day 3\사진\Post object 조회.png)

      * Post.objects.all() : 모든 host 테이블 안에 있는 객체들을 불러온다.
      * <QuerySet [<Post: Post object (1)>]> : QuerySet Box안에서 Post 객체 첫 번째 값을 불러온다.





