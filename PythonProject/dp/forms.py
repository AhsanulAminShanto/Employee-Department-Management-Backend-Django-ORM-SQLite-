from django import forms
from django.forms import inlineformset_factory
from .models import Employee, AchievementEmployee, Department, Achievement

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone', 'address', 'department')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.all()

class AchievementEmployeeForm(forms.ModelForm):
    class Meta:
        model = AchievementEmployee
        fields = ('achievement', 'achievement_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['achievement'].queryset = Achievement.objects.all()

AchievementEmployeeFormSet = inlineformset_factory(
    parent_model=Employee,
    model=AchievementEmployee,
    form=AchievementEmployeeForm,
    fields=('achievement', 'achievement_date'),
    extra=1,
    can_delete=True
)