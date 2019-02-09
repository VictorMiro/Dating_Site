from django.contrib import admin

from profileOF.models import Profile, CategoryOFUSER, CityOFUSER


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')
    search_fields = ('bio', 'city')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CategoryOFUSER)
admin.site.register(CityOFUSER)

