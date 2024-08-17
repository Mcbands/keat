from django.contrib import admin
from .models import Course, Enrollment



class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    prepopulated_fields = {"slug": ("title",)}

# admin.site.register(library)
admin.site.register(Course)
admin.site.register(Enrollment)
# admin.site.register(Module, ModuleAdmin)
