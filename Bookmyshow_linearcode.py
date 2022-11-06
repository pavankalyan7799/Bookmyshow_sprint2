import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
c_path = r"C:\Users\91779\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path = c_path)
path = r"https://in.bookmyshow.com/"
driver.get(path)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath",'//img[@alt="CHEN"]').click()
driver.find_element("link text","Movies").click()
driver.find_element("xpath","(//div[text()='Browse by Cinemas'])[1]").click()
driver.find_element("xpath","//a[text()='AGS Cinemas OMR: Navlur']").click()
driver.find_element("xpath",'(//div[@class="slick-track"])[2]//li[1]').click()
time.sleep(1)
driver.find_element("xpath",'(//a[@class="data-enabled showtime-pill showtime-pill-with-no-hover "])[1]').click()
time.sleep(1)
driver.find_element("id",'btnPopupAccept').click()
time.sleep(1)
driver.find_element("xpath","//button[text()='OK']").click()
time.sleep(1)
driver.find_element("id",'pop_1').click()
driver.find_element("xpath",'//ul[@id="popQty"]//li[2]').click()
driver.find_element("id","proceed-Qty").click()
#alert_obj = driver.switch_to_alert()
#alert_obj.dismiss()
driver.find_element("xpath",'(//a[@class="_available"])[5]').click()
driver.find_element("xpath",'(//a[@id="btmcntbook"])[1]').click()
driver.find_element("id",'prePay').click()
driver.find_element("id",'txtEmail').send_keys("pk7799461667@gmail.com")
driver.find_element("id",'txtMobile').send_keys("8639461234")
time.sleep(1)
driver.find_element("id",'dContinueContactSec').click()
driver.find_element("id",'txtCardNo').send_keys("1234 5678 9123")
driver.find_element("id",'txtCardName').send_keys("pavan kalyan vinnakota")
driver.find_element("id",'txtExpMonth').send_keys("07")
driver.find_element("id",'txtExpYear').send_keys("1998")
driver.find_element("id",'txtCVV').send_keys("143")
driver.find_element("id",'makeCardPayment').click()








