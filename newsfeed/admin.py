from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Comment)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'likes', 'deleted')
    search_fields = ('caption', 'user__username')

    def get_queryset(self, request):
        return Blog.admin_objects.get_queryset()  # Use the default manager to include all entries
