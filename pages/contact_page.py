import re

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from .locators import ContactLocators


class ContactPage:
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_presents(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_contact_page(self):
        self.should_be_contact_url()
        self.should_contact_title_page()
        self.should_be_contact_header()
        self.should_be_contact_form_private()

    def should_be_contact_url(self):
        pattern = '(/kontakt){1}'
        url = self.browser.current_url
        match_contact_url = re.search(pattern, url)
        assert match_contact_url, 'Page url is not contact url'

    def should_be_contact_header(self):
        header_el = ContactLocators.CONTACT_HEADER
        header = self.is_element_presents(*header_el)
        assert header, 'There is not header'
        header = self.browser.find_element(*header_el).text
        assert header == 'Kontakt', 'Text of header is not correct'

    def should_be_contact_form_private(self):
        self.should_be_radio_type_of_client()
        self.should_be_checked_radio_private_client()
        self.should_be_name_surname_field()
        self.should_be_email_field()
        self.should_be_phone_field()
        self.should_be_dropdown_subject_request()
        self.should_be_request_text_area()
        self.should_be_radio_delivery_answer()
        self.should_be_check_agreement_personal_data()
        self.should_be_check_agreement_receive_email()
        self.should_be_check_agreement_trusted_partners()
        self.should_be_button_send()

    def should_be_contact_form_corporate(self):
        self.should_be_radio_type_of_client()
        self.should_be_checked_radio_corporate_client()
        self.should_be_name_surname_field()
        self.should_be_email_field()
        self.should_be_phone_field()
        self.should_be_company_name_field()
        self.should_be_dropdown_subject_request()
        self.should_be_request_text_area()
        self.should_be_radio_delivery_answer()
        self.should_be_check_agreement_personal_data()
        self.should_be_check_agreement_receive_email()
        self.should_be_check_agreement_trusted_partners()
        self.should_be_button_send()

    def should_be_radio_type_of_client(self):
        assert self.is_element_presents(
            *ContactLocators.RADIO_PRIVATE_CLIENT), 'There is not radio button for private client'
        assert self.is_element_presents(
            *ContactLocators.RADIO_BUSINESS_CLIENT), 'There is not radio button for corporate client'

    def should_be_email_field(self):
        assert self.is_element_presents(*ContactLocators.INPUT_EMAIL), 'There is not input for e-mail'

    def should_be_phone_field(self):
        assert self.is_element_presents(*ContactLocators.INPUT_PHONE), 'There is not input for phone'

    def should_be_request_text_area(self):
        assert self.is_element_presents(
            *ContactLocators.TEXT_AREA_REQUEST), 'There is not text area for describing request'

    def should_be_name_surname_field(self):
        assert self.is_element_presents(*ContactLocators.INPUT_NAME_SURNAME), 'There is not input for Name & Surname'

    def should_be_dropdown_subject_request(self):
        assert self.is_element_presents(
            *ContactLocators.ITEMS_REQUEST_SUBJECTS), 'There is not drop down for subject choosing'

    def should_be_radio_delivery_answer(self):
        assert self.is_element_presents(
            *ContactLocators.RADIO_DELIVERY_ANSWER_EMAIL), 'There is not drop down for answer delivery email'
        assert self.is_element_presents(
            *ContactLocators.RADIO_DELIVERY_ANSWER_POST), 'There is not drop down for answer delivery post'

    def should_be_check_agreement_personal_data(self):
        assert self.is_element_presents(
            *ContactLocators.CHECKBOX_AGREEMENT_PROCESS_PERSONAL_DATA), \
            'There is not checkbox for agreement of personal data'

    def should_be_check_agreement_receive_email(self):
        assert self.is_element_presents(
            *ContactLocators.CHECKBOX_AGREEMENT_RECEIVE_EMAILS), \
            'There is not checkbox for agreement for receiving emails'

    def should_be_check_agreement_trusted_partners(self):
        assert self.is_element_presents(
            *ContactLocators.CHECKBOX_AGREEMENT_TRUSTED_PARTNERS), \
            'There is not checkbox for agreement for give data to trusted partners'

    def should_be_button_send(self):
        assert self.is_element_presents(*ContactLocators.BUTTON_SEND), 'There is not button for sending request'

    def should_be_checked_radio_private_client(self):
        radio_private = self.browser.find_element(*ContactLocators.RADIO_PRIVATE_CLIENT)
        assert radio_private.is_selected(), 'There is not checked private client by default'

    def should_be_checked_radio_corporate_client(self):
        radio_corporate = self.browser.find_element(*ContactLocators.RADIO_BUSINESS_CLIENT)
        assert radio_corporate.is_selected(), 'There is not checked corporate client'

    def switch_to_corporate_form(self):
        self.browser.find_element(*ContactLocators.RADIO_BUSINESS_CLIENT).click()

    def send_name_surname(self, name_surname):
        self.browser.find_element(*ContactLocators.INPUT_NAME_SURNAME).send_keys(name_surname)

    def send_email(self, email):
        self.browser.find_element(*ContactLocators.INPUT_EMAIL).send_keys(email)

    def send_phone(self, phone):
        self.browser.find_element(*ContactLocators.INPUT_PHONE).send_keys(phone)

    def send_request_description(self, description):
        self.browser.find_element(*ContactLocators.TEXT_AREA_REQUEST).send_keys(description)

    def switch_radio_delivery_answer_email(self):
        self.browser.find_element(*ContactLocators.RADIO_DELIVERY_ANSWER_EMAIL).click()

    def check_agreement_personal_data(self):
        self.browser.find_element(*ContactLocators.CHECKBOX_AGREEMENT_PROCESS_PERSONAL_DATA).click()

    def send_subject_request(self, subject):
        topic_select = Select(self.browser.find_element(*ContactLocators.SELECT_SUBJECT))
        topic_select.select_by_visible_text(subject)

    def should_be_company_name_field(self):
        assert self.is_element_presents(*ContactLocators.INPUT_COMPANY_NAME), 'There is not input for company name'

    def should_contact_title_page(self):
        assert self.browser.title == 'Kontakt - Bluemedia', 'Title page is not correct.'
