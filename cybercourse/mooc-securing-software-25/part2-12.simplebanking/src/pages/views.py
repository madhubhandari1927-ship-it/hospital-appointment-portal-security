from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Account


@login_required
def homePageView(request):
    accounts = Account.objects.filter(owner=request.user)
    return render(request, 'pages/index.html', {'accounts': accounts})


@login_required
def addView(request):
    if request.method == 'POST':
        iban = request.POST.get('iban')

        if iban:
            Account.objects.create(
                owner=request.user,
                iban=iban
            )

    return redirect('/')