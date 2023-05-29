from django.urls import path
import view
urlpatterns = [
    path('v1/calendar/init/', view.GoogleCalendarInitView, name='google_permission'),
    path('v1/calendar/redirect/', view.GoogleCalendarRedirectView, name='google_redirect')
]
