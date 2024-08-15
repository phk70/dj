from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    slug = models.SlugField("URL", unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        default=None,
    )
    tags = models.ManyToManyField("Tag", related_name="posts")
    views = models.IntegerField("Просмотров", default=0)
    published_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return str(self.title)

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"


class Category(models.Model):
    name = models.CharField("Категория", max_length=200, unique=True)
    slug = models.SlugField("URL", unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return str(self.name)

    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"


class Tag(models.Model):
    name = models.CharField("Тег", max_length=100, unique=True)
    slug = models.SlugField("URL", unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        self.name = self.name.lower().replace(" ", "_")
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return str(self.name)

    def get_absolute_url(self):
        return f"/blog/tag/{self.slug}/"


class Comment(models.Model):
    STATUS_CHOICES = [
        ("checked", "Проверен"),
        ("unchecked", "Не проверен"),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField("Текст")
    status = models.CharField(
        "Статус", max_length=10, choices=STATUS_CHOICES, default="unchecked"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self, *args, **kwargs):
        return str(self.text)
