from django.test import TestCase

# Create your tests here.


#### TESTING VIEWS ####

from django.urls import reverse

class SimpleViewTests(TestCase):
    def test_landing_view_status_code(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)

    def test_landing_view_template_used(self):
        response = self.client.get(reverse('landing'))
        self.assertTemplateUsed(response, 'landing.html')

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template_used(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact.html')



# TODO run sign_in test
# if get --> should 200 and render sign-in.html
# if post --> check if the form is valid --> assert True AND redirect to dashboard
# post --> invalid inputs --> assert False (different versions for: email, password, both) AND redirect to sign-in.html

#TODO ADD LATER --> check if google recaptcha is working
