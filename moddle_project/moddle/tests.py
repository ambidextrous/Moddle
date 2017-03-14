from django.test import TestCase

from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

from rango.models import *

class MediaTests(TestCase):
    def test_jpg_file_present(self):
        """
		Tests to ensure that a media file has been correctly loaded by the population
        script
		"""
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('media/bikes/boringSteve/bicycle-1834265_1280.jpg')
        self.assertIsNotNone(result)

class IndexPageTests(TestCase):
    def test_index_contains_welcome_message(self):
        # Check if index page includes the word 'Welcome'
        response = self.client.get(reverse('index'))
        self.assertIn(b'Welcome', response.content)		
		

	
