from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser
from .models import Articles, Comments

class ArticleNotLoggedIn(TestCase):

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

    def test_artikelen_not_logged_in(self):
        response = self.client.get(reverse('artikels'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/artikels/')

    def test_profile_not_logged_in(self):
        response = self.client.get(reverse('comments'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/comments/')

class ArticleLoggedIn(TestCase):

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
        self.client.login(username="testuser", password="secret")

    def test_add_article(self):
        post = self.client.post(reverse("artikelaanmaken"), {
            'title':'artikel titel',
            'text':'Dit is een artikel',
        })
        self.assertEquals(post.status_code, 302)
        response = self.client.get('/artikel/1/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Dit is een artikel')

    def test_update_article(self):
        user = CustomUser.objects.get(username="testuser")
        article = Articles.objects.create(author=user, title='The Catcher in the Rye', text='The one who catches')
        post = self.client.post(reverse('artikelbewerken', kwargs={'pk': article.id}), {
            'title':'The Catcher',
            'text':'The one who catches',
        })
        self.assertEquals(post.status_code, 302)
        article.refresh_from_db()
        self.assertEqual(article.title, 'The Catcher')

    def test_delete_article(self):
        user = CustomUser.objects.get(username="testuser")
        article = Articles.objects.create(author=user, title='The Catcher in the Rye', text='The one who catches')
        response = self.client.get(reverse('artikeldetail', kwargs={'pk': article.id}))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'The one who catches')
        post = self.client.post(reverse('artikelverwijderen', kwargs={'pk': article.id}), {})
        self.assertEquals(post.status_code, 302)
        response = self.client.get(reverse('artikeldetail', kwargs={'pk': article.id}))
        self.assertEquals(response.status_code, 404)

    def test_update_comment(self):
        user = CustomUser.objects.get(username="testuser")
        article = Articles.objects.create(author=user, title='The Catcher in the Rye', text='The one who catches')
        comment = Comments.objects.create(article=article, author="James", email="test@hotmail.com", comment="Dit is een test comment")
        post = self.client.post(reverse('commentbewerken', kwargs={'pk': comment.id}), {
            'author':'Johan',
            'email':'test@hotmail.com',
            'comment':'Dit is een test comment',
        })
        self.assertEquals(post.status_code, 302)
        comment.refresh_from_db()
        self.assertEqual(comment.author, 'Johan')