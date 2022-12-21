from django.db import models

# Create your models here.
from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey("ArticleCategory",null=True,blank=True,on_delete=models.CASCADE ,verbose_name="دسته بندی")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=200,unique=True, verbose_name="عنوان  دسته بندی در url")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")
    is_article = models.BooleanField(default=True, verbose_name="مقاله میباشد")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقالات"
        verbose_name_plural = "دسته بندی های مقالات"

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=400, allow_unicode=True, db_index=True, verbose_name="عنوان در url")
    image = models.ImageField(upload_to="images/articles", verbose_name="تصویر مقاله")
    short_description = models.TextField(verbose_name="توضحیات مختصر")
    text = models.TextField(verbose_name="توضیحات مقاله")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")
    selected_categories = models.ManyToManyField(to="ArticleCategory", verbose_name="دسته بندی های مقاله")
    author = models.ForeignKey(User, verbose_name="نویسنده", null=True, editable=False, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد", editable=False)
    view_count = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
