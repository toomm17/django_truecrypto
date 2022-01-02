from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название категории')
    image = models.ImageField(upload_to='categories/', verbose_name='Фотография', blank=True)
    slug = models.SlugField(unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название теги')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    slug = models.SlugField(default=slugify(title), verbose_name='Ссылка')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='artilces/', verbose_name='Фотографи для превью')
    article_image = models.ImageField(upload_to='artilces/', verbose_name='Фото в статье', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_news = models.BooleanField(default=False, verbose_name='Это новость?')
    tag = models.ManyToManyField(Tag, related_name='article_tag', verbose_name='Теги')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        verbose_name='Категория',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Описание события')
    date = models.DateTimeField(auto_now=False, verbose_name='Дата')
    tag = models.ManyToManyField(Tag, related_name='event_tag', verbose_name='Теги')
    slug = models.SlugField(verbose_name='Ссылка', null=True)
    deadline = models.DateTimeField(auto_now=False, verbose_name='Событие длится до', null=True, blank=True)
    have_kyc = models.BooleanField(default=False, verbose_name='Есть у события KYC?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календарь'
