from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import os
import time
chromedriver = "C:/webdrivers/chromedriver"
os.environ["webdriver.chrome.driver"]= chromedriver
driver=webdriver.Chrome(chromedriver)
driver.get("https://www.analytics.ford.com/QvAJAXZfc/opendoc.htm?document=it%5Ceassets%20reporting%20dashboard.qvw&lang=en-US&host=QVS%40ProdCluster")

time.sleep(10)
driver.execute_script("$('#inp_37').click()")
time.sleep(5)
# best = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
best = driver.find_element(By.CSS_SELECTOR, "div:nth-child(12) div:nth-child(2) div:nth-child(1) img:nth-child(1)")
driver.execute_script("arguments[0].click(2);", best)
action = ActionChains(driver)
action.double_click(best).perform()

time.sleep(5)

# sel = Select(driver.find_element_by_class_name('QvListbox'))
# sel.select_by_visible_text('AWOL 30-90')
sel = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL >180']/div[1]")
driver.execute_script("arguments[0]", sel)
action = ActionChains(driver)
action.double_click(sel).perform()

time.sleep(5)

# div:nth-child(11) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)

besta = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
driver.execute_script("arguments[0].click(2);", besta)
action = ActionChains(driver)
action.click(besta).perform()
time.sleep(3)
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]
sela = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]")
driver.execute_script("arguments[0].click()", sela)
action = ActionChains(driver)
action.double_click(sela).perform()
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL >180']/div[1]
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 90-180']/div[1]


# body > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)















from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
chromedriver = "C:/webdrivers/chromedriver"
os.environ["webdriver.chrome.driver"]= chromedriver
driver=webdriver.Chrome(chromedriver)
driver.get("https://www.analytics.ford.com/QvAJAXZfc/opendoc.htm?document=it%5Ceassets%20reporting%20dashboard.qvw&lang=en-US&host=QVS%40ProdCluster")

# div[title='Clear All Selections']
time.sleep(10)
timere = driver.find_element(By.CSS_SELECTOR, "div[title='Clear All Selections']")
driver.execute_script("arguments[0].click;", timere)
action = ActionChains(driver)
action.click(timere).perform()


time.sleep(5)
driver.execute_script("$('#inp_37').click()")

timea = driver.find_element(By.CSS_SELECTOR, ".ui-state-default.ui-state-highlight.ui-state-active.ui-state-hover")
driver.execute_script("arguments[0].click;", timea)
action = ActionChains(driver)
action.click(timea).perform()


# action = ActionChains(driver).key_down(Keys.CONTROL).click(selbp).key_up(Keys.CONTROL).perform()

time.sleep(5)
clam = driver.find_element(By.CSS_SELECTOR, "div[title='ASSET STATE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()
clam = driver.find_element(By.CSS_SELECTOR, "div[title='ASSET STATUS'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).click(clam).key_down(Keys.CONTROL).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='BLUE DOLLAR CONFIGURATION'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='COMPUTER MODEL'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='COMPUTER NAME'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='DEVICE STATUS'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='DEVICE TYPE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='DEVICE USER CDSID'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='EQUIPMENT TYPE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='FIRST LOG DATE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()


clam = driver.find_element(By.CSS_SELECTOR, "div[title='FORD MANAGER'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='INSTALL DATE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='LAST LOG DATE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='LEASE END DATE'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()


clam = driver.find_element(By.CSS_SELECTOR, "div[title='LOCATION DESCRIPTION'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='SERIAL NUMBER'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='SLS LAST USER'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).perform()

clam = driver.find_element(By.CSS_SELECTOR, "div[title='TRANSFER STATUS'] div[class='QvOptional_LED_CHECK_363636']")
driver.execute_script("arguments[0].click();", clam)
action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).key_up(Keys.CONTROL).perform()

'''Asset State'''
time.sleep(3)
# best = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
best = driver.find_element(By.CSS_SELECTOR, "div:nth-child(12) div:nth-child(2) div:nth-child(1) img:nth-child(1)")
driver.execute_script("arguments[0].click(2);", best)
action = ActionChains(driver)
action.double_click(best).perform()

time.sleep(2)

# sel = Select(driver.find_element_by_class_name('QvListbox'))
# sel.select_by_visible_text('AWOL 30-90')
sel = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL >180']/div[1]")
driver.execute_script("arguments[0]", sel)
action = ActionChains(driver).key_down(Keys.CONTROL).click(sel).perform()

# action = ActionChains(driver)
# # action.click(sel).perform()
# action.click_and_hold(sel).perform()

time.sleep(2)

# div:nth-child(11) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)

'''besta = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
driver.execute_script("arguments[0].click(2);", besta)
action = ActionChains(driver)
action.click(besta).perform()
time.sleep(5)
'''# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]
sela = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]")
driver.execute_script("arguments[0].click()", sela)
action = ActionChains(driver).key_down(Keys.CONTROL).click(sela).perform()

# action = ActionChains(driver)
# action.click_and_hold(sela).perform()
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL >180']/div[1]
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 30-90']/div[1]
# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 90-180']/div[1]
time.sleep(2)
selb = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='AWOL 90-180']/div[1]")
driver.execute_script("arguments[0].click()", selb)
action = ActionChains(driver).key_down(Keys.CONTROL).click(selb).perform()
# action = ActionChains(driver).key_down(Keys.CONTROL).click(clam).key_up(Keys.CONTROL).perform()

time.sleep(2)
selb = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='DETECTED']/div[1]")
driver.execute_script("arguments[0].click()", selb)
action = ActionChains(driver).key_down(Keys.CONTROL).click(selb).perform()
# body > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
# Program office
time.sleep(2)
selb = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='IN-STORAGE']/div[1]")
driver.execute_script("arguments[0].click()", selb)
action = ActionChains(driver).key_down(Keys.CONTROL).click(selb).perform()

time.sleep(2)
selb = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='MANUAL']/div[1]")
driver.execute_script("arguments[0].click()", selb)
action = ActionChains(driver).key_down(Keys.CONTROL).click(selb).key_up(Keys.CONTROL).perform()

time.sleep(3)


bestp = driver.find_element(By.CSS_SELECTOR, "div:nth-child(29) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
driver.execute_script("arguments[0].click(2);", bestp)
action = ActionChains(driver)
action.double_click(bestp).perform()

# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='APA-FBSC']/div[1]
time.sleep(2)

# sel = Select(driver.find_element_by_class_name('QvListbox'))
# sel.select_by_visible_text('AWOL 30-90')
selp = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='APA-FBSC']/div[1]")
driver.execute_script("arguments[0]", selp)
action = ActionChains(driver)
action.click(selp).perform()



time.sleep(3)

bestap = driver.find_element(By.CSS_SELECTOR, "div:nth-child(29) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
driver.execute_script("arguments[0].click(2);", bestap)
action = ActionChains(driver)
action.double_click(bestap).perform()
# action.click(bestap).perform()
# action.click(bestap).perform()

# div[id='DS'] div:nth-child(4) span:nth-child(1)
time.sleep(2)

bestapd = driver.find_element(By.CSS_SELECTOR, "div[id='DS'] div:nth-child(4) span:nth-child(1)")
driver.execute_script("arguments[0].click(2);", bestapd)
action = ActionChains(driver)
action.double_click(bestapd).perform()
time.sleep(1)
action.double_click(bestapd).perform()
time.sleep(1)
action.click(bestapd).perform()

time.sleep(2)

# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='APA-FTSI']/div[1]
selbp = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='APA-FTSI']/div[1]")
driver.execute_script("arguments[0].click()", selbp)
action = ActionChains(driver).key_down(Keys.CONTROL).click(selbp).key_up(Keys.CONTROL).perform()
# action.release(selbp).perform()



# div[title='ASSET STATE'] div[class='QvSelected_LED_CHECK_363636']
'''
time.sleep(5)

#try retry


bestp = driver.find_element(By.CSS_SELECTOR, "div:nth-child(29) div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)")
driver.execute_script("arguments[0].click(2);", bestp)
action = ActionChains(driver)
action.click(bestp).perform()

# //body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='APA-FBSC']/div[1]
time.sleep(5)

# sel = Select(driver.find_element_by_class_name('QvListbox'))
# sel.select_by_visible_text('AWOL 30-90')
selp = driver.find_element(By.XPATH, "//body/div[@id='DS']/div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='APA-FBSC']/div[1]")
driver.execute_script("arguments[0]", selp)
action = ActionChains(driver)
action.release(selp).perform()


'''

# div[title='Physical Inventory Report'] div[title='Send to Excel']

time.sleep(3)

exl = driver.find_element(By.CSS_SELECTOR, "div[title='Physical Inventory Report'] div[title='Send to Excel']")
driver.execute_script("arguments[0].click(2);", exl)
action = ActionChains(driver)
action.double_click(exl).perform()