from django.utils.html import format_html
from wagtail.images.formats import Format, register_image_format


class CaptionedImageFormat(Format):

    def image_to_html(self, image, alt_text, extra_attributes=None):

        default_html = super().image_to_html(image, alt_text, extra_attributes)

        return format_html("{}<figcaption>{}</figcaption>", default_html, alt_text)


class NoAlignImageFormat(Format):

    def image_to_html(self, image, alt_text, extra_attributes=None):

        default_html = super().image_to_html(image, alt_text, extra_attributes)

        return format_html("{}", default_html, alt_text)


register_image_format(
    CaptionedImageFormat('captioned_fullwidth', 'Full width captioned', 'richtext-image full-width-captioned', 'width-800')
)

register_image_format(
    NoAlignImageFormat('noalign', 'No Alignment', 'richtext-image non-aligned', 'original')
)
