from django.contrib import admin
from .models import PersonalInfo


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    list_editable = ('first_name', 'last_name', 'email')

    def has_add_permission(self, request):
        count = PersonalInfo.objects.all().count()

        if count == 0:
            return True
        return False
