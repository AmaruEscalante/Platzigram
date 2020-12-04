"""post admin classes."""
from django.contrib import admin


# Register your models here.
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    list_display = ('pk', 'user', 'title', 'photo', 'created')
    list_display_links = ('pk','user')
    list_editable = ('title', 'photo')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title',
    )

    readonly_fields = ('created', 'modified', 'user')


