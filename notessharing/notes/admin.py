from django.contrib import admin
from .models import Signup, Notes
# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    class Meta:
        model = Signup
        fields = '__all__'

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    class Meta:
        model = Notes
        fields = '__all__'
