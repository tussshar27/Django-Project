from django.forms import ModelForm
from .models import Reimbursement,Leave,Meeting
from django import forms


class ReimbursementForm(ModelForm):
    class Meta:
        model = Reimbursement
        fields = ['user','reimbursement_type', 'title', 'description', 'total_amount','file_1','file_2','file_3','date_of_reimbursement','approval','included_in_salary']
        widgets = {'user':forms.HiddenInput(),'included_in_salary':forms.HiddenInput(), 'approval':forms.HiddenInput()}

class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = ['user','leave_type', 'title', 'description', 'date_of_leave','time_of_leave','approval']
        widgets = {'user':forms.HiddenInput(),'included_in_salary':forms.HiddenInput(), 'approval':forms.HiddenInput()}

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['user','title','description','date_of_meeting', 'time_start', 'time_end', 'approval','included_in_salary','approval']
        widgets = {'user':forms.HiddenInput(),'included_in_salary':forms.HiddenInput(), 'approval':forms.HiddenInput()}

class MeetingUpdateForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['user','title','description','date_of_meeting', 'time_start', 'time_end', 'approval','included_in_salary','approval']
        widgets = {'user':forms.TextInput(attrs={'disabled': True}),
        'title':forms.TextInput(attrs={'disabled': True}),
        'description':forms.Textarea(attrs={'disabled': True}),
        'time_start':forms.TextInput(attrs={'disabled': True}),
        'time_end':forms.TextInput(attrs={'disabled': True}),
        'included_in_salary':forms.HiddenInput(),
        'date_of_meeting':forms.TextInput(attrs={'disabled': True}),

        }