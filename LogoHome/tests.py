from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Suppliers

def register_new_supplier(no_char, name_char, days):
    """ create new supplier by adding supplier_no, supplier_name as well as days offset to now(negative for past, positive for future) """
    time = timezone.now() + datetime.timedelta(days=days)
    return Suppliers.objects.create(no_char=no_char, name_char=name_char, registration_date=time)

class SupplierIndexViewTest(TestCase):
    def test_no_suppliers(self):
        """ If no suppliers exist, an appropriate message is displayed. """
        response = self.client.get(reverse('LogoHome:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No LogoHome are available.")
        self.assertQuerysetEqual(response.context['latest_suppliers_list'],[])
    
    def test_past_suppliers(self):
        """ Suppliers with a registration_date in the past are displayed on the index page """
        register_new_supplier(no_char="PAST01", name_char="Past supplier", days=-30)
        response = self.client.get(reverse('LogoHome:index'))
        self.assertQuerysetEqual(response.context['latest_suppliers_list'], ['<Suppliers: Suppliers object (6)>'])
        # self.assertQuerysetEqual(response.context['latest_suppliers_list'], ['<Supplier: Past supplier>'])

    def test_future_suppliers(self):
        """ Suppliers with a registration_date in the future are displayed on the index page """
        register_new_supplier(no_char="FUTURE01", name_char="Future supplier", days=30)
        response = self.client.get(reverse('LogoHome:index'))
        self.assertContains(response, "No LogoHome are available.")
        self.assertQuerysetEqual(response.context['latest_suppliers_list'], [])

    def test_future_and_past_suppliers(self):
        register_new_supplier(no_char="PAST02", name_char="Past supplier 02", days=-25)
        register_new_supplier(no_char="FUTURE02", name_char="Future supplier 02", days=25)
        response = self.client.get(reverse('LogoHome:index'))
        self.assertQuerysetEqual(response.context['latest_suppliers_list'],['<Suppliers: Suppliers object (3)>'])

    def test_two_past_suppliers(self):
        """ Multiple suppliers will be displayed on the index page """
        register_new_supplier(no_char="PAST03", name_char="Past supplier 03", days=-30)
        register_new_supplier(no_char="PAST04", name_char="Past supplier 04", days=-25)
        response = self.client.get(reverse('LogoHome:index'))
        self.assertQuerysetEqual(response.context['latest_suppliers_list'],['<Suppliers: Suppliers object (8)>', '<Suppliers: Suppliers object (7)>'])

class SupplierDetailViewTest(TestCase):
    def test_future_suppliers(self):
        """ The detail view of a supplier with a registration_date in the future return 404 not found. """
        future_supplier = register_new_supplier(no_char="DETAILFUTURE01", name_char="Detail future supplier", days=15)
        url = reverse('LogoHome:detail', args=[future_supplier.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_suppliers(self):
        """ The detail view of the supplier who has the registration_date in the past displays the supplier_name. """
        past_supplier = register_new_supplier(no_char="DETAILPAST01", name_char="Detail past supplier", days=-10)
        url = reverse('LogoHome:detail', args=[past_supplier.id])
        response = self.client.get(url)
        self.assertContains(response, past_supplier.name_char)

class SuppliersModelTests(TestCase):
    def test_registrtion_date_with_future_suppliers(self):
        """ registration_inputed return() False for Suppliers whose registration_date is in future."""

        time = timezone.now() + datetime.timedelta(days=30)
        future_suppliers = Suppliers(registration_date = time)
    
        self.assertIs(future_suppliers.registration_inputed(), False)
    
    def test_registration_date_with_old_suppliers(self):
        """ registration_inputed return() False for Supplier whose registration_date is older than 2 day """

        time = timezone.now() - datetime.timedelta(days=2, seconds=1)
        old_suppliers = Suppliers(registration_date = time)

        self.assertIs(old_suppliers.registration_inputed(), False)
    
    def test_registration_date_with_recent_suppliers(self):
        """ registration_inputed return() True for Supplier whose registration_date is within the last day. """

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_suppliers = Suppliers(registration_date = time)

        self.assertIs(recent_suppliers.registration_inputed(), True)
