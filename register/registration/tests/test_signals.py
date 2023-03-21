from django.test import TestCase, override_settings
from django.core import mail
from registration.models import Registration

@override_settings(ADMIN_EMAIL='admin@example.com')
class RegistrationSignalTest(TestCase):
    def test_send_registration_email(self):
        registration = Registration.objects.create(full_name='John Doe', phone_number='1234567890', id_number='ABC123')
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, 'New registration created')
        self.assertIn('A new registration has been created', mail.outbox[0].body)
        self.assertIn('Full Name: John Doe', mail.outbox[0].body)
        self.assertIn('Phone Number: 1234567890', mail.outbox[0].body)
        self.assertIn('ID Number: ABC123', mail.outbox[0].body)