from django.conf import settings

def site_settings(request):
    """テンプレートで使用するサイト全体の設定を提供する"""
    return {
        'SITE_NAME': settings.SITE_NAME,
    }