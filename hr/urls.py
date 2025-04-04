# hr_app/hr/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='custom_login'),
    path('', views.home, name='home'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('timeclock/', views.timeclock, name='timeclock'),
    path('timeclock-report/', views.timeclock_report, name='timeclock_report'),
    path('export-timeclock-csv/', views.export_timeclock_csv, name='export_timeclock_csv'),
    path('training-management/', views.training_management, name='training_management'),
    path('manage-crews/', views.manage_crews, name='manage_crews'),
    path('employee-detail/<int:user_id>/', views.employee_detail, name='employee_detail'),
    path('third-party-submit/<str:token>/', views.third_party_submit, name='third_party_submit'),
    path('staff-message/', views.staff_message, name='staff_message'),
    path('update-application/', views.update_application, name='update_application'),
    path('apply/', views.apply, name='apply'),
    path('sign-application/', views.sign_application, name='sign_application'),  # Fixed route
    path('report-hazard/', views.report_hazard, name='report_hazard'),
    path('hazard-report-detail/<int:hazard_id>/', views.hazard_report_detail, name='hazard_report_detail'),
    path('suggest/', views.suggest, name='suggest'),
    path('suggestion-detail/<int:suggestion_id>/', views.suggestion_detail, name='suggestion_detail'),
    path('upload-picture/', views.upload_picture, name='upload_picture'),
    path('view-application-pdf-basic/<int:app_id>/', views.view_application_pdf_basic, name='view_application_pdf_basic'),
    path('view-application-pdf-complete/<int:app_id>/', views.view_application_pdf_complete, name='view_application_pdf_complete'),
    path('bulk-renew-training/', views.bulk_renew_training, name='bulk_renew_training'),
    path('training-dashboard/', views.training_dashboard, name='training_dashboard'),
    path('performance-dashboard/', views.performance_dashboard, name='performance_dashboard'),
    path('user-upload-document/', views.user_upload_document, name='user_upload_document'),
    path('perdiems/', views.manage_perdiems, name='manage_perdiems'),
    path('auto-expenses/', views.manage_auto_expenses, name='manage_auto_expenses'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)