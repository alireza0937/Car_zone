from django.contrib import admin
from team.models import Team
from django.utils.html import format_html


@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
    def image(self, object: Team):
        return format_html('<img src="{}" width=40>'.format(object.photo.url))

    list_display = ('id', 'image', 'first_name', 'last_name', 'position')
    search_fields = ('last_name', 'position')
