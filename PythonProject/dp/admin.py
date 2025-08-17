from django.contrib import admin

# Register your models here.
# dp/admin.py
from django.contrib import admin
from .models import Department, Achievement, Employee, AchievementEmployee

class AchievementEmployeeInline(admin.TabularInline):
    model = AchievementEmployee
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    search_fields = ('name', 'email')
    list_filter = ('department',)
    inlines = [AchievementEmployeeInline]

admin.site.register(Department)
admin.site.register(Achievement)
