import factory
from django.contrib.auth.models import User

from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    # is_stuff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
