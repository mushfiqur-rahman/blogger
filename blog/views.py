from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
#    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "components/post-list-elements.html"
        return "blog/index.html"
