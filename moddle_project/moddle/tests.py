from django.test import TestCase

from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

from moddle.models import *
from moddle.forms import *

class IndexPageTests(TestCase):
    def test_index_contains_welcome_message(self):
        # Check if index page includes the word 'Welcome'
        response = self.client.get(reverse('index'))
        self.assertIn(b'Welcome', response.content)		

class TemplatesWorkingTests(TestCase):
    def test_contact_us_using_template(self):
        response = self.client.get(reverse('contact_us'))
        # Check template used to render contact_us page
        self.assertTemplateUsed(response, 'moddle/contact_us.html')		
	
class GraphicsDisplayTests(TestCase):		
    def test_logo_displayed(self):
        response = self.client.get(reverse('about'))
        # Check if logo displayed on about page
        self.assertIn('/static/images/logo-256.png'.lower(), response.content.lower())			

class CSRFTokenTests(TestCase):		
    def test_csrf_token_displayed(self):
        response = self.client.get(reverse('register'))
        # Check check if CSRF middleware token displayed on registration page
        self.assertIn('csrfmiddlewaretoken'.lower(), response.content.lower())	

class ButtonTests(TestCase):		
    def test_summit_button_displayed(self):
        response = self.client.get(reverse('register'))
        # Check check if submission button displayed on registration page
        self.assertIn('name="submit"'.lower(), response.content.lower())		

class BikeCategorySelectionTests(TestCase):		
    def test_bike_selection_available(self):
        response = self.client.get(reverse('index'))
        # Check if 'mountainbike' option available on index page 
        self.assertIn('mountainbike'.lower(), response.content.lower())	
