import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestListByTag:
    def test_tag_url(self, client, post_factory):
        post_factory(title='test-post', tags=['test-tag'])
        url = reverse('post_by_tag', kwargs={'tag': 'test-tag'})
        response = client.get(url)
        assert response.status_code == 200

    def test_tag_htmx_fragment(self, client, post_factory):
        post_factory(title='test-post', tags=['test-tag'])
        headers = {'HTTP_HX-Request': 'True'}
        url = reverse('post_by_tag', kwargs={'tag': 'test-tag'})
        response = client.get(url, **headers)
        assertTemplateUsed(response, 'components/post-list-elements-tags.html')

    def test_tag_filter(self, client, post_factory):
        x = post_factory(title='test-post', tags=['test-tag'])
        url = reverse('post_by_tag', kwargs={'tag': 'test-tag'})
        response = client.get(url)
        assert x.tags.all()[0].name == response.context['tag']
        # grabbing the tags associated to this post here (x = ...) that should match to response context tags
