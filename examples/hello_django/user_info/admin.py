from django.contrib import admin

from .models import Dep, Person


# @admin.register(Dep, Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'dep')
    fields = ('name', 'age', 'dep')


admin.site.register(Dep)
admin.site.register(Person, PersonAdmin)
