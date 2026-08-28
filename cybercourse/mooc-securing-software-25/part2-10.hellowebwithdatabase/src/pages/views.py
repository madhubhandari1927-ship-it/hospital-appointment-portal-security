from django.http import HttpResponse
from .models import Message


def homePageView(request):
    message_id = request.GET.get('id')

    message = Message.objects.get(pk=message_id)

    return HttpResponse(message.content)