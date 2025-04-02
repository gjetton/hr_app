# /home/hradmin/hr_app/purge_former_employees.py
import os
import shutil
from datetime import datetime, timedelta
from django.conf import settings
from hr.models import User

BASE_DIR = settings.BASE_DIR
DATA_DIR = os.path.join(BASE_DIR, 'data', 'employees')

def purge_former_employees():
    one_year_ago = datetime.now().date() - timedelta(days=365)
    former_employees = User.objects.filter(
        profile__is_employee=False,
        profile__is_active=False,
        profile__termination_date__lt=one_year_ago  # Updated to use termination_date
    )
    
    for user in former_employees:
        folder = os.path.join(DATA_DIR, user.username)
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Removed {folder}")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hr_app.settings")
    import django
    django.setup()
    purge_former_employees()