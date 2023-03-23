from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.core import mail
from datetime import date, time
from registration.models import Complaint, Appointment 
from registration.forms import  ContactForm, LoginForm, AppointmentForm

class LoginViewTest(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/home.html')

class AboutViewTest(TestCase):
    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/about.html')



class RegistrationListViewTest(TestCase):
    def test_registration_list_view(self):
        response = self.client.get(reverse('registration_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registered.html')
        self.assertQuerysetEqual(response.context['object_list'], [])

class ContactViewTest(TestCase):
    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_form_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'Hello, this is a test message.'
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New contact message from John Doe')

class ComplaintCreateViewTestCase(TestCase):
    def test_create_complaint(self):
        url = reverse('complaint-list')
        data = {
            'name': 'John Doe',
            'appointment_type': 'passport',
            'description': 'My passport application was rejected.',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Complaint.objects.count(), 1)
        complaint = Complaint.objects.first()
        self.assertEqual(complaint.name, data['name'])
        self.assertEqual(complaint.appointment_type, data['appointment_type'])
        self.assertEqual(complaint.description, data['description'])
        self.assertTrue(timezone.now() - complaint.created_at < timezone.timedelta(seconds=1))

class AppointmentFormViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('appointment_success')

    def test_form_submission(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'date': str(date.today()),
            'time': str(time(10, 30)),
            'location': 'New York City',
        }
        response = self.client.post(self.url, data=data)
        print(response.content)  
        self.assertEqual(response.status_code, 405)
        self.assertEqual(Appointment.objects.count(), 0)
        

    def test_form_validation(self):
        form = AppointmentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('date', form.errors)
        self.assertIn('time', form.errors)
        self.assertIn('location', form.errors)        