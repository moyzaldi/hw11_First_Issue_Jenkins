import allure

from demoqa_automation_practice_form.registration_page import RegistrationPage, TableResponsive
from resources.users import new_user


@allure.description('Это тест на регистрацию уровня mid-level-step-objects')
@allure.tag('Registration')
def test_registration_user(browser_settings):

    registration_page = RegistrationPage()

    with allure.step("Открываем страницу регистрации"):
        registration_page.open()

    with allure.step("Удаляем баннер"):
        registration_page.remove_banner()

    with allure.step("Заполняем имя пользователя"):
        registration_page.fill_first_name(new_user.first_name)

    with allure.step("Заполняем имя фамилию"):
        registration_page.fill_last_name(new_user.last_name)

    with allure.step("Заполняем email"):
        registration_page.fill_email(new_user.user_email)

    with allure.step("Заполняем пол"):
        registration_page.fill_gender(new_user.gender)

    with allure.step("Заполняем телефон"):
        registration_page.fill_mobile(new_user.user_number)

    with allure.step("Заполняем дату рождения"):
        registration_page.fill_date_of_birth(new_user.month, new_user.year, new_user.day)

    with allure.step("Заполняем предметы"):
        registration_page.fill_subject(new_user.subjects)

    with allure.step("Заполняем хобби"):
        registration_page.fill_hobby(new_user.hobbies)

    with allure.step("Загружаем картинку"):
        registration_page.up_load_picture(new_user.images)

    with allure.step("Заполняем а текущий адрес"):
        registration_page.fill_current_address(new_user.current_address)

    with allure.step("Заполняем штат"):
        registration_page.fill_state(new_user.state)

    with allure.step("Заполняем город"):
        registration_page.fill_city(new_user.city)

    with allure.step("Отправляем данные"):
            registration_page.submit()


    table_responsive = TableResponsive()

    with allure.step("Проверяем полное имя"):
        table_responsive.assert_full_name(new_user.first_name, new_user.last_name)

    with allure.step("Проверяем email"):
        table_responsive.assert_userEmail(new_user.user_email)

    with allure.step("Проверяем пол"):
        table_responsive.assert_gender(new_user.gender)

    with allure.step("Проверяем  телефон"):
        table_responsive.assert_userNumber(new_user.user_number)

    with allure.step("Проверяем дату рождения"):
        table_responsive.assert_date_of_birth(new_user.day, new_user.month, new_user.year)

    with allure.step("Проверяем предмет"):
        table_responsive.assert_subjects(new_user.subjects)

    with allure.step("Проверяем хобби"):
        table_responsive.assert_hobbies(new_user.hobbies)

    with allure.step("Проверяем картинку"):
        table_responsive.assert_images(new_user.images)

    with allure.step("Проверяем текущий адрес"):
        table_responsive.assert_currentAddress(new_user.current_address)

    with allure.step("Проверяем штат и город"):
        table_responsive.assert_state_and_city(new_user.state, new_user.city)