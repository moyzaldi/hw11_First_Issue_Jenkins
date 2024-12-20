import os
from selene import browser, by, have, command
from resources.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def remove_banner(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()

    def fill_date_of_birth(self, mm, yyyy, dd):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(mm)).click()
        # browser.element('.react-datepicker__month-select').send_keys('4')
        browser.element('.react-datepicker__year-select').click().element(by.text(yyyy)).click()
        if len(dd) == 1:
            dd = '0' + dd
        browser.element(f'.react-datepicker__day--0{dd}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()

    def up_load_picture(self, path):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(os.path.join(os.path.dirname(__file__), f"../resources/images/{path}")))



    #     browser.element("#uploadPicture").send_keys(os.path.abspath(f"../resources/images/{path}"))
        # browser.element("#uploadPicture").set_value(
        #     os.path.abspath(
        #         os.path.join(os.path.dirname(resources._file_),f"images/{path}")
        #     )
        # )


    def fill_current_address(self, value):
        # browser.element('#currentAddress').type(value)
        # browser.element('#currentAddress').with_(set_value_by_js=True).set_value(value)  для переменной и  использовать  несколько раз
        browser.element('#currentAddress').perform(command.js.set_value(value))  # если один раз

    def fill_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def submit(self):
        browser.element('#submit').click()
        # browser.element('#submit').press_enter()
        # browser.element('#submit').perform(command.js.click)

    def register(self, new_user: User):
        self.fill_first_name(new_user.first_name)
        self.fill_last_name(new_user.last_name)
        self.fill_email(new_user.user_email)
        self.fill_gender(new_user.gender)
        self.fill_mobile(new_user.user_number)
        self.fill_date_of_birth(new_user.month, new_user.year, new_user.day)
        self.fill_subject(new_user.subjects)
        self.fill_hobby(new_user.hobbies)
        self.up_load_picture(new_user.images)
        self.fill_current_address(new_user.current_address)
        self.fill_state(new_user.state)
        self.fill_city(new_user.city)
        self.submit()


class TableResponsive:

    def assert_full_name(self, firstName,lastName):
        browser.element('.table').should(have.text(f'{firstName} {lastName}'))

    def assert_userEmail(self, userEmail):
        browser.element('.table').should(have.text(userEmail))

    def assert_gender(self, gender):
        browser.element('.table').should(have.text(gender))

    def assert_userNumber(self, userNumber):
        browser.element('.table').should(have.text(userNumber))

    def assert_date_of_birth(self, day, month,year):
        browser.element('.table').should(have.text(f'{day} {month},{year}'))

    def assert_subjects(self, subjects):
        browser.element('.table').should(have.text(subjects))

    def assert_hobbies(self, hobbies):
        browser.element('.table').should(have.text(hobbies))

    def assert_images(self, images):
        browser.element('.table').should(have.text(images))

    def assert_currentAddress(self, currentAddress):
        browser.element('.table').should(have.text(currentAddress))

    def assert_state_and_city(self, state, city):
        browser.element('.table').should(have.text(f'{state} {city}'))

    def assert_data(self, new_user: User):
        self.assert_full_name(new_user.first_name, new_user.last_name)
        self.assert_userEmail(new_user.user_email)
        self.assert_gender(new_user.gender)
        self.assert_userNumber(new_user.user_number)
        self.assert_date_of_birth(new_user.day, new_user.month, new_user.year)
        self.assert_subjects(new_user.subjects)
        self.assert_hobbies(new_user.hobbies)
        self.assert_images(new_user.images)
        self.assert_currentAddress(new_user.current_address)
        self.assert_state_and_city(new_user.state, new_user.city)