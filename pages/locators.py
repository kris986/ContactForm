from selenium.webdriver.common.by import By


class ContactLocators:
    CONTACT_HEADER = (By.CSS_SELECTOR, 'h1.main-content__header__title')
    RADIO_PRIVATE_CLIENT = (
        By.CSS_SELECTOR,
        'form.contact__form div.grid-24 input[data-request-data="id:2,post_id:370"][name="client_type"]')
    RADIO_BUSINESS_CLIENT = (
        By.CSS_SELECTOR,
        'form.contact__form div.grid-24 input[data-request-data="id:1,post_id:370"][name="client_type"]')
    INPUT_NAME_SURNAME = (By.CSS_SELECTOR, 'form.contact__form input#name[name="name"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'form.contact__form input#email_c[name="email_c"]')
    INPUT_PHONE = (By.CSS_SELECTOR, 'form.contact__form input#phone[name="phone"]')
    SELECT_TOPIC = (By.CSS_SELECTOR, 'div.form__select select#subject optgroup > *')
    TEXT_AREA_REQUEST = (By.CSS_SELECTOR, 'form.contact__form textarea#body[name="body"]')
    RADIO_DELIVERY_ANSWER_EMAIL = (By.CSS_SELECTOR, 'form.contact__form input[name="respond_type"][value="email"]')
    RADIO_DELIVERY_ANSWER_POST = (By.CSS_SELECTOR, 'form.contact__form input[name="respond_type"][value="post"]')
    CHECKBOX_AGREEMENT_PROCESS_PERSONAL_DATA = (
        By.CSS_SELECTOR, 'form.contact__form input#agreement_1[name="agreement_1"]')
    CHECKBOX_AGREEMENT_RECEIVE_EMAILS = (By.CSS_SELECTOR, 'form.contact__form input#agreement_2[name="agreement_2"]')
    CHECKBOX_AGREEMENT_TRUSTED_PARTNERS = (By.CSS_SELECTOR, 'form.contact__form input#agreement_3[name="agreement_3"]')
    BUTTON_SEND = (By.CSS_SELECTOR, 'form.contact__form button.submit-contact')
    LINK_PRIVACY = (By.XPATH, 'a[href='']')
