import telepot
from django.db import models

from Novac.settings import BOT_TOKEN


class SiteIcon(models.Model):
    image = models.ImageField(upload_to='media/icons/')
    link = models.URLField(blank=True)  # Поле для ссылки на внешний сайт


# Create your models here.
class Header(models.Model):
    company_name = models.TextField(null=True, max_length=50)
    descriptions = models.TextField(null=True, max_length=50)
    phone_number = models.CharField(max_length=15)
    icons = models.ManyToManyField(SiteIcon, related_name='header_icons', blank=True)

    class Meta:
        verbose_name_plural = 'Хедер'


class Footer(models.Model):
    company_name = models.TextField(null=True, max_length=50)
    user_agreement = models.FileField(upload_to='user_agreements/', null=True, blank=True)
    company_description = models.TextField(null=True, max_length=250)
    icons = models.ManyToManyField(SiteIcon, related_name='footer_icons', blank=True)
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Футер'


class IconMain(models.Model):
    header_logo = models.URLField(null=True)
    page_data = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='icon_slide')

    class Meta:
        verbose_name_plural = 'Иконки'


class Slide(models.Model):
    title = models.CharField(max_length=255, null=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    slide_order = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Слайды'

    def get_products(self):
        # Получить все товары для этого слайда
        return Product.objects.filter(slide=self)

class Card(models.Model):
    slide = models.ForeignKey(Slide, related_name='cards_blocks', on_delete=models.CASCADE)
    text = models.TextField(null=True, max_length=450)
    description = models.TextField(null=True, max_length=450, blank=True)
    image = models.ImageField(upload_to='media/images', null=True)

    class Meta:
        verbose_name_plural = 'Карточки'


class TextBlock(models.Model):
    slide = models.ForeignKey(Slide, related_name='text_blocks', on_delete=models.CASCADE)
    text = models.TextField(null=True, max_length=450)
    description = models.TextField(null=True, max_length=450, blank=True)

    class Meta:
        verbose_name_plural = 'Текст'


class Product(models.Model):
    image = models.ImageField(upload_to='media/product', null=True, verbose_name="Фотография")
    NameProduct = models.CharField(null=False, max_length=15, verbose_name="Название товара")

    class Meta:
        verbose_name_plural = 'Товар'


class Photo(models.Model):
    slide = models.ForeignKey(Slide, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images', null=True)

    class Meta:
        verbose_name_plural = 'Фотографии'


# Создайте экземпляр бота
bot = telepot.Bot(BOT_TOKEN)


class FeedbackPost(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15)  # Предполагаем, что номер телефона - строка

    # def send_telegram_message(self):
    #     message_text = f'Пришла новая заявка!\nИмя: {self.name}\nТелефон: {self.phone_number}'
    #     chat_id = '680617843'
    #     bot.sendMessage(chat_id, message_text)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.send_telegram_message()

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = 'Заявки'
