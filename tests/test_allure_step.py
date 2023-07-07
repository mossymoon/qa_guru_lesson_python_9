import json

import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure import attachment_type


def test_allure_step():
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, the world is not enough</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)

    with allure.step("Открываем главую страницу GitHub"):
        browser.open("https://github.com")
    with allure.step("Клик в поле поиска"):
        browser.element("//span[@class='flex-1']").click()
    with allure.step("Ввод в поле поиска адреса репозитория 'eroshenkoam/allure-example'"):
        browser.element("//input[@id='query-builder-test']").send_keys("eroshenkoam/allure-example")
    with allure.step("Нажать кнопку поиска"):
        browser.element("//input[@id='query-builder-test']").submit()
    with allure.step("Кликнуть на название репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Нажать кнопку Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Элемент №65 отображается"):
        browser.element(by.partial_text("#65")).should(be.visible)
    with allure.step("Закрыть окно браузера"):
        browser.quit()
