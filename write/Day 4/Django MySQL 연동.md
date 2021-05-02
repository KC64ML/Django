# DB 웹으로 출력할 때

* ![Database](D:\Computer_Science\Study\Django\Django\write\Day 4\사진2\Database.png)

  * mysql 정보들을 DATABASES에 입력한다.

* python manage.py inspectdb

  * 자동으로 해당 db에 존재하는 테이블들을 정리하여 터미널 창에 출력해준다.

  * ![mysql_input](D:\Computer_Science\Study\Django\Django\write\Day 4\사진2\mysql_input.png)

* models.py
  * 위 내용을 그대로 models.py에 복사한다.
  * ![models](D:\Computer_Science\Study\Django\Django\write\Day 4\사진2\models.png)
* python manage.py makemigrations
* python manage.py migrate
  * model이 변경되었기에 이를 DB에 알려준다.



# DB 앱으로 출력할 때





참고 자료 : https://hae-ong.tistory.com/25