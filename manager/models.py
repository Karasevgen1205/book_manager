from json import loads, dumps
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg
from slugify import slugify


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', help_text='ну это типа имя книги')
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(max_length=1000, null=True, verbose_name='Описание')
    authors = models.ManyToManyField(User, related_name="books")
    rate = models.DecimalField(decimal_places=2, max_digits=3, default=0.0)
    count_rated_users = models.PositiveIntegerField(default=0)
    count_all_stars = models.PositiveIntegerField(default=0)
    users_like = models.ManyToManyField(User, through="manager.LikeBookUser", related_name="liked_books")
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return f"{self.title}{self.slug:}"

    def save(self, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.title)
        try:
            super().save(**kwargs)
        except:
            self.slug += str(self.date)
            super().save(**kwargs)


class LikeBookUser(models.Model):
    class Meta:
        unique_together = ("user", "book")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_book_table")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="liked_user_table", null=True)
    rate = models.PositiveIntegerField(default=5)

    def save(self, **kwargs):
        try:
            super().save(**kwargs)
        except:
            lbu = LikeBookUser.objects.get(user=self.user, book=self.book)
            self.book.count_all_stars -= lbu.rate
            lbu.rate = self.rate
            lbu.save()
        else:
            self.book.count_rated_users += 1
        self.book.count_all_stars += self.rate
        self.book.rate = self.book.count_all_stars / self.book.count_rated_users
        self.book.save()


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    likes_com = models.ManyToManyField(User, through="manager.LikeComment", related_name="liked_comments")


class LikeComment(models.Model):
    class Meta:
        unique_together = ("user", "comment") #взаимоуникальные поля
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_comment_table")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="liked_comm_user_table")

    def save(self, **kwargs):
        try:
            super().save(**kwargs)
        except:
            LikeComment.objects.get(user=self.user, comment=self.comment).delete()
            self.comment.likes -= 1
        else:
            self.comment.likes += 1
        self.comment.save()


class AccountUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="git_hub")
    github_account = models.CharField(null=True, max_length=100)
    _github_repos = models.TextField(null=True)

    @property
    def github_repos(self):
        if self._github_repos is not None:
            return loads(self._github_repos)
        return []

    @github_repos.setter
    def github_repos(self, value):
        assert isinstance(value, list), "you can set list only"
        self._github_repos = dumps(value)