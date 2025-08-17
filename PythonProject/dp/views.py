from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Prefetch
from .models import Employee, AchievementEmployee
from .forms import EmployeeForm, AchievementEmployeeFormSet
import logging

# Set up logging
logger = logging.getLogger(__name__)

@login_required
def employee_list(request):
    employees = (
        Employee.objects
        .select_related('department')
        .prefetch_related(
            Prefetch('achievement_links', queryset=AchievementEmployee.objects.select_related('achievement'))
        )
        .order_by('name')
    )
    return render(request, 'dp/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        formset = AchievementEmployeeFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            employee = form.save()
            formset.instance = employee
            formset.save()
            return redirect('employee_list')
        else:
            logger.error(f"Form errors: {form.errors}")
            logger.error(f"Formset errors: {formset.errors}")
    else:
        form = EmployeeForm()
        formset = AchievementEmployeeFormSet()
    return render(request, 'dp/employee_form.html', {'form': form, 'formset': formset, 'create': True})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        formset = AchievementEmployeeFormSet(request.POST, instance=employee)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
        formset = AchievementEmployeeFormSet(instance=employee)
    return render(request, 'dp/employee_form.html', {'form': form, 'formset': formset, 'create': False})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'dp/employee_confirm_delete.html', {'employee': employee})