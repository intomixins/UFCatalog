from django.contrib import admin

from my_site.models import Fighter, Styles


class FighterAdmin(admin.ModelAdmin):
    """ админка для бойца """
    model = Fighter
    list_display = ('name', 'last_name', 'record', 'is_retired', 'style',)


class StylesAdmin(admin.ModelAdmin):
    """ админка для стилей бойца """
    model = Styles
    list_display = ('name',)


admin.site.register(Fighter, FighterAdmin)
admin.site.register(Styles, StylesAdmin)
