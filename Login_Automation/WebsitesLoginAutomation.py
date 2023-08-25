from selenium import webdriver
import yaml

with open('loginDetails.yml', 'r') as yaml_file:
    conf = yaml.safe_load(yaml_file)
myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']

driver = webdriver.Chrome()

def loginNumber(driver,url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)

    timeout = 10
    try:
        driver.find_element("name", "loginId").send_keys(username)
        driver.find_element("id", "loginPassword").send_keys(password)
        driver.find_element("id", "login-button").click()
    except:
        print("Timeout waiting for page to load")

loginNumber(driver,"https://www.virginplus.ca/myAccount/logon-smart.do?typeCode=postpaid&TYPE=33554433&REALMOID=06-0004e1a4-702a-10ed-af81-791a8e750000&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-7JlqyXXIx62fWJKJRjpJpmScYdTuCZOVz7B%2b2gDO7%2bCR4ci%2fvYXsupTRISNl0iBa&TARGET=-SM-HTTPS%3a%2f%2fmyaccount%2evirginplus%2eca%2fLogin","loginId", myFbEmail, "loginPassword", myFbPassword, "login-button")
input("Press Enter to close the browser...")
driver.close()

