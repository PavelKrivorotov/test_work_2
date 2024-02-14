from django.contrib import admin

from menu.models import MenuItem, MenuRelation


class AdminMenuItem(admin.ModelAdmin):
    pass

class AdminMenuRelations(admin.ModelAdmin):
    pass


admin.site.register(MenuItem, AdminMenuItem)
admin.site.register(MenuRelation, AdminMenuRelations)
