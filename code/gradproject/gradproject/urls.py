from django.conf.urls import url, include
# from testapp import views
from test2 import views
from django.urls import path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# 최상위 project root에서 app 쪽으로 들어간 후, views에서 address_list 가져온다.

# testapp
# urlpatterns = [
#     path('gradproject/', views.address_list),
#     path('gradproject/<int:pk>/', views.address),
#     # views.address로 가는데 address에서는 def address(request, pk): 로 받는다.
#     # 그러므로 첫 번째 gradproject 두 번째는 pk로
#     path('login/', views.login),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

schema_url_patterns = [
    path('api/', include('gradproject.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gradproject.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]

# test2
urlpatterns = [
    path('gradproject/', views.address_list),
    path('gradproject/<int:pk>/', views.address),
    # views.address로 가는데 address에서는 def address(request, pk): 로 받는다.
    # 그러므로 첫 번째 gradproject 두 번째는 pk로
    path('app_login/', views.app_login),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view),
]
