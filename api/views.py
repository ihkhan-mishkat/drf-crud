from rest_framework import generics
from .serializers import ContactlistSerializer
from .models import Contactlist

class CreateView(generics.ListCreateAPIView):
    queryset = Contactlist.objects.all()
    serializer_class = ContactlistSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contactlist.objects.all()
    serializer_class = ContactlistSerializer
