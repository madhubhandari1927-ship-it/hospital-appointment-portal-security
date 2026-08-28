from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account


@login_required
def transferView(request):
    if request.method == 'POST':
        to = User.objects.get(username=request.POST.get('to'))
        amount = int(request.POST.get('amount'))

        sender = Account.objects.get(user=request.user)
        receiver = Account.objects.get(user=to)

        with transaction.atomic():
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()

    return redirect('/')


@login_required
def homePageView(request):
    accounts = Account.objects.exclude(user_id=request.user.id)
    return render(request, 'pages/index.html', {'accounts': accounts})