from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
#driver.set_window_size(1120, 550)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")

driver.save_screenshot('out.png')

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

print '\n'
print 50 * '!'
print "Done!"
print 50 * '!'

