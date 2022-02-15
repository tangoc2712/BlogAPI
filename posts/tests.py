from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create user
        testUser1 = User.objects.create_user(username='tangoc', password='1')
        testUser1.save()

        # create blog post
        test_post = Post.objects.create(author=testUser1, title='First News',
                                        body='Today, cases of covid 19 in Vietnam has descrease, at all has 1000 cases.')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        print(type(post.author), author)

        self.assertEqual(author, 'tangoc')
        self.assertEqual(title, 'First News')
        self.assertEqual(
            body, 'Today, cases of covid 19 in Vietnam has descrease, at all has 1000 cases.')
