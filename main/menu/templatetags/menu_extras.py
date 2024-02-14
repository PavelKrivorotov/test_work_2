from django import template

from menu.templatetags.manager import MenuManager


register = template.Library()

@register.inclusion_tag('draw-menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = context.get('menu_name')
    item = context.get('menu_item')

    manager = MenuManager(menu_name, item)

    if menu == menu_name:
        items = manager.open()
    else:
        items = manager.show()


    return {
        'menu': items,
        'menu_name': menu_name,
        'menu_item': item
    }

