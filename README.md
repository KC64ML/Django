# Django

* 웹 프레임워크

* Python언어로 만들어졌다.
* Python 컴퓨터와 대화하는 하나의 방식
  * 데이터 분석, 머신 러닝이 가능하다.
  * 라이브러리 : 단순 활용가능한 도구들의 집합
  * 프레임 워크 : 라이브러리를 많이 가지고 있다. 
    * 도구들의 집합들을 사용할 수 있게 만들어졌다.
    * 프레임워크는 뼈대나 기반구조를 의미
    * 소프트웨어에써는 문제를 해결하기 위해서 상호 협력하는 클래스와 인터페이스의 집합
* 웹 프레임워크 django
  * 사용자 인터페이스
  * DB 연동
  * URL 파싱
  * 세션 관리
  * 관리자 페이지
  * Request 파싱 등등 가능
* 모델(Model), 템플릿(Template), 뷰(View) 
  * Django에서는 MTV패턴
* Django가 제공하는 것으로
  * 폼, 개발 프로세스, 관리자, 보안 등등을 제공한다.



# MTV 패턴

* 모델(Model), 템플릿(Template), 뷰(View) 

  * <img src="D:\Computer_Science\Study\Django\Django\write\Day 1\MTV 패턴.png" alt="MTV 패턴" style="zoom:80%;" />

  * 사진 주소 : [초보자를 위한 장고 Django 뿌시기🔥 - 구름EDU (goorm.io)](https://edu.goorm.io/lecture/16377/초보자를-위한-장고-django-뿌시기)

    * Client : 클라이언트, 사용자

    * View : 요청에 대한 응답을 하는 곳

    * Template : View에서 response로 쓰이는 HTML, XML 등등

      * render 함수를 통해 template (html)을 response로 client에게 보여준다.

    * Model : DataBase에 테이블 형태로 만들기 위한 설계

      * Relation : Model 상호간의 관계
      * DataBase : 실제로 데이터를 저장하는 곳
        * DB에서는 보통 SQL 언어를 사용한다.
      * Django에서 사용하는 Python과 SQL은 다른 언어이므로 통역사가 필요하다.
        * (이를 위한) 통역사 : ORM이다.
          * Python에서 DB와 서로 소통할 수 있게 만들어 준다.

      

      * Client가 View에게 요청을 하고, View는 Client에게 응답을 한다.
      * ex) 11번가 서버 접속을 예로 든다면
      * Client가 인터넷에서 11번가 검색 후 url 접속을 시도할 때
      * Client은 11번가 서버로 요청하게 되고 서버 View 다음 Model을 거친 후 DB에서 상품 객체들을 가져와서  html로 구성된 화면에 render함수를 통해 응답으로 사용자들 화면에 띄어준다.
      * View 같은 경우 11번가 서버를 의미하고, template 보이는 화면을 의미한다.
      * Model 같은 경우 11번가 화면에 보이는 상품 이름, 가격 등을 설계해서 만들어 진 것을 상품 Model이라고 한다.
        * 이러한 상품 모델(설계)로 찍어낸 상품 하나 하나를 객체라고 한다.
        * 한쪽 방향에서는 이러한 객체들을 DB에 저장하는 과정이다.
        * 다른 방향에서는 서버에서 DB로부터 불러와서 화면 template에 뿌려주는 역할을 한다. 이를 통해 화면에 보이게 된다.
      * template 틀 화면이라 생각하면 되고, Model 같은경우 구체적인 화면 구성요소로 생각하면 된다.

  * ex)

  * User : Username, Email, Password, Bdate

    * 컬럼, 필드, 애트리뷰트 : 특정 모델의 속성들
    * 모델의 컬럼마다 데이터 타입이 있다.
    * 데이터 타입(자료형) : 프로그래밍 언어에서 실수치, 정수, 불린 자료형 따위의 여러 종류의 데이터를 식별하는 분류
    * ![UserTable](D:\Computer_Science\Study\Django\Django\write\Day 1\UserTable.png)
    * 사진 주소 : [초보자를 위한 장고 Django 뿌시기🔥 - 구름EDU (goorm.io)](https://edu.goorm.io/lecture/16377/초보자를-위한-장고-django-뿌시기)
    * User 내용들을 migrate라는 과정을 통해 DB에 User Table을 생성한다.
      * Table : Excel 표와 비슷하다.

  * Post : Title, Content, ViewCount

    * 제목, 글 내용, 조회 수

  * Comment : content

    * 댓글

  * 이처럼 설계한 것들이 모델이고 이들로 객체를 찍어낸다.

