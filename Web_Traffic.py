import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.microsoft import EdgeChromiumDriverManager as CM

# Print welcome message
print("A R K W A R D   B O O S T\nCopyright (C) Ark Corporation. All rights reserved.")
print("\nD E F Y   R E A L I T Y\n\n")

# Prompt user for input
Views = input("How many users do you want? :: ")
Views = int(Views)
URL = input("Enter the URL :: ")

# Set up browser options
options = webdriver.EdgeOptions()

# Set up mobile emulation
mobile_emulation = {
    "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/83.0.1025.133 Mobile Safari/535.19'
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# Set up the driver for the specified browser
bot = webdriver.Edge(executable_path=CM().install(), options=options)

# Navigate to the specified URL
# bot.get(URL)

# Set the window size and wait for the page to load
bot.set_window_size(500, 950)
time.sleep(5)
bot.get('https://www.youtube.com')
time.sleep(5)

# Loop through the specified number of views and refresh the page
for i in range(Views):
    print("S U C C E S S F U L")
    time.sleep(10)
    bot.refresh()
