import factory
from django.contrib.auth.models import User
from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.StubFactory(UserFactory)
    content = "x"
    status = "published"
