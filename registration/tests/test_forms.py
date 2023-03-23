from django.test import TestCase
from registration.models import Registration, Complaint, Appointment
from registration.forms import LoginForm, RegistrationForm, ContactForm, ComplaintForm, AppointmentForm


class FormTests(TestCase):

    def test_login_form(self):
        form_data = {'user_name': 'testuser', 'password': 'password12'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_registration_form(self):
        form_data = {'full_name': 'John Doe', 'phone_number': '1234567890', 'id_number': 'ABC123'}
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_contact_form(self):
        form_data = {'name': 'John Doe', 'message': 'This is a test message.'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_complaint_form(self):
        form_data = {'name': 'John Doe', 'appointment_type': 'passport', 'description': 'This is a test complaint.'}
        form = ComplaintForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_appointment_form(self):
        form_data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'date': '2023-03-22', 'time': '12:00:00', 'location': '123 Main St.'}
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())


