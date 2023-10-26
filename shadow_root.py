from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()


driver.get('https://www.abcmouse.com/abc/')


shadow_root_script = '''
const shadowRoot = arguments[0].shadowRoot;
return shadowRoot;
'''
element = driver.find_element(By.CSS_SELECTOR, "route-view[class='loaded']")
shadow_root = driver.execute_script(shadow_root_script, element)


element_in_shadow_dom = shadow_root.find_element(By.CSS_SELECTOR, 'signup-button.header-button.abcmouse-sans.enteractive.tab-outline-blue')
sleep(10)

element_in_shadow_dom.click()


driver.quit()

