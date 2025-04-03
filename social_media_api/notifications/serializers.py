from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer


class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)
    actor = UserSerializer(read_only=True)
    target_type = serializers.SerializerMethodField()
    target_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            "id",
            "recipient",
            "actor",
            "verb",
            "target_type",
            "target_id",
            "created_at",
            "read",
        ]
        read_only_fields = ["id", "created_at"]

    def get_target_type(self, obj):
        if obj.content_type:
            return obj.content_type.model
        return None

    def get_target_id(self, obj):
        return obj.object_id
