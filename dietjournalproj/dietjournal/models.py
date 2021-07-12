from django.db import models
from users.models import User
from django.utils import timezone

class LogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    bedtime = models.DateTimeField(default=timezone.now)
    waketime = models.DateTimeField(default=timezone.now)
    sleep_quality = models.TextField(default='')
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.date_created + '_' + self.user


class Meal(models.Model):
    meal_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    meal_num = models.IntegerField()
    food = models.CharField(max_length=200)
    drink = models.CharField(max_length=200)
    mood = models.CharField(max_length=200)
    notes = models.TextField()
    day_time = models.DateTimeField(default=timezone.now)
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_type
        

class WaterConsumed(models.Model):
    h2o_oz = models.IntegerField()
    day_time = models.DateTimeField(default=timezone.now)
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.h2o_oz


class Medication(models.Model):
    name = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    dosage = models.CharField(max_length=200)
    reaction = models.TextField()
    day_time = models.DateTimeField(default=timezone.now)
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '_' + self.dosage


class BowelMovement(models.Model):
    bm_num = models.IntegerField()
    notes = models.TextField()
    day_time = models.DateTimeField(default=timezone.now)
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.bm_num

