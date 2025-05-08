/** 処理 */
document.addEventListener('DOMContentLoaded', function () {
  // フォームのバリデーション
  const authForm = document.querySelector('.auth-form form');
  if (authForm) {
    authForm.addEventListener('submit', function (e) {
      const passphrase = document.getElementById('passphrase').value.trim();
      if (passphrase === '') {
        e.preventDefault();
        alert('合言葉を入力してください');
      }
    });
  }

  // メッセージの自動非表示
  const messages = document.querySelectorAll('.message');
  if (messages.length > 0) {
    setTimeout(function () {
      messages.forEach(function (message) {
        message.style.opacity = '0';
        setTimeout(function () {
          message.style.display = 'none';
        }, 500);
      });
    }, 3000);
  }
});