from django.shortcuts import render


def homePageView(request):
    items = request.session.get('items', [])

    if request.method == 'POST':
        item = request.POST.get('content', '').strip()

        if item:
            items.append(item)
            request.session['items'] = items

    return render(request, 'pages/index.html', {'items': items})