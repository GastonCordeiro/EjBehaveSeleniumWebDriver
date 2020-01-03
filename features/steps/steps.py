from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


@given('a browser')
def step_impl(context):
    context.browser = webdriver.Chrome(executable_path='/home/administrador/PycharmProjects/test1/chromedriver')


@when("I enter the url {url}")
def step_impl(context, url):
    context.browser.get(url)


@when("I click on a Woman")
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a").click()
    time.sleep(1)


@when("I click on Dresses")
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[1]/div[1]/div/ul/li[2]/a").click()
    time.sleep(1)


@when("I find class product dresses")
def step_impl(context):
    dresses = context.browser.find_elements_by_class_name("product_list")
    time.sleep(3)

    for dress in dresses:
        dress.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/div/div[2]/h5/a").click()
    time.sleep(3)



@when("I find SIZE click in M")
def step_impl(context):
    select = Select(context.browser.find_element_by_id("group_1"))
    select.select_by_value('2')




@then('I will find the dress size M')
def step_impl(context):
    if context.browser.current_url == "http://automationpractice.com/index.php?id_product=3&controller=product#/color-orange/size-m":
        pass



#Second Scenario

@given('I am on url {url}')
def step_impl(context, url):
    context.browser = webdriver.Chrome(executable_path='/home/administrador/PycharmProjects/test1/chromedriver')
    context.browser.get(url)


@when("I click on Submit")
def step_impl(context):
    context.browser.find_element_by_name("Submit").click()
    time.sleep(1)


@when("Proceed to checkout")
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a").click()
    time.sleep(2)


@then("Check url")
def step_impl(context):
    if context.browser.get == "http://automationpractice.com/index.php?controller=order":
        pass











