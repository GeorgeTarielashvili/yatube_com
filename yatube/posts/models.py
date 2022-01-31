from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='groups',
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        db_table = 'Posts'
        pass


class Group(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание группы')

    class Meta:
        app_label = 'posts'
        db_table = 'Groups'
        pass

    def __str__(self):
        return self.title
