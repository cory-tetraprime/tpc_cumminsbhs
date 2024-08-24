from django.db import models

from django.apps import apps
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
# from blog.models import BlogPage


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request):
        BlogPage = apps.get_model('blog', 'BlogPage')
        context = super().get_context(request)
        featured_posts = BlogPage.objects.live().filter(home_featured=True).order_by('-date')
        context['featured_posts'] = featured_posts
        return context
