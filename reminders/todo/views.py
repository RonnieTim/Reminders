from rest_framework.viewsets import ModelViewSet

from .models import Reminder
from .serializers import ReminderSerializer


class ReminderViewSet(ModelViewSet):
    """Reminder View Set."""

    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
