""" add new class to admin panel """
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


class MyFlatPageAdmin(FlatPageAdmin):
    """ define new class"""
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

    list_display = ('url', 'title', 'registration_required')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)
