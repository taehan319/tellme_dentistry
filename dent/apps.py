from django.apps import AppConfig

# このアプリケーションの設定ファイル
# アプリケーションの名前、モデル、管理画面の設定などを記述する

class DentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dent'
