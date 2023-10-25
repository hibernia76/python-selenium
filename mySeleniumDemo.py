import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# So, the sequence of events is as follows:

# Open Python.org
# Maximize the window
# Click the "Downloads" button
# Take a screenshot
# Wait for 5 seconds (added using time.sleep(5))
# Go back to the previous page (Python.org)
# Locate the Search
# Input and send "FAQ"
# Take a screenshot
# Go back to the previous page (Python.org)
# Wait for 5 seconds (sleep)
# Close the browser

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# Maximize the window
driver.maximize_window()

# Find and click the download button
download_button = driver.find_element(By.LINK_TEXT, "Downloads")
download_button.click()

# Create a WebDriverWait instance with a timeout of 5 seconds
wait = WebDriverWait(driver, 5)

# Take a screenshot
driver.save_screenshot("C:/Users/admin/Desktop/selenium/screenshotDownload.png")

# Go back to the previous page
driver.back()

# Wait for an element with class "search-field" to be present (Search Box )
search_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-field")))

# Enter "FAQ" into the search field
search_field.send_keys("FAQ")

# Submit the form (either by pressing Enter or clicking the "Go" button)
search_field.send_keys(Keys.RETURN)  # Press Enter

# Create a WebDriverWait instance with a timeout of 5 seconds
wait = WebDriverWait(driver, 5)

# Take a screenshot
driver.save_screenshot("C:/Users/admin/Desktop/selenium/screenshotFAQ.png")

# Go back to the previous page
driver.back()

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.close()



