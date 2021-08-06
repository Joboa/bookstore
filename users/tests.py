from django.urls.base import resolve
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .views import SignupPageView
from users.forms import CustomUserCreationForm


class CustomUserTests(TestCase):

  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(
        username='boamah',
        email='boamah@joboadevs.com',
        password='OneDayIWllBeAProfessionalDeveloper'
        )

    self.assertEqual(user.username, 'boamah')
    self.assertEqual(user.email, 'boamah@joboadevs.com')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)


  def test_create_superuser(self):
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@joboadevs.com',
        password='ItsWell'
        )

    self.assertEqual(admin_user.username, 'superadmin')
    self.assertEqual(admin_user.email, 'superadmin@joboadevs.com')
    self.assertTrue(admin_user.is_active)
    self.assertTrue(admin_user.is_staff)
    self.assertTrue(admin_user.is_superuser)

  
class SignUpPageTests(TestCase):

  def setUp(self):
    url = reverse('signup')
    self.response = self.client.get(url)

  def test_signup_template(self):
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'signup.html')
    self.assertContains(self.response, 'Sign Up')
    self.assertNotContains(self.response, 'Weirdo!, going django pro!')

  def test_signup_form(self):
    form = self.response.context.get('form')
    self.assertIsInstance(form, CustomUserCreationForm)
    self.assertContains(self.response, 'csrfmiddlewaretoken')
  
  def test_signup_view(self):
    view = resolve('/accounts/signup/')
    self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
  