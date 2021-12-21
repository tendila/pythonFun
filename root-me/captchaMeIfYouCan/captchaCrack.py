from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re, os, base64, pickle, subprocess

###########################################################
#   Challenge root-me.org => prog => CaptchaMeIfYouCan    #
#     ~/captchaCrack.py            JUST FOR FUN            #
#               MADE IN 12/21 - 410!5                     #
###########################################################

path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(service=Service(path))

######### Log in to root-me.org
# driver.get('https://www.root-me.org/?page=login')
# login_form = driver.find_element(By.ID, 'var_login')
# login_form.send_keys('login')
# login_form.send_keys(Keys.RETURN)
# passwd_form = driver.find_element(By.ID, 'password')
# passwd_form.send_keys('pwd')
# passwd_form.send_keys(Keys.RETURN)
# driver.find_element(By.XPATH, '//*[@id="formulaire_login"]/p/input').submit()
# print("Login to root-me.org successful.")


######### Storing the cookies
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# driver.quit()

######### Open in a new tab
# driver.execute_script('window.open("http://challenge01.root-me.org/programmation/ch8/")',"_blank")

print("Login to the challenge.. ")
driver.get('http://challenge01.root-me.org/programmation/ch8/')

######### Loading the stored cookies
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#   driver.add_cookie(cookie)

######### Get the captcha from the challenge
regexImg = r'data:image/png;base64,(.*)"'
result = re.search(regexImg, driver.page_source)

print("Code de l'image")
print(result)
result = result.group(1)

######### Put the image in a captcha.png file
result = base64.b64decode(result)
file_handle = open('captcha.png', 'wb')
file_handle.write(result)
file_handle.close()

######### Launch gocr -i on captcha.png
file_handle = open('captcha.png', 'rb')
result = subprocess.Popen(['gocr -i captcha.png'],
                          shell=True, stdout=subprocess.PIPE).communicate()[0]
file_handle.close()

######### Delete the noise
result = result.replace(b'\n', b'')
result = result.replace(b' ', b'')
result = result.replace(b',', b'')
result = result.replace(b'\'', b'')
print(result.decode())

######### Send the response
captchaForm = driver.find_element(By.NAME, 'cametu')
# driver.find_element(By.XPATH, '/html/body/form/input[2]').submit()
captchaForm.send_keys(result.decode())

print(driver.page_source)
sleep(5)

driver.quit() 

######### Clean-up
for file in os.listdir('.'):
    if file.endswith('.png'):
        os.remove(file)