from django.contrib import admin

from .models import Cat, Feeding

# Register your models here.

# 
# class CatAdmin(admin.ModelAdmin):
#     list_display = ('name', 'breed', 'description', 'age')
#     list_display_links = ('name',)
#     list_filter = ('breed',)
#     search_fields = ('name', 'breed')
#     ordering = ('name',)
#     # list_editable = ('breed',)
#     # list_editable = ('description',)
#     # list_editable = ('age',)
#     # list_editable = ('breed', 'description', 'age')
#     # list_editable = ('breed', 'description', 'age')
#     # list_editable = ('breed', 'description', 'age')
#     # list_editable = ('breed', 'description', 'age')

admin.site.register( Cat)
admin.site.register(Feeding)