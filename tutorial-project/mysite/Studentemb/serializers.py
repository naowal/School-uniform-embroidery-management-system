from . import models

from rest_framework import serializers


class StudentEmbInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentEmbInfo
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'firstname', 
            'lastname', 
            'schoolname', 
            'moreinfo', 
            'status', 
            'color', 
            'create_by', 
            'price_baht', 
        )


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.user
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


