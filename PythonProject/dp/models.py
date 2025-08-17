from django.db import models

# Create your models here.
# dp/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    achievements = models.ManyToManyField(Achievement, through='AchievementEmployee', related_name='employees', blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class AchievementEmployee(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='achievement_links')
    achievement_date = models.DateField()

    class Meta:
        unique_together = ('achievement', 'employee', 'achievement_date')
        verbose_name = 'Achievement record'
        verbose_name_plural = 'Achievement records'

    def __str__(self):
        return f"{self.employee.name} - {self.achievement.name} on {self.achievement_date}"
