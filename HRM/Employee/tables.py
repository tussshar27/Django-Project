from django_tables2 import tables, TemplateColumn
from .models import Reimbursement,Leave,Meeting,Attendance

class EmployeeReimbursementTable(tables.Table):
    class Meta:
        model = Reimbursement
        attrs = {'class': 'table table-sm','id':'employeeReimbursementTable','width':'100%','cellspacing':'0'}
        fields = ['reimbursement_type', 'title', 'description', 'total_amount', 'file_1','file_2','file_3','date_of_reimbursement','date_of_application','approval']

class ManagerReimbursementApprovalTable(tables.Table):
    class Meta:
        model = Reimbursement
        attrs = {'class': 'table table-sm','id':'managerReimbursementTable','width':'100%','cellspacing':'0'}
        fields = ['user','reimbursement_type', 'title', 'description', 'total_amount', 'file_1','file_2','file_3','date_of_reimbursement','date_of_application','approval']
    
    approve = TemplateColumn(template_name='table_templates/approve_reimbursement_button.html')

class EmployeeLeaveTable(tables.Table):
    class Meta:
        model = Leave
        attrs = {'class': 'table table-sm','id':'employeeLeaveTable','width':'100%','cellspacing':'0'}
        fields = ['leave_type', 'title', 'description', 'date_of_leave','time_of_leave','approval']

class ManagerLeaveApprovalTable(tables.Table):
    class Meta:
        model = Meeting
        attrs = {'class': 'table table-sm','id':'managerApproveLeaveTable','width':'100%','cellspacing':'0'}
        fields = ['user','leave_type', 'title', 'description', 'date_of_leave','time_of_leave','approval']
    
    approve = TemplateColumn(template_name='table_templates/approve_leaves_button.html')
    

class EmployeeMeetingTable(tables.Table):
    class Meta:
        model = Meeting
        attrs = {'class': 'table table-sm','id':'employeeMeetingTable','width':'100%','cellspacing':'0'}
        fields = ['title','description','date_of_meeting', 'time_start', 'time_end', 'approval']

class ManagerMeetingApprovalTable(tables.Table):
    class Meta:
        model = Meeting
        attrs = {'class': 'table table-sm','id':'managerApproveMeetingTable','width':'100%','cellspacing':'0'}
        fields = ['user','title','description','date_of_meeting', 'time_start', 'time_end', 'approval']
    
    approve = TemplateColumn(template_name='table_templates/approve_meetings_button.html')


class EmployeeAttendanceTable(tables.Table):
    class Meta:
        model = Attendance
        attrs = {'class': 'table table-sm','id':'employeeAttendanceTable','width':'100%','cellspacing':'0'}
        fields = ['today_date','start_time', 'end_time']