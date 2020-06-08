from django.test import TestCase, Client
from django.urls import reverse

from .models import CustomUser
from .forms import CustomAuthenticationForm, MakeCustomUserForm 

class UserTests(TestCase):

    def setUp(self):
        self.client = Client()
        testuser = CustomUser.objects.create_user(
            username='testuser',
            email='user@example.org',
            first_name='Jan',
            last_name='Hooi',
            password='secret',
        )
        testuser.save()
    
    def test_register_page(self):
        response = self.client.get('/registreren/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')
        self.assertIsInstance(response.context['form'], MakeCustomUserForm)

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertIsInstance(response.context['form'], CustomAuthenticationForm)

    def test_profile_not_logged_in(self):
        response = self.client.get(reverse('profielbewerken'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/profielbewerken/')

    def test_registration_form(self):
        response = self.client.post(reverse("register"), {
            'username':'treeuser',
            'password1':'django12345',
            'password2':'django12345',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/')
        self.assertEqual(CustomUser.objects.count(), 2)
        
    def test_login_form(self):
        response = self.client.post(reverse('login'), {
            'username':'testuser',
            'password':'secret',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        response = self.client.get('/')
        self.assertEquals(str(response.context['user']), 'testuser')
        self.assertTemplateUsed(response, 'home.html')
