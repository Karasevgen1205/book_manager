from django.http import HttpResponse
from manager.models import LikeComment


def add_like2comment(request):
    if request.user.is_authenticated:
        LikeComment.objects.create(user=request.user, comment_id=request.GET.get('comment_id'))
    return HttpResponse("OK")