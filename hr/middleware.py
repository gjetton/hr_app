# hr_app/hr/middleware.py
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now()
            timeout = 2700  # 45 minutes in seconds

            if last_activity:
                last_activity = timezone.datetime.fromisoformat(last_activity)
                if (now - last_activity).total_seconds() > timeout:
                    logger.info(f"Auto-logging out user {request.user.username} due to inactivity")
                    logout(request)
                    return redirect('login')

            # Update last activity timestamp
            request.session['last_activity'] = now.isoformat()

        response = self.get_response(request)
        return response