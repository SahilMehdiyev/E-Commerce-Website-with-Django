from django.contrib import admin
from .models import Page,Carousel



class PageModify(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'updated_at',
    )
    list_editable = (
        'title',
        'status',
    )
    list_filter = ('status',)
    
admin.site.register(Page,PageModify)


# class CarouselAdmin(admin.ModelAdmin):
admin.site.register(Carousel)
