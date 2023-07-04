import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_allure_step():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open("https://github.com")
    with allure.step("Клик в поле поиска"):
        browser.element(".header-search-input").click()
    with allure.step("Ввод в поле поиска адреса репозитория 'eroshenkoam/allure-example'"):
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    with allure.step("Нажать кнопку поиска"):
        browser.element(".header-search-input").submit()
    with allure.step("Кликнуть на название репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Нажать кнопку Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Элемент №65 отображается"):
        browser.element(by.partial_text("#65")).should(be.visible)
    with allure.step("Закрыть окно браузера"):
        browser.quit()
