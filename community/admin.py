from django.contrib import admin
from .models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'updated_at',]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
