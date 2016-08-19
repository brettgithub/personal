from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
assert 'https://duckduckgo.com/?q=realpython' in driver.current_url
driver.quit()