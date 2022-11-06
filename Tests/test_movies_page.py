import datetime
import pytest
from Library.config import Config
from POM.movies_page import BookMyShow
from Library.excel_lib import ReadExcel

class TestBookMyShow:
    read_xl = ReadExcel()
    data = read_xl.read_testdata("locations")

    @pytest.mark.parametrize("location, email, mob_no, cardno, cardname,exp_month,exp_year,cvv", data)
    def test_valid_credentials(self, init_driver, location, email, mob_no, cardno, cardname,exp_month,exp_year,cvv):
        driver = init_driver
        bm = BookMyShow(driver)
        try:
            bm.enter_textfield(location)
            bm.click_on_location()
            bm.click_on_movies()
            bm.click_on_browsecinemas()
            bm.click_on_movietheater()
            bm.click_on_theater_date()
            bm.click_on_theater_halldate()
            bm.click_on_acceptbutton()
            bm.click_on_alert()
            bm.click_on_selecteseats()
            bm.click_on_proceed()
            bm.click_on_selectseats()
            bm.click_on_ticketsbutton()
            bm.click_on_prepay()
            bm.enter_email(email)
            bm.enter_mobilenumber(mob_no)
            bm.click_on_continue()
            bm.enter_cardno(cardno)
            bm.enter_cardname(cardname)
            bm.enter_expmonth(exp_month)
            bm.enter_expyear(exp_year)
            bm.enter_cvv(cvv)

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            path = r"C:\Users\91779\PycharmProjects\book_myshow\screenshots\\"
            driver.save_screenshot(Config.SCREENSHOTS_PATH + name)
            raise err_msg
