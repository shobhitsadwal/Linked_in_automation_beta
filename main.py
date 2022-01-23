from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException    #common exceptions
from selenium.common.exceptions import ElementNotInteractableException   #for not interactable objects


webdriver_path="D:\chrome driver\chromedriver_win32\chromedriver.exe"     #common path element

driver=webdriver.Chrome(executable_path=webdriver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2813582804&geoId=92000000&keywords=marketing%20intern&location=Worldwide")

sign_in=driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
id=driver.find_element(by=By.ID,value='username')
password=driver.find_element(by=By.ID,value='password')
id.send_keys('youremail')
# id.send_keys(Keys.ENTER)
password.send_keys("yourpassword")
down_sign_in=driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[3]/button')
down_sign_in.click()
# down_sign_in=driver.find_elements(by=By.CSS_SELECTOR,value='.ember-view a')
# down_sign_in=driver.find_element(by=By.ID,value='ember246')
time.sleep(3)

all_listings = driver.find_elements(by=By.CSS_SELECTOR,value=".job-card-container--clickable")

for i in all_listings:
    i.click()              #listing of the jobs
    time.sleep(2)

    try:    #trying the following code for each iteration

        apply_button=driver.find_element(by=By.CSS_SELECTOR,value='.jobs-s-apply button')
        apply_button.click()
        #Now we have to fill the phone number
        phone = driver.find_element(by=By.CLASS_NAME,value="fb-single-line-text__input")
        phone.send_keys('34434343')
        time.sleep(4)      #sleeping for 4 seconds  

        submit_button=driver.find_element(by=By.CSS_SELECTOR,value='footer button')
        time.sleep(2)
        if submit_button.get_attribute('data-control-name')=='continue_unify':
            cross_button=driver.find_element(by=By.CLASS_NAME,value='artdeco-modal__dismiss')
            cross_button.click()
            time.sleep(2)
            discard_button=driver.find_element(by=By.CSS_SELECTOR,value='.artdeco-modal__actionbar .artdeco-button--primary')
            discard_button.click()
            print('complex application skipped')
            continue

        else:
            submit_button.click()
            continue

    except NoSuchElementException:
        print('the exceptions are handled dont worry ')

    except ElementNotInteractableException:
        continue

