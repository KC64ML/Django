# Http, json

* Django에서는 request와 response 객체로 상태를 서버와 클라이언트가 주고 받는다.
  * djanog http 모듈에서 HttpRequest와 HttpResponse API를 제공
  * 서버-클라이언트 통신시
    * 특정 페이지가 요청되면, 장고는 요청 시 메타데이터를 포함하는 HttpRequest 객체를 생성
    * 장고는 urls.py에서 정의한 특정 View 클래스/함수에 첫 번째 인자로 해당 객체(request)를 전달
    * 해당 View는 결과 값을 HttpResponse 혹은 JsonResponse 객체에 담아 전달

* HttpRequest

  * 주요 속성(Attribute)

  * ```http
    HttpRequest.body  # request의 body 객체
    HttpRequest.headers # request의 headers 객체
    HttpRequest.COOKIES # 모든 쿠키를 담고 있는 딕셔너리 객체
    HttpRequest.method # reqeust의 메소드 타입
    HttpRequest.GET # GET 파라미터를 담고 있는 딕셔너리 같은 객체
    HTTpRequest.POST # POST 파라미터를 담고 있는 딕셔너리 같은 객체
    ```

* HttpResponse(data, content_type)

  * response을 반환하는 가장 기본적인 함수

  * 주로 html를 반환

  * ```python
    # string 전달하기
    HttpResponse("Here's the text of the Web page.")
    ```

* HttpResponseRedirect(url)
  * response를 하지 않고, 지정된 url페이지로 redicrect를 한다.
  * 첫 번째 인자로 url 지정, 경로는 절대경로 혹은 상대경로를 이용할 수 있다.

* Render

  ```python
  render(request(필수), template_name(필수), 
        context=None, content_type=None, 
        status=None, using=None)
  ```

  * `render`는 `httpRespose` 객체를 반환하는 함수로 template을 context와 엮어 `httpResponse`로 쉽게 반환해 주는 함수임
  * template_name에는 불러오고 싶은 템플릿명을 적음
  * context에는 View에서 사용하던 변수(dictionary 자료형)를 html 템플릿에서 전달하는 역할을 함. key 값이 템플릿에서 사용할 변수이름, value값이 파이썬 변수가 됨

* JsonResponse

  * ```python
    JsonResponse(data, encoder=DjangoJSONEncoder,
                 safe=True, json_dumps_params=None, 
                 **kwargs)
    ```

    * `HttpResponse`의 subclass로, JSON-encoded response를 생성할수 있게 해 줌. 대부분의 기능은 superclass에서 상속받음
    * 첫번째 인자로는 전달할 데이터로서 반드시 dictionary 객체여야 함.
    * encoder는 데이터를 [serialize](https://docs.djangoproject.com/en/3.0/topics/serialization/#serialization-formats-json)할 때 이용된다.
    * response를 커스터마이징 하여 전달하고 싶을 때, http status code에 더하여 메세지를 입력해서 전달할 수 있다.
    * 프론트엔드 개발자와 협의하여 약속된 메세지를 던진다.
    * 전달할 메세지가 없고 status code만 전달한다면 HttpResponse를 사용한다.









참고 주소 : https://velog.io/@jcinsh/Django-request-response

