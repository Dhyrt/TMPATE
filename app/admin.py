from django.contrib import admin
from .forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin  as BaseUserAdmin
from .models import AdultoMayor, Discapacidad, Instructor, Administrador, Taller, Sala, Curso, Materiales, Inscripcion

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form =  UserCreationForm

    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'rut_usuario','first_name','s_nombre', 'last_name', 's_apellido', 'email','password')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )

    search_fields =  ('username', 'email')
    ordering = ('username','email')

    filter_horizontal = ()

admin.site.register(AdultoMayor)
admin.site.register(Discapacidad)
admin.site.register(Instructor)
admin.site.register(Administrador)
admin.site.register(Taller)
admin.site.register(Sala)
admin.site.register(Curso)
admin.site.register(Materiales)
admin.site.register(Inscripcion)