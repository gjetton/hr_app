# hr_app/hr/tasks.py
from celery import shared_task  # Add this import
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from .models import EmploymentApplication, Signature, ApplicantDocument, EmployeeForm, TrainingRecord, HazardReport, Profile
from PIL import Image
import os
import logging

logger = logging.getLogger(__name__)

@shared_task
def purge_unused_tokens():
    now = timezone.now()
    deleted_count, _ = SubmissionToken.objects.filter(
        models.Q(expires_at__lt=now) | models.Q(is_used=True)
    ).delete()
    print(f"Purged {deleted_count} unused or expired tokens on {now}")
    return deleted_count

@shared_task
def send_application_email(app_id, pdf_type):
    app = EmploymentApplication.objects.get(id=app_id)
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', f"{pdf_type}_application_{app_id}.pdf")
    subject = f"New Application: {app.user.username} ({pdf_type})"
    body = f"Application submitted by {app.user.username} on {app.submitted_at}."
    email = EmailMessage(
        subject, body, settings.DEFAULT_FROM_EMAIL, settings.STAFF_EMAILS
    )
    if os.path.exists(pdf_path):
        email.attach_file(pdf_path)
    else:
        print(f"PDF not found: {pdf_path}")
    email.send()
    print(f"Email sent for {pdf_type} PDF, app ID: {app_id}")

@shared_task
def resize_image(image_path):
    """Resize a single image if width > 800px."""
    try:
        with Image.open(image_path) as img:
            if img.size[0] > 800:
                new_height = int(800 * img.size[1] / img.size[0])
                img = img.resize((800, new_height), Image.Resampling.LANCZOS)
                img.save(image_path, quality=85)
                logger.info(f"Resized image: {image_path}")
            else:
                logger.info(f"Image {image_path} already within size limits")
    except Exception as e:
        logger.error(f"Error resizing image {image_path}: {e}")

@shared_task
def resize_images():
    """Batch resize all images across models."""
    print("Starting resize_images task")
    for model, field in [
        (Signature, 'signature_image'),
        (ApplicantDocument, 'document'),
        (EmployeeForm, 'document'),
        (HazardReport, 'photo'),
        (Profile, 'picture'),
    ]:
        for obj in model.objects.all():
            if getattr(obj, field) and (
                field != 'document' or obj.document.name.lower().endswith(('.png', '.jpg', '.jpeg'))
            ):
                img_path = getattr(obj, field).path
                resize_image(img_path)
    print("Finished resize_images task")

@shared_task
def check_training_expirations():
    today = datetime.now().date()
    reminder_date = today + timedelta(days=30)
    expiring_trainings = TrainingRecord.objects.filter(
        renewal_date__lte=reminder_date,
        renewal_date__gte=today
    )
    if expiring_trainings:
        subject = "Training Expiration Reminders"
        body = "The following trainings are nearing expiration:\n\n"
        for training in expiring_trainings:
            days_left = (training.renewal_date - today).days
            body += f"- {training.training_type} for {training.user.username}: Expires {training.renewal_date} ({days_left} days left)\n"
        body += "\nPlease review on the staff dashboard."
        email = EmailMessage(
            subject, body, settings.DEFAULT_FROM_EMAIL, settings.STAFF_EMAILS
        )
        email.send()
        print(f"Sent training expiration reminders for {expiring_trainings.count()} trainings")