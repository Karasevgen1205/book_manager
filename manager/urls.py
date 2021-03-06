from django.urls import path
from manager.oauth_views import complete_github_view, complete_github_callback
from manager.views import MyPage, AddCommentLike, BookDetail, AddRate2Book, AddBook, LoginView, \
    logout_user, AddComment, book_delete, UpdateBook, comment_delete, UpdateComment,  RegisterView
from django.conf import settings
from django.conf.urls.static import static
from manager.views_ajax import DeleteComment, AddLikeComment, CreateBook, CreateToken

urlpatterns = [
    path('add_like_comment/<int:id>', AddCommentLike.as_view(), name="add-like-comment"),
    path('add_like_comment/<int:id>/<str:location>/', AddCommentLike.as_view(), name="add-like-comment-location"),
    path("add_rate_to_book/<str:slug>/<int:rate>/", AddRate2Book.as_view(), name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/", AddRate2Book.as_view(), name="add-rate-location"),
    path("book_view_detail/<str:slug>/", BookDetail.as_view(), name="book-detail"),
    path("add_book/", AddBook.as_view(), name="add-book"),
    path("add_comment/<str:slug>/", AddComment.as_view(), name="add-comment"),
    path("delete_book/<str:slug>/", book_delete, name="delete-book"),
    path("update_book/<str:slug>/", UpdateBook.as_view(), name="update-book"),
    path("delete_comment/<int:id>/", comment_delete, name="delete-comment"),
    path("update_comment/<int:id>/", UpdateComment.as_view(), name="update-comment"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", RegisterView.as_view(), name='register'),
    path("complete/", complete_github_view, name='complete_github'),
    path("complete/github/", complete_github_callback, name="complete_callback"),
    path("complete/", complete_github_view, name='complete_github'),
    path("AddLikeComment/<int:pk>", AddLikeComment.as_view()),
    path("delete_comment_ajax/<int:pk>", DeleteComment.as_view()),
    #path("delete_book_ajax/", delete_book),
    path("create_book_ajax/", CreateBook.as_view()),
    #path("create_token/", CreateToken.as_viwe()),
    path("", MyPage.as_view(), name="the-main-page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


