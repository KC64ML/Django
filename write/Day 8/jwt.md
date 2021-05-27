### MySQL Workbench 업데이트

* Synchronize Model(Ctrl+Shift+Z) 실행



# JWT(Json Web Tokenization)

* Stateless 서버
  * token 기반 인증 시스템
  * 유저의 상태 정보를 저장하지 않고 클라이언트 측에서 들어오는 요청만으로 작업을 수행
  * 유저 정보를 확인하고 그에 맞는 적절한 권한을 부여할 때 '토큰'을 사용한다.
  * 서버에서 토큰을 클라이언트에 전달하면, 클라이언트는 이를 저장해두고 요청을 할 때 해당 토큰을 함께 보낸다.
* Stateful 서버
  * 클라이언트에서 요청을 받을 때마다 클라이언트의 상태를 계속 유지하고, 서비스를 제공할 때 항상 참고
* Example
  * User가 id와 password를 입력하고 로그인 한다.
  * login 성공하면 서버내에 session을 만들게 되고 세션 id, user id, password, 권한 등의 정보가 들어 있다.
  * 서버는 session 아이디인 쿠키(cookie)를 클라이언트에 보내고 클라이언트가 무언가 요청을 할 때마다 이 쿠키를 서버에 보내 서버가 확인한다.
  * 서버는 쿠키에 담긴 세션 id를 찾고, 유효시간 및 권한을 확인하여 요청에 맞는 특정 웹페이지를 보여준다.
  * ![참고자료](C:\Users\USER\Desktop\졸업작품\주차\14주차\사진\참고자료.png)







참고 주소 : https://moondol-ai.tistory.com/173?category=865999

