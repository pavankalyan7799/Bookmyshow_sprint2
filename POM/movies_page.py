import re
import time
from Library.excel_lib import ReadExcel
from Library.config import Config


class BookMyShow:
    read_xl = ReadExcel()
    reg_locators = read_xl.read_locators(Config.MOVIES_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def enter_textfield(self, location):
        locator = self.reg_locators["enter_textfield"]
        self.driver.find_element(*locator).send_keys(location)
        time.sleep(2)

    def click_on_location(self):
        locator = self.reg_locators["click_on_location"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_movies(self):
        locator = self.reg_locators["click_on_movies"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_browsecinemas(self):
        locator = self.reg_locators["click_on_browsecinemas"]
        self.driver.find_element(*locator).click()

    def click_on_movietheater(self):
        locator = self.reg_locators["click_on_movietheater"]
        self.driver.find_element(*locator).click()

    def click_on_theater_date(self):
        locator = self.reg_locators["click_on_theater_date"]
        self.driver.find_element(*locator).click()

    def click_on_theater_halldate(self):
        locator = self.reg_locators["click_on_theater_halldate"]
        self.driver.find_element(*locator).click()

    def click_on_acceptbutton(self):
        locator = self.reg_locators["click_on_acceptbutton"]
        self.driver.find_element(*locator).click()

    def click_on_alert(self):
        locator = self.reg_locators["click_on_alert"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_selecteseats(self):
        locator = self.reg_locators["click_on_selecteseats"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_proceed(self):
        locator = self.reg_locators["click_on_proceed"]
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def click_on_selectseats(self):
        locator = self.reg_locators["click_on_selectseats"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_ticketsbutton(self):
        locator = self.reg_locators["click_on_ticketsbutton"]
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def click_on_prepay(self):
        locator = self.reg_locators["click_on_prepay"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_email(self, email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern,email)
        assert result,"valid email"
        locator = self.reg_locators["enter_email"]
        self.driver.find_element(*locator).send_keys(email)
        time.sleep(1)

    def enter_mobilenumber(self, mob_no):
        if isinstance(mob_no,float):
            mob_no = str(int(mob_no))
        assert len(mob_no) == 10
        locator = self.reg_locators["enter_mobilenumber"]
        self.driver.find_element(*locator).send_keys(mob_no)
        time.sleep(1)

    def click_on_continue(self):
        locator = self.reg_locators["click_on_continue"]
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def enter_cardno(self,cardno):
        if isinstance(cardno,float):
            cardno = int(cardno)
        assert len(cardno) == 19
        locator = self.reg_locators["enter_cardno"]
        self.driver.find_element(*locator).send_keys(cardno)
        time.sleep(2)

    def enter_cardname(self,cardname):
        locator = self.reg_locators["enter_cardname"]
        self.driver.find_element(*locator).send_keys(cardname)
        time.sleep(1)

    def enter_expmonth(self,exp_month):
        if isinstance(exp_month,float):
            exp_month = int(exp_month)
        locator = self.reg_locators["enter_expmonth"]
        self.driver.find_element(*locator).send_keys(exp_month)
        time.sleep(1)

    def enter_expyear(self,exp_year):
        if isinstance(exp_year,float):
            exp_year = int(exp_year)
        locator = self.reg_locators["enter_expyear"]
        self.driver.find_element(*locator).send_keys(exp_year)

    def enter_cvv(self,cvv):
        if isinstance(cvv, float):
            cvv = int(cvv)
        locator = self.reg_locators["enter_cvv"]
        self.driver.find_element(*locator).send_keys(cvv)
        time.sleep(2)
        self.driver.close()