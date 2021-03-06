from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, BaseForm, ModelMultipleChoiceField
from manager.models import Book, Comment
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'autofocus': True, "class": "form-control"}))
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password', "class": "form-control"}),
    )


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control", "rows": 5, "cols": 50})
        }
        help_texts = {
            "title": "",
            "text": ""
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": Textarea(attrs={"class": "form-control", "rows": 5, "cols": 50})
        }
        help_texts = {
            "text": ""
        }
        #book_id = ModelMultipleChoiceField(queryset=Book.objects.all())