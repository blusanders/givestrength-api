from django.contrib import admin
from .models import Person
from .models import PersonType
from .models import Day
from .models import Availability

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ['user', 'on_call', 'zip']
admin.site.register(Person, PersonAdmin)


admin.site.register(PersonType)
admin.site.register(Day)
admin.site.register(Availability)