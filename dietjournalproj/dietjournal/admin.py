from django.contrib import admin
from .models import LogEntry, Meal, WaterConsumed, Medication, BowelMovement

admin.site.register(LogEntry)
admin.site.register(Meal)
admin.site.register(WaterConsumed)
admin.site.register(Medication)
admin.site.register(BowelMovement)
