

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
    * Decoupling : 알아보기
  * ![django json api](D:\Computer_Science\Study\Django\Django\write\Day 3\사진4\django json api.png)
    * 안드로이드에서는 Http API를 요청하고, Backend에서는 Json으로 응답한다.
    * Android에서는 Component Renderer, View Controller가 필요하고
    * BackEnd에서는 API View, ORM, Serializer이 필요하다. 







참고 자료 : https://butter-shower.tistory.com/50

참고 자료 : https://butter-shower.tistory.com/52

