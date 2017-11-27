
from django.test import TestCase
from .models import Contactlist

class ModelTestCase(TestCase):
    """This class defines the test suite for the contactlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.contactlist_name = "Write world class code"
        self.contactlist = Contactlist(name=self.contactlist_name)

    def test_model_can_create_a_contactlist(self):
        """Test the contactlist model can create a contactlist."""
        old_count = Contactlist.objects.count()
        self.contactlist.save()
        new_count = Contactlist.objects.count()
        self.assertNotEqual(old_count, new_count)
