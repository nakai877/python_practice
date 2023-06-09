from django.views import generic
from django.urls import reverse_lazy
from .forms import CorporateContactForm
from .models import CorporateContact
from django.template.loader import get_template
from accounts.models import CustomUser


class CorporateContactCreate(generic.CreateView):
    model = CorporateContact
    form_class = CorporateContactForm
    template_name = 'contacts/corporate_contact_create.html'
    success_url = reverse_lazy('contacts:corporate_create')

def form_valid(self, form):
    # 入力内容に問題がなければ呼ばれるメソッド

    # フォームの役割
    # 1. 入力欄を作る
    # 2. 送信されてきた入力内容を受け取る(値の検証や、型をPython用に変換してくれる)

    # テンプレートファイルに、辞書を渡して、メール本文の文字列を作成している
    subject = '題名'
    mail_text_template = get_template('contacts/email/corporate_message.txt')
    context = {
        'form': form,
    }
    # mail_textには、メールの本文が文字列で作られた状態
    mail_text = mail_text_template.render(context)

    # メールの送信処理
    for user in CustomUser.objects.all():  # モデル名.objects.all()
        if user.is_received_email:
            # 実際にメールを送る。Userモデルに定義されている、メール送信用のメソッド
            user.email_user(subject, mail_text, 'info@a.com')

    # generic.CreateViewのform_validメソッドよぶ
    # form.save(保存処理のこと)と、リダイレクト処理をしている
    return super().form_valid(form)