from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class InsideDefault(Page):
    content_rich_1 = RichTextField(blank=True)
    content_rich_2 = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content_rich_1'),
        FieldPanel('content_rich_2')
    ]
