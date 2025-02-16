from django.db import models

# Create your models here.
# https://azinkin.ru/orm.html

class Category(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    reaction = models.IntegerField(choices=[(1, 'Лайк'), (-1, 'Дизлайк')])

    def __str__(self):
        return f"Like on {self.post.title}"

    class Meta:
        verbose_name = "лайк"
        verbose_name_plural = "лайки"

class Donation(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to='donations/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "донат"
        verbose_name_plural = "донаты"
