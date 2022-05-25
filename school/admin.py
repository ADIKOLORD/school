from django.contrib import admin
from .models import Category, Accreditation, Chronology, Teacher, File


class FileInlines(admin.TabularInline):
    model = File
    extra = 0


class AccreditationAdmin(admin.ModelAdmin):
    inlines = [FileInlines]


admin.site.register(Category)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(Chronology)
admin.site.register(Teacher)
