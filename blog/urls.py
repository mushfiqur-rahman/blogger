from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("<slug:post>/", views.post_single, name='post_single'),
    path("tag/<slug:tag>/", views.TagListView.as_view(), name='post_by_tag')
]
