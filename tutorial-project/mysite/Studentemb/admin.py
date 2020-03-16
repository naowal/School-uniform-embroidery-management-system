from django.contrib import admin
from django import forms
from .models import StudentEmbInfo, user

class StudentEmbInfoAdminForm(forms.ModelForm):

    class Meta:
        model = StudentEmbInfo
        fields = '__all__'


class StudentEmbInfoAdmin(admin.ModelAdmin):
    form = StudentEmbInfoAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'firstname', 'lastname', 'schoolname', 'moreinfo', 'status', 'color', 'create_by', 'price_baht']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'firstname', 'lastname', 'schoolname', 'moreinfo', 'status', 'color', 'create_by', 'price_baht']

admin.site.register(StudentEmbInfo, StudentEmbInfoAdmin)


class userAdminForm(forms.ModelForm):

    class Meta:
        model = user
        fields = '__all__'


class userAdmin(admin.ModelAdmin):
    form = userAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(user, userAdmin)


