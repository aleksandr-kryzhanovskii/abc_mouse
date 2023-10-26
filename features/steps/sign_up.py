from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


@given('Open ABC Mouse page')
def open_dress_page(context):
    context.app.main_page.open_main_page()

@when('Click sign up button')
def open_dress_page(context):
    context.app.click_sign_up_button()

@then('Verify {link} link returned')
def verify_can_select_colors(context, link):
   context.app.product_page.verify_url_contains_query()

@when('Input {email} into email field')
def input_amazon_search(context, email):
    context.app.main_page.input_email(email)

@when('Click Submit button')
def open_dress_page(context):
    context.app.click_submit_button()

@then('Verify {text} text is present')
def verify_become_a_member_text(context, text):
    context.app.main_page.verify_become_a_member_text()

