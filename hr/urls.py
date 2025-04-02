# hr_app/hr/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('apply/', views.apply, name='apply'),
    path('sign/', views.sign_application, name='sign'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff-dashboard/employee/<int:user_id>/', views.employee_detail, name='employee_detail'),
    path('view-pdf-basic/<int:app_id>/', views.view_application_pdf_basic, name='view_pdf_basic'),
    path('view-pdf-complete/<int:app_id>/', views.view_application_pdf_complete, name='view_pdf_complete'),
    path('update-application/', views.update_application, name='update_application'),
    path('upload-document/', views.user_upload_document, name='user_upload_document'),
    path('report-hazard/', views.report_hazard, name='report_hazard'),
    path('login/', views.custom_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('suggest/', views.suggest, name='suggest'),
    path('timeclock/', views.timeclock, name='timeclock'),
    path('staff-dashboard/timeclock-report/', views.timeclock_report, name='timeclock_report'),
    path('timeclock-report/export-csv/', views.export_timeclock_csv, name='export_timeclock_csv'),
    path('upload-picture/', views.upload_picture, name='upload_picture'),
    path('third-party-submit/<uuid:token>/', views.third_party_submit, name='third_party_submit'),
    path('staff-dashboard/manage-crews/', views.manage_crews, name='manage_crews'),
    path('staff-dashboard/bulk-renew-training/', views.bulk_renew_training, name='bulk_renew_training'),
    path('staff-dashboard/performance/', views.performance_dashboard, name='performance_dashboard'),
    path('staff-dashboard/hazard-report/<int:hazard_id>/', views.hazard_report_detail, name='hazard_report_detail'),
    path('staff-dashboard/suggestion/<int:suggestion_id>/', views.suggestion_detail, name='suggestion_detail'),
    path('staff-message/', views.staff_message, name='staff_message'),
    path('perdiem-list/', views.perdiem_list, name='perdiem_list'),
    path('auto-list/', views.auto_list, name='auto_list'),
    path('training-dashboard/', views.training_dashboard, name='training_dashboard'),
    path('training-management/', views.training_management, name='training_management'),
    path('bulk-renew-training/', views.bulk_renew_training, name='bulk_renew_training'),
    path('timeclock-report/', views.timeclock_report, name='timeclock_report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)