from . import models
from . import serializers
from rest_framework import viewsets, permissions


class StudentEmbInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the StudentEmbInfo class"""

    queryset = models.StudentEmbInfo.objects.all()
    serializer_class = serializers.StudentEmbInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class userViewSet(viewsets.ModelViewSet):
    """ViewSet for the user class"""

    queryset = models.user.objects.all()
    serializer_class = serializers.userSerializer
    permission_classes = [permissions.IsAuthenticated]


