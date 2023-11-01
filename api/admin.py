from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail
from .models import Slide, TextBlock, Photo, Header, Footer, SiteIcon, Card, Product
from PIL import Image


# @admin.register(Slide)
# class SlideAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slide_order')
#     search_fields = ('title',)

class TextBlockInline(admin.TabularInline):
    model = TextBlock
    extra = 1  # Количество пустых форм для добавления текстовых блоков


class CardBlockInline(admin.TabularInline):
    model = Card
    extra = 1  # Количество пустых форм для добавления текстовых блоков


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Количество пустых форм для добавления фотографий


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('NameProduct', 'image')
    search_fields = ('NameProduct',)


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide_order')
    list_filter = ('slide_order',)
    search_fields = ('title', 'sub_title')
    inlines = [TextBlockInline, PhotoInline, CardBlockInline]


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone_number')
    search_fields = ['company_name']


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user_agreement', 'company_description')
    list_filter = ('company_name',)
    search_fields = ('company_name',)


@admin.register(SiteIcon)
class SiteIconAdmin(admin.ModelAdmin):
    list_display = ('image', 'link')
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="/api/media{obj.image.url}">')
