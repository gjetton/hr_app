# hr_app/hr/admin.py
from django.contrib import admin
from .models import Profile, EmploymentApplication, Signature, Certification, EmployeeCertification, Jobsite

# Define admin classes first
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_months')
    search_fields = ('name',)

class EmployeeCertificationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'certification', 'completion_date', 'expiration_date', 'is_valid')
    list_filter = ('certification', 'completion_date')
    search_fields = ('employee__username', 'certification__name')

class JobsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'site_specific_training')
    filter_horizontal = ('required_certifications',)
    search_fields = ('name', 'location')

# Register models with admin
admin.site.register(Profile)
admin.site.register(EmploymentApplication)
admin.site.register(Signature)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(EmployeeCertification, EmployeeCertificationAdmin)
admin.site.register(Jobsite, JobsiteAdmin)