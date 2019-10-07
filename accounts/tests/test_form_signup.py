from django.test import TestCase
from ..forms import SignupForm

class SignupFormTest(TestCase):
    def setUp(self):
        self.form = SignupForm()
    def test_form_has_fields(self):
        expected = ['username', 'email', 'password1', 'password2']
        self.assertSequenceEqual(list(self.form.fields), expected)
