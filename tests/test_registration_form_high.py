import allure

from demoqa_automation_practice_form.registration_page import RegistrationPage, TableResponsive
from resources import users


@allure.description('Это тест на регистрацию уровня high-level-step-objects')
@allure.tag('Registration')
def test_registration_user(browser_settings):

    registration_page = RegistrationPage()

    with allure.step("Открываем страницу регистрации"):
        registration_page.open()

    with allure.step("Удаляем баннер"):
        registration_page.remove_banner()

    with allure.step("Регистрируем  пользователя"):
        registration_page.register(users.new_user)


    table_responsive = TableResponsive()

    with allure.step("Проверяем регистрационные данные"):
        table_responsive.assert_data(users.new_user)
