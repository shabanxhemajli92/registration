from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .models import Registration


class TestLoginView(TestCase):
    def test_login_page_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

class TestHomeView(TestCase):
    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'registration/home.html')


class TestAboutView(TestCase):
    def test_about_page_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'registration/about.html')


class TestRegistrationView(TestCase):
    def test_registration_page_uses_correct_template(self):
        response = self.client.get(reverse('registration'))
        self.assertTemplateUsed(response, 'registration/registration_form.html')

    def test_successful_registration_creates_new_user(self):
        self.client.post(reverse('registration'), {'full_name': 'John Doe', 'phone_number': '1234567890', 'id_number': 'ABC123'})
        self.assertTrue(Registration.objects.filter(full_name='John Doe').exists())

    def test_successful_registration_redirects_to_registration_list_page(self):
        response = self.client.post(reverse('registration'), {'full_name': 'John Doe', 'phone_number': '1234567890', 'id_number': 'ABC123'})
        self.assertRedirects(response, reverse('registration_list'))


class TestRegistrationListView(TestCase):
    def test_registration_list_page_uses_correct_template(self):
        response = self.client.get(reverse('registration_list'))
        self.assertTemplateUsed(response, 'registration/registered.html')


class TestContactView(TestCase):
    def test_contact_page_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'registration/contact.html')

    def test_successful_contact_submission_sends_email(self):
        self.client.post(reverse('contact'), {'name': 'John Doe', 'message': 'Test message'})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New contact message from John Doe')
        self.assertEqual(mail.outbox[0].body, 'John Doe sent a message:\n\nTest message')

