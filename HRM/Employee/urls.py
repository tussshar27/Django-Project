from django.contrib import admin
from django.urls import path
from .views import loginView,dashboardView,logout_request,profileView,forgotpasswordView,reimbursementView,leaveView,meetingView,approveMeetingView,approveMeetingUpdate,approveLeaveView,approveLeaveUpdate,approveReimbursementView,approveReimbursementUpdate,applySalaryView

urlpatterns = [
    path('', loginView, name='login'),
    path('forgot-password', forgotpasswordView, name='forgotpassword'),
    path('dashboard', dashboardView, name='dashboard'),
    path('reimbursement', reimbursementView,name='reimbursement'),
    path('leave',leaveView,name='leave'),
    path('meeting',meetingView,name='meeting'),
    path('approveReimbursement',approveReimbursementView,name='approveReimbursement'),
    path('approveReimbursement/<int:pk>/', approveReimbursementUpdate.as_view(), name='approveReimbursementUpdate'),
    path('approveLeave',approveLeaveView,name='approveLeave'),
    path('approveLeave/<int:pk>/', approveLeaveUpdate.as_view(), name='approveLeaveUpdate'),
    path('approveMeeting',approveMeetingView,name='approveMeeting'),
    path('approveMeeting/<int:pk>/', approveMeetingUpdate.as_view(), name='approveMeetingUpdate'),
    path('profile', profileView, name='profile'),
    path('logout', logout_request, name='logout'),
    path('applysalary',applySalaryView,name='applysalary')
    
]

app_name = "Employee"