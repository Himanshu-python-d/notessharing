from django.contrib import admin
from .models import Category , Image
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = ['id','title','category']

@admin.register(Image)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Image
        fields = ['id','title','description','image','added_date','cat']
