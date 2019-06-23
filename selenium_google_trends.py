from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import Keywords
keywords = Keywords.keywords


webdriver_path = '/home/targoon/Downloads/chromedriver_linux64/chromedriver'

def enable_headless_download(browser, download_path):
    # Add missing support for chrome "send_command" to selenium webdriver
    browser.command_executor._commands["send_command"] = \
        ("POST", '/session/$sessionId/chromium/send_command')
 
    params = {'cmd': 'Page.setDownloadBehavior',
              'params': {'behavior': 'allow', 'downloadPath': download_path}}
    browser.execute("send_command", params)

# Add arguments telling Selenium to not actually open a window


for keyword in keywords['Social Unrest']:
    download_path = 'data/' + keyword
    chrome_options = Options()
    download_prefs = {'download.default_directory' : download_path,
                      'download.prompt_for_download' : False,
                      'profile.default_content_settings.popups' : 0}

    chrome_options.add_experimental_option('prefs', download_prefs)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    url = 'https://trends.google.com/trends/explore?date=2018-10-01%202019-04-08&geo=US&q=' + keyword
    # Start up browser
    browser = webdriver.Chrome(executable_path=webdriver_path,chrome_options=chrome_options)
    browser.get(url) 
    enable_headless_download(browser, download_path)
    # Load webpage
    browser.get(url)
    time.sleep(5)
    button = browser.find_element_by_css_selector('.widget-actions-item.export')
    button.click()
    time.sleep(5)
    browser.quit()
