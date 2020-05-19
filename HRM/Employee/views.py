from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Employee,Reimbursement,Leave,Meeting,Attendance
from .forms import ReimbursementForm,LeaveForm,MeetingForm,MeetingUpdateForm
from .tables import EmployeeReimbursementTable,EmployeeLeaveTable,EmployeeMeetingTable,ManagerMeetingApprovalTable,ManagerLeaveApprovalTable,ManagerReimbursementApprovalTable,EmployeeAttendanceTable
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employee:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'Employee/loginPage.html', context={'form': form})

def forgotpasswordView(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employee:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'Employee/forgotpasswordPage.html', context={'form': form})

@login_required
def logout_request(request):
    logout(request)
    return redirect("employee:login")

@login_required
def reimbursementView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    form=None
    table = EmployeeReimbursementTable(Reimbursement.objects.filter(user=request.user))

    if request.method == 'POST':
        form = ReimbursementForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('employee:reimbursement')
        else:
            print(form.is_valid())
            print(form.errors)
    else:
        form = ReimbursementForm(initial={'user': request.user})

    context = {
        'user_details': user_details,
        'form':form,
        'table':table,
        'notifications':notifications,
        'notification_count':notification_count
    }
    return render(request,'Employee/reimbursementPage.html',context=context)

@login_required
def leaveView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    form=None
    table = EmployeeLeaveTable(Leave.objects.filter(user=request.user))

    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('employee:leave')
        else:
            print(form.is_valid())
            print(form.errors)
    else:
        form = LeaveForm(initial={'user': request.user})

    context = {
        'user_details': user_details,
        'form':form,
        'table':table,
        'notifications':notifications,
        'notification_count':notification_count
    }
    return render(request,'Employee/leavePage.html',context=context)

@login_required
def meetingView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    form=None
    table = EmployeeMeetingTable(Meeting.objects.filter(user=request.user))

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('employee:meeting')
        else:
            print(form.is_valid())
            print(form.errors)
    else:
        form = MeetingForm(initial={'user': request.user})

    context = {
        'user_details': user_details,
        'form':form,
        'table':table,
        'notifications':notifications,
        'notification_count':notification_count
    }
    return render(request,'Employee/meetingPage.html',context=context)

#Manager functionality
@login_required
def approveLeaveView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    employees_under_manager=Employee.objects.filter(managers=Employee.objects.get(user=request.user))
    employee_under_manager_arr=[]
    for employee in employees_under_manager:
        employee_under_manager_arr.append(employee.user)
    print(employee_under_manager_arr)
    table = ManagerLeaveApprovalTable(Leave.objects.filter(user__in=employee_under_manager_arr))

    context = {
        'user_details': user_details,
        'table':table,
        'notifications':notifications,
        'notification_count':notification_count
        
    }
    return render(request,'Employee/approveLeavePage.html',context=context)

class approveLeaveUpdate(UpdateView):
    template_name = 'Employee/approveLeaveFormPage.html'
    model = Leave
    fields = ['approval']
    success_url = reverse_lazy('employee:approveLeave')


@login_required
def approveReimbursementView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    employees_under_manager=Employee.objects.filter(managers=Employee.objects.get(user=request.user))
    employee_under_manager_arr=[]
    for employee in employees_under_manager:
        employee_under_manager_arr.append(employee.user)
    print(employee_under_manager_arr)
    table = ManagerReimbursementApprovalTable(Reimbursement.objects.filter(user__in=employee_under_manager_arr))

    context = {
        'user_details': user_details,
        'table':table,
        'notifications':notifications,
        'notification_count':notification_count
    }
    return render(request,'Employee/approveReimbursementPage.html',context=context)

class approveReimbursementUpdate(UpdateView):
    template_name = 'Employee/approveReimbursementFormPage.html'
    model = Reimbursement
    fields = ['approval']
    success_url = reverse_lazy('employee:approveReimbursement')

@login_required
def approveMeetingView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    employees_under_manager=Employee.objects.filter(managers=Employee.objects.get(user=request.user))
    employee_under_manager_arr=[]
    for employee in employees_under_manager:
        employee_under_manager_arr.append(employee.user)
    print(employee_under_manager_arr)
    table = ManagerMeetingApprovalTable(Meeting.objects.filter(user__in=employee_under_manager_arr))

    context = {
        'user_details': user_details,
        'table':table,
        'notifications':notifications,
        'notification_count':notification_count
    }
    return render(request,'Employee/approveMeetingPage.html',context=context)

class approveMeetingUpdate(UpdateView):
    template_name = 'Employee/approveMeetingFormPage.html'
    model = Meeting
    fields = ['approval']
    success_url = reverse_lazy('employee:approveMeeting')

@login_required
def profileView(request):
    user_details= getUserDetails(request.user)
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()
    context = {
        'user_details': user_details,
        'notifications':notifications,
        'notification_count':notification_count
    }
    return render(request,'Employee/profilePage.html',context=context)

#Other server requests, TODO: handle anonymous user error flow
def handler404(request, exception):
    user_details= None #getUserDetails(request.user)
    context = {
        'user_details': user_details
    }
    response = render(request, "Components/404.html", context=context)
    response.status_code = 404
    return response

def handler500(request):
    user_details= None #getUserDetails(request.user)
    context = {
        'user_details': user_details
    }
    response = render(request, "Components/500.html", context=context)
    response.status_code = 500
    return response


#utility methods
def getUserDetails(user):
    return get_object_or_404(Employee,user=user)

#AAdesh
@login_required
def dashboardView(request):
    user_details= getUserDetails(request.user)
    current_date = timezone.now()
    data = Attendance.objects.filter(user=request.user,today_date=current_date).first()
    table = EmployeeAttendanceTable(Attendance.objects.filter(user=request.user))
    notifications=request.user.notifications.unread()
    notification_count=notifications.count()

    print("Notifications")
    print(notifications)

    warning=None
    startDisableFlag=False
    endDisableFlag=False

    #######Salary calculation
    reimbursements = Reimbursement.objects.filter(user=request.user,approval='accept')
    leaves = Leave.objects.filter(user=request.user,approval='accept')
    total_reimbursement=0
    total_leave=0
    emp_obj=Employee.objects.filter(user=request.user).first()
    base_salary=emp_obj.base_salary

    for reimbursement in reimbursements:
        total_reimbursement+=reimbursement.total_amount

    for leave in leaves:
        if(leave.leave_type=='HalfDay'):
            total_leave+=0.5
        elif (leave.leave_type=='FullDay'):
            total_leave+=1
    
    salary_per_day=base_salary/30
    deductions=total_leave*salary_per_day
    total_days_present=30-total_leave
    total_salary=(salary_per_day*total_days_present)+total_reimbursement

    salary_calculation={
        "salary_per_day":salary_per_day,
        "deductions":deductions,
        "total_days_present":total_days_present,
        "total_salary":total_salary,
        "reimbursement":total_reimbursement
    }
    print(total_leave)
    print(total_reimbursement)
    print(base_salary)
    ######

    if request.method == 'GET':
        click_state=request.GET.get('click',None)#request.query_params.get('click', None)
        #######Salary calculation
        reimbursements = Reimbursement.objects.filter(user=request.user,approval='accept')
        leaves = Leave.objects.filter(user=request.user,approval='accept')
        total_reimbursement=0
        total_leave=0
        emp_obj=Employee.objects.filter(user=request.user).first()
        base_salary=emp_obj.base_salary

        for reimbursement in reimbursements:
            total_reimbursement+=reimbursement.total_amount

        for leave in leaves:
            if(leave.leave_type=='HalfDay'):
                total_leave+=0.5
            elif (leave.leave_type=='FullDay'):
                total_leave+=1
    
        salary_per_day=base_salary/30
        deductions=total_leave*salary_per_day
        total_days_present=30-total_leave
        total_salary=(salary_per_day*total_days_present)+total_reimbursement
        annual_salary=base_salary*12
        salary_calculation={
        "base_salary":base_salary,
        "annual_salary":annual_salary,
        "salary_per_day":salary_per_day,
        "total_leave":total_leave,
        "deductions":deductions,
        "total_days_present":total_days_present,
        "total_salary":total_salary,
        "total_reimbursement":total_reimbursement
        }
        print(total_leave)
        print(total_reimbursement)
        print(base_salary)
        ######

        if click_state=='start':
            if data:
                if data.start_time:
                    startDisableFlag=True
                if data.end_time:
                    endDisableFlag=True

                #######Salary calculation
                reimbursements = Reimbursement.objects.filter(user=request.user,approval='accept')
                leaves = Leave.objects.filter(user=request.user,approval='accept')
                total_reimbursement=0
                total_leave=0
                emp_obj=Employee.objects.filter(user=request.user).first()
                base_salary=emp_obj.base_salary

                for reimbursement in reimbursements:
                    total_reimbursement+=reimbursement.total_amount

                for leave in leaves:
                    if(leave.leave_type=='HalfDay'):
                        total_leave+=0.5
                    elif (leave.leave_type=='FullDay'):
                        total_leave+=1
    
                salary_per_day=base_salary/30
                deductions=total_leave*salary_per_day
                total_days_present=30-total_leave
                total_salary=(salary_per_day*total_days_present)+total_reimbursement

    
                ######

                warning='Session already started!!!'
                context={
                        'user_details':user_details,
                        'startDisableFlag':startDisableFlag,
                        'endDisableFlag':endDisableFlag,
                        'warning':warning,
                        'table':table,
                        'salary_calculation':salary_calculation,
                        'notifications':notifications,
                        'notification_count':notification_count
                        
                    }

                return render(request,'Employee/dashboardPage.html',context=context)

            else:

                Attendance.objects.create(user=request.user,start_time=timezone.localtime(timezone.now()))
                return redirect('employee:dashboard')

        elif click_state=='stop':
            if data:
                if data.end_time:
                    startDisableFlag=True
                    endDisableFlag=True
                    warning="Session already ended for today!!!"
                    context={
                        'user_details':user_details,
                        'startDisableFlag':startDisableFlag,
                        'endDisableFlag':endDisableFlag,
                        'warning':warning,
                        'table':table,
                        'salary_calculation':salary_calculation,
                        'notifications':notifications,
                        'notification_count':notification_count
                    }

                    return render(request,'Employee/dashboardPage.html',context=context)
                else:
                    #data.update(end_time=timezone.localtime(timezone.now()))
                    Attendance.objects.filter(pk=data.pk).update(end_time=timezone.localtime(timezone.now()))
                    return redirect('employee:dashboard')
        else:
            if data:
                if data.start_time:
                    startDisableFlag=True
                if data.end_time:
                    endDisableFlag=True

    context={
        'user_details':user_details,
        'startDisableFlag':startDisableFlag,
        'endDisableFlag':endDisableFlag,
        'warning':warning,
        'table':table,
        'salary_calculation':salary_calculation,
        'notifications':notifications,
        'notification_count':notification_count
    }

    return render(request,'Employee/dashboardPage.html',context=context)


@login_required
def applySalaryView(request):
    user_details= getUserDetails(request.user)
    employees_under_manager=Employee.objects.filter(managers=Employee.objects.get(user=request.user))



    context = {
        'user_details': user_details,
    }
    return render(request,'Employee/applySalaryPage.html',context=context)
