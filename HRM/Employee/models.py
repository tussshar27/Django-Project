from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class ApprovalChoice(models.TextChoices):
    accept='accept','accept'
    pending='pending','pending'
    rejected='rejected','rejected'

class Department(models.Model):
    departmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentName
    

class Employee(models.Model):
    class DesignationChoice(models.TextChoices):
        Employee = 'EMP','Employee'
        Manager = 'MGR','Manager'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(max_length=300)
    emailId = models.EmailField(max_length=150)
    phoneNo = PhoneNumberField(null=False, blank=False, unique=True)
    designation = models.CharField( max_length=50, choices=DesignationChoice.choices,default=DesignationChoice.Employee)
    date_of_joining = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()
    profile_image = models.ImageField(upload_to='profile_images/', max_length=100, null=True, blank=True)
    managers= models.ManyToManyField('Employee',limit_choices_to={'designation': 'MGR'})
    base_salary= models.DecimalField(max_digits=10, decimal_places=2,default="3000")

    def __str__(self):
        return self.first_name

class Reimbursement(models.Model):
    class ReimbursementChoice(models.TextChoices):
        TravelingA = 'TravellingA','Travelling Allowance'
        SpecialA = 'SpecialA','Special Allowance'
        MedicalA= 'MedicalA','Medical Allowance'
        BusinessA= 'BusinessA','Business Allowance'
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    reimbursement_type= models.CharField( max_length=50, choices=ReimbursementChoice.choices,default=ReimbursementChoice.TravelingA)
    title=models.CharField(max_length=150)
    description=models.TextField(max_length=300,blank=True,null=True)
    total_amount=models.DecimalField(max_digits=6, decimal_places=2)
    file_1=models.FileField(upload_to='reimbursements/%Y/%m/%d',blank=True,null=True)
    file_2=models.FileField(upload_to='reimbursements/%Y/%m/%d',blank=True,null=True)
    file_3=models.FileField(upload_to='reimbursements/%Y/%m/%d',blank=True,null=True)
    date_of_reimbursement= models.DateField()
    date_of_application=models.DateField(auto_now=True) 
    approval=models.CharField( max_length=50, choices=ApprovalChoice.choices,default=ApprovalChoice.pending)
    included_in_salary=models.BooleanField(default=False) 

    def __str__(self):
        return self.title


class Leave(models.Model):
    class LeaveChoice(models.TextChoices):
        FullDay = 'FullDay','Full Day'
        HalfDay = 'HalfDay','Half Day'
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type= models.CharField( max_length=50, choices=LeaveChoice.choices,default=LeaveChoice.FullDay)
    title=models.CharField(max_length=150)
    description=models.TextField(max_length=300,blank=True,null=True)
    date_of_leave= models.DateField()
    time_of_leave=models.TimeField(blank=True,null=True)
    approval=models.CharField( max_length=50, choices=ApprovalChoice.choices,default=ApprovalChoice.pending)
    included_in_salary=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Meeting(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField(max_length=300,blank=True,null=True)
    date_of_meeting= models.DateField()
    time_start=models.TimeField(blank=True,null=True)
    time_end=models.TimeField(blank=True,null=True)
    approval=models.CharField( max_length=50, choices=ApprovalChoice.choices,default=ApprovalChoice.pending)
    included_in_salary=models.BooleanField(default=False)

    def __str__(self):
        return self.title

#AAdesh

class Attendance(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    today_date = models.DateField(default=timezone.now())
    start_time = models.TimeField(default=None,blank=True, null=True)
    end_time = models.TimeField(default=None,blank=True, null=True)
    def __str__(self):
        return self.user

class Salary(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    basic_salary=models.DecimalField(max_digits=6,decimal_places=2)
    leaves_taken=models.IntegerField(default=0)
    deducted_salary=models.DecimalField(max_digits=6,decimal_places=2)
    reimbursement=models.DecimalField(max_digits=6,decimal_places=2)
    total_salary=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.user



#Signals