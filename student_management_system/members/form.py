from django import forms
from .models import* 

class staff_nptel(forms.ModelForm):
    
    certificate_type = (('None', 'None'), ('Silver','Silver')('Elite','Elite'),('Gold','Gold'))
    certificate = forms.CharField(choices = certificate_type, widget=forms.RadioSelect)
    
    class Meta:
        models = Nptel
        field = "__all__"
        labels = {
            "Name" : "",
            "nptel_course": "nptel_course",
            "nptel_session_start": "nptel_session_start",
            "nptel_session_end" : "nptel_session_end",
            "percentage": "percentage",
            "upload_certificate": "upload_certificate"
            
            
            
        }
    