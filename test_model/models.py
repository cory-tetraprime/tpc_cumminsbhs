from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RawHTMLBlock


class TestModel(Page):
    image_banner = models.ImageField(upload_to='images/')
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('image_banner'),
        FieldPanel('body')
    ]
