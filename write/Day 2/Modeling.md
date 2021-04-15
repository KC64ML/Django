# vscode 설정

* 먼저 git Bash를 TERMINAL에 추가한다.
* ![Terminal](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\Terminal.png)
  * vscode 첫 시작시 TERMINAL 기본 쉘로 Command Prompt, PowerShell만 존재할 것이다.
  * ![terminal2](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\terminal2.png)
* ctrl + shift + '(물결) 
  * bash 터미널 창이 뜬다.
  * ![bash](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\bash.png)
* vscode EXPLORER에 디렉터리를 OPEN 한다.
* 현재 TERMINAL에 git bash를 열어준다. (alt + shift + `)
* ![터미널](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\터미널.png)

* 위 자료는 웹 주소 : https://integer-ji.tistory.com/81?category=745989 에서 가져온 자료입니다.



## 이제 중요

* python 버전 확인하기

  * python --version
  * 3.6 버전 이상 진행해야한다.

* venv(가상 환경) 생성하기

  * python -m venv myvenv
    * myvenv : 생성하려는 가상 환경 이름
    * 가상환경이라는 걸 쉽게 알기 위해 venv를 붙여줘야 한다.
  * 실행시 현재 디렉터리 경로에 myvenv 디렉터리가 설치된다.
  * 가상 환경(Virtual environment) : virtualenv라고도 한다.
    * 기존에 설치되어있는 Python과 django를 분리시켜 준다.
    * 다른 프로젝트들과 충돌이 안나게 독립적인 환경을 만들어 준다.

* 가상 환경 실행하기

  * source myvenv(가상 환경 이름)/Scripts/activate

  * ![source](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\source.png)

    * 정상 실행될 시 myvenv(가상 환경 이름) 출력
      * 이제부터 myvenv 가상환경 안에 있는 것을 말하는 것이다.
      * pip, setuptools, wheel 가상환경을 시작할 때 기본으로 설치된 것이다.

    * 가상 환경을 종료하는 방법
      * deactivate 또는 터미널 종료하면 된다.

  * pip란?

    * pip는 파이썬으로 작성된 패키지 라이브러리를 관리해주는 시스템
      * 리눅스에서는 apt-get이다.
    * pip는 python 3.4 이후 버전에는 기본적으로 포함되어 있다.
    * pip list
      * 현재 내 컴퓨터에 설치된 python package 목록을 볼 수 있다.
    * pip install --upgrade pip
      * pip를 최신 버전으로 업그레이드 할 때 사용
    * pip install <패키지 이름>
      * pip를 이용해 파이썬 라이브러리 패키지를 설치
    * pip uninstall <패키지 이름>
      * pip를 이용해 설치된 패키지를 제거
    * 많이 사용하는 패키지들은 대부분 pip를 이용해 설치할 수 있다.

* Django 설치하기

  * pip install django
    * django 패키지를 설치한다.
    * 특정 버전의 django를 다운로드 하기 위해서는
      * pip install django==2.x.x 식으로 입력하면된다.

* ![pip install](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\pip install.png)

  * 만약 설치 완료 후 업그레이드를 요구한다면
    * python -m pip install --upgrade pip를 입력해주면 된다.

* ![python upgrade](D:\Computer_Science\Study\Django\Django\write\Day 2\사진\python upgrade.png)





## Django를 이용해 project 만들고, app 생성

* pip 업그레이드가 완료되었다면 django-admin을 이용해 project를 만들어 준다.
  * django-admin startproject crudproject
    * crudproject를 생성한다.
* django 서버 작동
  * 이제 crudproject 경로로 이동하여, runserver를 한다.
  * python manage.py runserver
    * 명령어를 실행하면 기본적으로 내부 IP의 8000번 포트로 개발 서버를 띄운다.
    * manage.py를 이용하여 http://127.0.0.1:8000/ 서버가 시작된다.
    * 열린 서버를 닫을 때 : ctrl + c
    * 8080 포트 바꾸려면
      * python manage.py runserver 8080
    * 서버 IP 바꾸기
      * python manage.py runserver 0:8000
  * ![runserver](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\runserver.png)
  * ![django internet](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\django internet.png)
* app 만들기
  * python manage.py startapp crudapp
    * crudapp 앱 생성
    * ![startapp](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\startapp.png)
* project와 app 이어주기
  * INSTALLED_APPS = [~]에 'crudapp.apps.CrudappConfig', 를 추가해준다.
  * ![setting](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\setting.png)
* app에 templates 폴더 추가, 폴더 안에 home.html 만들기
  * 이때, MTV 패턴 중 T, Template 폴더가 생성되며 안에는 html이 들어간다. 
  * ![template](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\template.png)
* view.py에 home란 이름의 함수 만들기
  * View를 메서드로 구현한 것이 view.py이며 웹이나 Database에서 온 요청을 처리한다.
  * home는 요청이 들어오면 home.html을 실행
  * ![viewpy](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\viewpy.png)
* project의 urls.py와 app의 views.py 연결하기
  * from crudapp import views
  * path(' ',views.home, name='home'),
    * 이때 템플릿 처리를 한 후 html로 된 응답 데이터를 웹 클라이언트로 반환한다.
  * app과 project는 다른 디렉터리에 있어 서로 연결한다.
  * ![urlspy](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\urlspy.png)
* 이제 입력한 내용들을 확인하기 위해 python manage.py runserver 입력한다.
  *  http://127.0.0.1:8000/ 클릭시 출력내용 확인가능
  * ![runserver2](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\runserver2.png)
* 결과
  * ![result](D:\Computer_Science\Study\Django\Django\write\Day 2\사진2\result.png)
* 지금까지 한 내용은 MVT 패턴 중 View, Template을 사용하였다.
* View 같은 경우, views.py 메서드로 구현되며 웹이나 Database에서 온 요청을 처리한다.
  * 최종으로 데이터를 html로 변환하기 위해 Template 처리를 한 후 html로 응답 데이터를 웹 클라이언트로 반환한다.
* Template은 html 파일들이 저장된 디렉터리이다.



* runserver 나가기 : ctrl + c



[참고 자료] : https://m.blog.naver.com/complusblog/221177123238

[참고 자료] : https://integer-ji.tistory.com/82?category=745989

