from django.contrib import admin
from .models import Enseignant, Cours


class EnseignantAdmin(admin.ModelAdmin):
    list_display = ("nom", "specialite")
    search_fields = ("nom", "specialite")
    list_filter = ("nom",)


class CoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "credit", "enseignant")
    search_fields = ("titre",)
    list_filter = ("credit", "enseignant")




admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Cours, CoursAdmin)