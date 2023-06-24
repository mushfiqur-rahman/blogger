import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestPostSingle:
    def test_post_single_url(self, client, post_factory):
        post = post_factory()
        url = reverse('post_single', kwargs={'post': post.slug})
        response = client.get(url)
        assert response.status_code == 200
