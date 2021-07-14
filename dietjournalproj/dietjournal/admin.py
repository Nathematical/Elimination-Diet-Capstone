from django.contrib import admin
from .models import LogEntry, Meal, Water, Medication, BowelMovement, Note

admin.site.register(LogEntry)
admin.site.register(Meal)
admin.site.register(Water)
admin.site.register(Medication)
admin.site.register(BowelMovement)
admin.site.register(Note)
