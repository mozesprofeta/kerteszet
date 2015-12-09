from django.contrib import admin
from .models import Before, After


# Register your models here.

class BeforeAdmin(admin.ModelAdmin):
    actions = ['really_delete_selected']

    def get_actions(self, request):
        actions = super(BeforeAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 image was"
        else:
            message_bit = "%s images were" % queryset.count()

        self.message_user(request, "%s sucessfully deleted." % message_bit)

    really_delete_selected.short_description = "Delete selected entries"


admin.site.register(Before, BeforeAdmin)
admin.site.register(After)
