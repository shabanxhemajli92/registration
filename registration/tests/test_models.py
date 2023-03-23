from django.test import TestCase
from registration.models import Registration, Complaint, Appointment


class RegistrationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Registration.objects.create(full_name='John Doe', phone_number=1234567890, id_number='ABC123')

    def test_full_name_label(self):
        registration = Registration.objects.get(id=1)
        field_label = registration._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')

    def test_phone_number_max_length(self):
        registration = Registration.objects.get(id=1)
        max_length = registration._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, None)

    def test_object_name_is_full_name(self):
        registration = Registration.objects.get(id=1)
        expected_object_name = f'{registration.full_name}'
        self.assertEqual(expected_object_name, str(registration))


class ComplaintModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Complaint.objects.create(name='John Doe', appointment_type='passport', description='Test complaint')

    def test_name_label(self):
        complaint = Complaint.objects.get(id=1)
        field_label = complaint._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_appointment_type_choices(self):
        complaint = Complaint.objects.get(id=1)
        choices = complaint._meta.get_field('appointment_type').choices
        self.assertEqual(choices, [('passport', 'Passport'), ('id', 'ID'), ('driverslicence', "Driver's Licence"), ('utilitybill', 'Utility Bill')])

    def test_object_name_is_name_appointment_type(self):
        complaint = Complaint.objects.get(id=1)
        expected_object_name = f'{complaint.name} {complaint.appointment_type}'
        self.assertEqual(expected_object_name, str(complaint))

class AppointmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Appointment.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            date='2023-03-22',
            time='15:30',
            location='123 Main St'
        )

    def test_name_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_email_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_date_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_time_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'time')

    def test_location_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'location')

    def test_object_name_is_name(self):
        appointment = Appointment.objects.get(id=1)
        expected_object_name = f'{appointment.name}'
        self.assertEqual(expected_object_name, str(appointment))