from time import sleep

import pytest
from ..pages.contact_page import ContactPage


class TestContactPage:
    url = 'https://bluemedia.pl/kontakt'

    @pytest.fixture(scope='class')
    def contact_page(self, browser):
        page = ContactPage(browser, self.url)
        page.open()
        yield page

    def test_elements_of_contact_page(self, contact_page):
        contact_page.should_be_contact_page()
        contact_page.should_be_contact_form_private()
        contact_page.switch_to_corporate_form()
        contact_page.should_be_contact_form_corporate()

    @pytest.mark.parametrize('name_surname, email, phone, topic, description', [
        ('BlueServices Test', 'bs@blueservices.pl', '+48 123 123 123', 'Przelewy natychmiastowe',
         'automat test Blueservices')])
    def test_filling_contact_form(self, contact_page, name_surname, email, phone, topic, description):
        contact_page.should_be_contact_page()
        contact_page.should_be_contact_form_private()
        contact_page.switch_to_corporate_form()
        contact_page.should_be_contact_form_corporate()
        contact_page.send_name_surname(name_surname)
        contact_page.send_email(email)
        contact_page.send_phone(phone)
        contact_page.send_topic(topic)
        contact_page.send_request_description(description)
        contact_page.switch_radio_delivery_answer_email()
        contact_page.check_agreement_personal_data()
        # There is the sleep for checking by human
        sleep(15)
