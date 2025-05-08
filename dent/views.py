# Create your views here.
# URLと処理を関連付けるビューを定義するファイル
# ユーザーからのリクエストを受け取り、処理結果を返すコードを記述する
# つまりDjango側(バックエンド側)でどのような動作をするのかを記述するところである

from django.shortcuts import render, redirect
from django.contrib import messages

# 合言葉のリスト（定数定義）
VALID_PASSPHRASES = ["はみがき", "歯磨き", "ハミガキ"]

def index(request):
    """トップページを表示"""
    return render(request, 'dent/index.html')

def authenticate_view(request):
    """合言葉認証処理"""
    if request.method == 'POST':
        passphrase = request.POST.get('passphrase', '')
        
        if passphrase in VALID_PASSPHRASES:
            # 認証成功時、セッションに認証状態を保存
            request.session['authenticated'] = True
            return redirect('dent:dental_info')
        else:
            # 認証失敗
            messages.error(request, '合言葉が正しくありません。')
            return redirect('dent:index')
    
    # GETリクエストの場合はトップページにリダイレクト
    return redirect('dent:index')

def dental_info(request):
    """認証後のページを表示"""
    # 認証済みかチェック
    if request.session.get('authenticated', False):
        return render(request, 'dent/dental_info.html')
    else:
        messages.error(request, '認証が必要です。')
        return redirect('dent:index')