from .. import views
from ..forms import SignupForm

from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

#登陆测试
class SignUpTests(TestCase):
    #初始化测试的响应
    def setUp(self):
        url = reverse('accounts:signup')
        self.response = self.client.get(url)

    #是否成功获取页面
    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    #页面是否由正确的视图处理
    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEquals(view.func, views.signup)

    #表单是否包含csrf_token字段
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    #页面是否有SignupForm
    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignupForm)

    #页面组件是否完整
    def test_contains_forms_input(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="password"', 2)
        self.assertContains(self.response, 'type="email"', 1)

class SuccessfulSignupTests(TestCase):
    def setUp(self):
        url = reverse('accounts:signup')
        data = {
            'username': 'smallfat',
            'email': '123456789@qq.com',
            'password1': 'jmw123456',
            'password2': 'jmw123456'
        }
        self.response = self.client.post(url, data)
        # print(self.response.status_code)
        self.home_url = reverse('home')

    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignupTests(TestCase):
    def setUp(self):
        url = reverse('accounts:signup')
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())



