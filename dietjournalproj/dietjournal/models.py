from django.db import models
from users.models import User

class LogEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_created + '_' + self.user

class Meal(models.Model):
    location = models.CharField(max_length=200)
    meal_num = models.IntegerField()
    food_name = models.CharField(max_length=200)
    day_time = models.DateTimeField(auto_now=True)
    bowel_movement = models.IntegerField()
    mood = models.CharField(max_length=200)
    notes = models.TextField()
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_num + '_' + self.food_name

class Snack(models.Model):
    location = models.CharField(max_length=200)
    snack_num = models.IntegerField()
    food_name = models.CharField(max_length=200)
    day_time = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.snack_num + '_' + self.food_name

class Sleep(models.Model):
    bedtime = models.DateTimeField()
    waketime = models.DateTimeField()
    sleep_quality = models.TextField()
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.bedtime + '_' + self.waketime
    
class WaterConsumed(models.Model):
    h2o_oz = models.IntegerField()
    log_entry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.h2o_oz

class Medication(models.Model):
    name = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    dosage = models.CharField(max_length=200)
    date_started = models.DateTimeField(auto_now=True)
    reaction = models.TextField()

    def __str__(self):
        return self.dosage + '_' + self.name
