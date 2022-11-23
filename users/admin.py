# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #columnas que se verán en la lista de usuarios
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # nos lleva al detalle
    list_display_links = ('pk', 'user')
    # campos editable desde las listas
    list_editable = ('phone_number', 'website', 'picture')
    # elementos de busqueda
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone_number','user_username')
    # Filtros
    list_filter = ('created', 'updated', 'user__is_active', 'user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'updated'),),
        })
    )

    readonly_fields = ('created', 'updated',)

    ''' unificando formularios admin profile'''

class ProfileInline(admin.StackedInline):
    ''' Profile in-line admin for users.'''
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    '''Add profile admin to base user admin.'''
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.
#admin.site.register(Profile)
