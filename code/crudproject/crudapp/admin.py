from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post
# Post를 가져온다.

# .models: 같은 경로에 있으면 .으로 처리

# # Register your models here.
# admin.site.register(Post)
# # 화면에 Post 띄우기


# 데코레이터 : 함수나 클래스를 꾸며주는 역할
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'view_count',
        'create_at',
        'update_at'
    )
    # list_display : 원하는 컬럼들을 보여준다.

    search_fields = (
        'title',
    )
    # search_fields : 검색이 가능한 컬럼 설정, 항상 ','를 붙여야 한다.

    # list_filter, list_display_links 알아보기
