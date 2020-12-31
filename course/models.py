from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    # @property
    # def get_absolute_url(self):
    #     return reverse('posts:listCategories')


class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(Category, default=1, on_delete=models.PROTECT)
    thumbnail = models.URLField(help_text='image url from unsplash/pexels')
    published_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Enrollments'
