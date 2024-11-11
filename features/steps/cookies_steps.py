from behave import given, when, then

from tests.test_cookies import get_cookie_value


@given('the "{cookie_name}" cookie is removed')
def remove_cookie(context, cookie_name):
    context.page.context.clear_cookies(name=cookie_name)


@given('I open the "{url}" page')
def navigate_to_the_page(context, url):
    context.page.goto(url)


@when('I click on the "Dostosuj" button on the cookie policy modal')
def click_the_cookies_settings_button(context):
    context.cookies_modal.settings.click()


@when('I click on the "Cookies analityczne" checkbox on the cookie policy modal')
def click_the_analytical_cookies_checkbox(context):
    context.cookies_modal.analitycal_cookies.click()


@when('I click on the "Zaakceptuj wybrane" button on the cookie policy modal')
def click_the_accept_chosen_cookies_button(context):
    context.cookies_modal.accept_chosen_cookies.click()


@then('the "{cookie_name}" cookie value is set to "{expected_cookie_value}"')
def check_cookie_value(context, cookie_name, expected_cookie_value):
    cookie_value = get_cookie_value(context.page, cookie_name)
    assert cookie_value == expected_cookie_value, (
        f"The '{cookie_name}' cookie value does not match the expected one. "
        f"The expected value is '{expected_cookie_value}', but got '{cookie_value}'."
    )
