from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RawHTMLBlock
from taggit.models import Tag as TaggitTag
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class BlogIndexPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = BlogPage.objects.live().public().order_by('-date')
        paginator = Paginator(all_posts, 12)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts

        return context

    content_rich_1 = RichTextField(verbose_name='Sidebar List', blank=True)
    content_rich_2 = RichTextField(verbose_name='Sidebar Content', blank=True)
    image_banner = models.ImageField(verbose_name='Page Banner', upload_to='images/', blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('image_banner'),
        FieldPanel('body'),
        FieldPanel('content_rich_1'),
        FieldPanel('content_rich_2'),
    ]


class BlogPage(RoutablePageMixin, Page):
    date = models.DateField("Post date")
    content_rich_1 = RichTextField(verbose_name='Sidebar List', blank=True)
    content_rich_2 = RichTextField(verbose_name='Sidebar Content', blank=True)
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
    ], use_json_field=True, blank=True)
    home_featured = models.BooleanField(default=False, verbose_name='Home Featured')
    tags = ClusterTaggableManager(through="blog.BlogPageTag", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('featured_image'),
        FieldPanel('body'),
        FieldPanel('content_rich_1'),
        FieldPanel('content_rich_2'),
        FieldPanel('home_featured'),
        InlinePanel('categories', label='Category', heading='Blog Category'),
        FieldPanel('tags'),
    ]


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True


class BlogPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.BlogPage", on_delete=models.CASCADE, related_name="categories"
    )
    blog_category = models.ForeignKey(
        "blog.BlogCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey("BlogPage", on_delete=models.CASCADE, related_name="post_tags")

