from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RawHTMLBlock
from wagtail.search import index


class InsideDefault(Page):
    content_rich_1 = RichTextField(verbose_name='Sidebar List', blank=True)
    content_rich_2 = RichTextField(verbose_name='Sidebar Content', blank=True)
    image_banner = models.ImageField(verbose_name='Page Banner', upload_to='images/', blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
    ], use_json_field=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('image_banner'),
        FieldPanel('body'),
        FieldPanel('content_rich_1'),
        FieldPanel('content_rich_2'),
    ]
