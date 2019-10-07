from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .views import home, board_topics, new_topic
from .forms import NewTopicForm

#主页测试
class HomeTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolve_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


#交流贴界面测试
class BoardTopicsTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('boards:board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        # hompage_url = reverse('home')
        new_topic_url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url).encode('utf8'))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))


class NewTopicTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        self.user = User.objects.create(username='smallfat', email='smallfat@qq.com', password='123456')

    def test_new_topic_view_success_status_code(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk + 1 })
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resloves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topic_view(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        board_topics_url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

    def test_csrf(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')
                                      # 'csrfmiddlewaretoken'

    def test_new_topic_valid_post_data(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        data = {
            'subject': 'Test title',
            'message': 'Some meesage for test.'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_topic_invalid_post_data_empty_fileds(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())

    def test_cotains_form(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)





