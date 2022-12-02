from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Enseignant
# Register your models here.
admin.site.unregister(Group)

class EmployeAdmin(admin.ModelAdmin):
    readonly_fields = ('user_account', 'nom', 'post_nom', 'pre_nom', 'genre', 'phone_number', 'email')
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=any):
        return False
    
admin.site.register(Enseignant, EmployeAdmin)