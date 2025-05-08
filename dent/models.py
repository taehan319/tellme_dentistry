from django.db import models

# Create your models here.
# アプリケーションで使用するモデルを定義するファイル
# モデルとはデータベースのテーブルと関連するフィールドのこと
class Passphrase(models.Model):
    """合言葉を管理するモデル"""
    phrase = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.phrase