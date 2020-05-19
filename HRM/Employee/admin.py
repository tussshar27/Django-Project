from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Employee,Department,Reimbursement,Leave,Meeting,Attendance
import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(BaseUserAdmin,ExportCsvMixin):
    inlines = (EmployeeInline,)
    actions = ["export_as_csv"]


class DepartmentAdmin(admin.ModelAdmin,ExportCsvMixin):
    actions = ["export_as_csv"]

class ReimbursementAdmin(admin.ModelAdmin,ExportCsvMixin):
    model= Reimbursement
    actions = ["export_as_csv"]
    list_display = ['user','reimbursement_type', 'title', 'description', 'total_amount', 'file_1','file_2','file_3','date_of_reimbursement','date_of_application','approval']


class LeaveAdmin(admin.ModelAdmin,ExportCsvMixin):
    model= Leave
    actions = ["export_as_csv"]
    list_display = ['user','leave_type', 'title', 'description', 'date_of_leave','time_of_leave','approval']

class MeetingAdmin(admin.ModelAdmin,ExportCsvMixin):
    model= Leave
    actions = ["export_as_csv"]
    list_display = ['user','title','description','date_of_meeting', 'time_start', 'time_end', 'approval']

class AttendanceAdmin(admin.ModelAdmin,ExportCsvMixin):
    model= Leave
    actions = ["export_as_csv"]
    list_display = ['user','today_date','start_time', 'end_time']

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Reimbursement,ReimbursementAdmin)
admin.site.register(Leave,LeaveAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Attendance,AttendanceAdmin)