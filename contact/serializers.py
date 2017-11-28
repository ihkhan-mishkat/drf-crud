from rest_framework import serializers
from .models import Contactlist

class ContactlistSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Contactlist
        fields = ('id', 'name', 'phone', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
