from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import time
from IPython import embed

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

var = 1
# for second in xrange(1,2):
#     print 50 * '#'
#     if second > 1:
#         print "waiting {0} seconds".format(second)
#     else:
#         print "waiting {0} second".format(second)
#     print 50 * '#'
#     time.sleep(1)

print "in embed?"
embed()
var = 2
embed()
print "out embed!!!!!!!!!!!!!!!!!"

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

print '\n'
print 50 * '!'
print "Done!"
print 50 * '!'

