# Register your models here.
# Django管理画面でアプリケーションのモデルを管理するための設定ファイル
# モデルの登録、一覧表示、編集画面の設定などを記述

from django.contrib import admin
from .models import Passphrase

# 管理画面に合言葉モデルを登録
@admin.register(Passphrase)
class PassphraseAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('phrase',)