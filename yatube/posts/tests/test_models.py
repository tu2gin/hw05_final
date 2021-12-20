from django.test import TestCase

from ..models import Comment, Group, Post, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Текст Поста',
        )
        cls.comm = Comment.objects.create(
            post=cls.post,
            author=cls.user,
            text='Тестовая комментарий',
        )

    def test_models_Group_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        act = PostModelTest.group.__str__()
        self.assertEqual(act, 'Тестовая группа', '__str__ модели Group')

    def test_models_Comment_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        act = PostModelTest.comm.__str__()
        self.assertEqual(act, 'Тестовая комментарий', '__str__ модели Comment')

    def test_models_Post_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        act = PostModelTest.post.__str__()
        self.assertEqual(act, 'Текст Поста', '__str__ модели Post')
