import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __sty__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timezone(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.TextField('Текст комментария', max_length=200)

    def __sty__(self):
        return self.author_name

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timezone(days=7))

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Comment4comment(models.Model):
    article = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.TextField('Текст комментария', max_length= 200)

    def __sty__(self):
        return self.author_name