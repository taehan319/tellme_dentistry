from django.urls import path
from . import views

app_name = 'dent'

urlpatterns = [
    path('', views.index, name='index'),  # トップページ
    path('authenticate/', views.authenticate_view, name='authenticate'),  # 認証処理
    path('dental-info/', views.dental_info, name='dental_info'),  # 認証後のページ
]