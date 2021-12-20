from django.contrib import admin

from browsersPc.models import PC, Browsers


class PCAdmin(admin.ModelAdmin):
    pass


class BrowsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(PC, PCAdmin)
admin.site.register(Browsers, BrowsersAdmin)