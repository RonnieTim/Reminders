from rest_framework.serializers import ModelSerializer

from .models import Reminder


class ReminderSerializer(ModelSerializer):
    """Reminder model serializer."""

    class Meta:
        model = Reminder
        fields = (
            "id",
            "name",
            "description",
            "completed",
            "created",
            "modified",
        )

        read_only_fields = (
            "id",
            "created",
            "date",
        )
