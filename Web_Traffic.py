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
# from webdriver_manager.chrome import ChromeDriverManager as CM
from webdriver_manager.microsoft import EdgeChromiumDriverManager as CM

print("A R K W A R D   B O O S T\nCopyright (C) Ark Corporation. All rights reserved.\n\nD E F Y   R E A L I T Y\n\n")

Views = input("How many user you want :: ")
Views = int(Views)
URL = input("Enter the URL :: ")

options = webdriver.ChromeOptions()
options = webdriver.EdgeOptions()
# options.add_argument("--headless")

mobile_emulation = {
    "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/83.0.1025.133 Mobile Safari/535.19'
}
options.add_experimental_option("mobileEmulation", mobile_emulation)
# bot = webdriver.Chrome(executable_path=CM().install(), options=options)
bot = webdriver.Edge(executable_path=CM().install(), options=options)

# bot.get(URL)

bot.set_window_size(500, 950)
time.sleep(5)
bot.get('www.youtube.com')
time.sleep(5)

for i in range(Views):
    print("S U C E S S F U L")
    time.sleep(10)
    bot.refresh()
