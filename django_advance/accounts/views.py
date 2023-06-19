from django.views import generic
from django.urls import reverse_lazy
from .forms import MyUserCreationForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

class AccountCreateView(generic.CreateView):
    Model = CustomUser  # カスタムユーザーにする
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')

from django.contrib.auth.views import LoginView, LogoutView
class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    # next_page = '/accounts/login/'
    # ログアウト後に、移動するページ
    next_page = reverse_lazy('accounts:login')


class Home(generic.TemplateView):
    template_name = 'accounts/home.html'

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/home.html'