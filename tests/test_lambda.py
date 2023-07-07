import allure
from allure_commons.types import Severity
from selene import browser, by


@allure.tag("Blocker")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "ssergienko")
@allure.feature("Тестирование через шаги декоратора")
@allure.story("Проверка вариантов оборачивания тестов в аллюре")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element("//span[@class='flex-1']").click()
    browser.element("//input[@id='query-builder-test']").send_keys(repo)
    browser.element("//input[@id='query-builder-test']").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()
