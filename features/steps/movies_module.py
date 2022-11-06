import re
import time
from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\91779\PycharmProjects\book_myshow\drivers\chromedriver.exe")
    context.driver.get(r"https://in.bookmyshow.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('open bookmyshow home page and click on location')
def click_on_movies(context):
    context.driver.find_element("xpath",'//img[@alt="CHEN"]').click()
    context.driver.find_element("link text","Movies").click()
    context.driver.find_element("xpath","(//div[text()='Browse by Cinemas'])[1]").click()
    context.driver.find_element("xpath","//a[text()='AGS Cinemas OMR: Navlur']").click()

@then('User must be able to click on location')
def click_on_location(context):
    context.driver.find_element("xpath",'(//div[@class="slick-track"])[2]//li[1]').click()
    context.driver.find_element("xpath",'(//a[@class="data-enabled showtime-pill showtime-pill-with-no-hover "])[1]').click()
    context.driver.find_element("id",'btnPopupAccept').click()
    context.driver.find_element("xpath","//button[text()='OK']").click()

@then('User must be able to click on movietheater')
def click_on_movietheater(context):
    context.driver.find_element("id",'pop_1').click()
    context.driver.find_element("xpath",'//ul[@id="popQty"]//li[2]').click()

@then('user must be able to click on seats')
def select_the_seats(context):
    context.driver.find_element("id","proceed-Qty").click()
    context.driver.find_element("xpath",'(//a[@class="_available"])[5]').click()

@then('user must be able to click on seat positions')
def select_the_seatpositions(context):
    context.driver.find_element("xpath",'(//a[@id="btmcntbook"])[1]').click()
    context.driver.find_element("id",'prePay').click()

@when('User is able to enter email "{email}"')
def enter_the_email(context,email):
    context.driver.find_element("id",'txtEmail').send_keys(email)
    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern, email)
    assert result, "invalid email"


@when('User is able to enter mobilenumber "{mobilenumber}"')
def enter_the_mobilenumber(context,mobilenumber):
    context.driver.find_element("id",'txtMobile').send_keys(mobilenumber)

@when('User is able to click on submit button')
def click_on_submit_button(context):
    context.driver.find_element("id",'dContinueContactSec').click()
    time.sleep(3)

@when('User is able to enter the usercardnumber "{cardnumber}"')
def enter_the_cardnumber(context,cardnumber):
    context.driver.find_element("id",'txtCardNo').send_keys(cardnumber)
    if isinstance(cardnumber,float):
        cardnumber = int(cardnumber)
    time.sleep(2)

@then('User is able to enter cardname "{cardname}"')
def enter_the_cardname(context,cardname):
    context.driver.find_element("id",'txtCardName').send_keys(cardname)
    time.sleep(2)

@then('User is able to enter cardexpirymonth "{expmonth}"')
def enter_the_expmonth(context,expmonth):
    context.driver.find_element("id",'txtExpMonth').send_keys(expmonth)
    time.sleep(2)

@then('User is able to enter cardexpiryyear "{expyear}"')
def enter_the_expyear(context,expyear):
    context.driver.find_element("id",'txtExpYear').send_keys(expyear)
    time.sleep(2)

@then('User is able to enter cardcvv "{cvv}"')
def enter_the_cvv(context,cvv):
    context.driver.find_element("id",'txtCVV').send_keys(cvv)
    time.sleep(2)

@then('User is able to click on make the payment')
def step_impl(context):
    context.driver.find_element("id",'makeCardPayment').click()

@then('close the browser')
def step_impl(context):
    context.driver.close()



