from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    parent = models.ForeignKey("ArticleCategory",null=True,blank=True,on_delete=models.CASCADE ,verbose_name="دسته بندی")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=200,unique=True, verbose_name="عنوان  دسته بندی در url")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")

class Article_mainTable(models.Model):
    article_category = models.ForeignKey("ArticleCategory", on_delete=models.CASCADE)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=400, allow_unicode=True, db_index=True, verbose_name="عنوان در url")
    image = models.ImageField(upload_to="images/articles", verbose_name="تصویر مقاله")
    short_description = models.TextField(verbose_name="توضحیات مختصر")
    text = models.TextField(verbose_name="توضیحات مقاله")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")
    selected_categories = models.ManyToManyField(to="ArticleCategory", verbose_name="دسته بندی های مقاله", through="Article_mainTable")

