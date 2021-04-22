from django.db import models

# Create your models here.


class Post(models.Model):  # 모델 상속
    title = models.CharField(max_length=200)
    # CharField() : 문자열 데이터 타입
    # max_length : 최대 길이
    content = models.TextField()
    # TextField : 1000자 정도의 문자열 데이터 타입
    view_count = models.IntegerField(default=0)
    # IntegerField = 정수형 데이터 타입
    # default : 기본값 (초기화 값)

    # DateTimeField : 시간 날짜 데이터 타입
    # auto_now_add : 생성될 때 현재시간 저장
    # auto_now : 생성, 수정될 때 현재시간 저장
    create_at = models.DateTimeField(auto_now_add=True)  # 언제 생성
    update_at = models.DateTimeField(auto_now=True)  # 언제 업데이트 되었는지
