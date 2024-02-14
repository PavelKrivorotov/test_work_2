from django.shortcuts import render


def index(request):
    menu_name = request.GET.get('menu')
    try:
        menu_item = int(request.GET.get('item'))
    except Exception:
        menu_item = None

    context = {
        'title': 'Okey - 1',
        'menu_name': menu_name,
        'menu_item': menu_item
    }

    return render(request, 'menu/menu.html', context=context)

