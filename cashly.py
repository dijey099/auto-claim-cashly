import os
import time
from tqdm import tqdm
from termcolor import colored
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


load_dotenv(dotenv_path=".env")

MAIL = os.getenv("MAIL")
URL = "https://cashlyfaucet.com"
print("*** Auto Claim for Cashly websites ***")
print("Auto claiming on " + colored("https://cashlyfaucet.com", 'magenta'))
print(colored("Buy this script from the author only!", 'white', 'on_red', attrs=['bold']) + "\n")
print("Author: " + colored("Dijey", 'green'))
print("Maintainer: " + colored("Dijey", 'green'))
print("Facebook: " + colored("https://fb.me/d1j3y", 'cyan'))
print("Mobile: " + colored("+261 32 61 968 23\n\n", 'yellow'))

opts = Options()
opts.add_argument("--width=240")
opts.add_argument("--height=800")
opts.add_argument("--headless")
opts.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36")
browser = webdriver.Firefox(options=opts)


def print_as_log(log):
	_time = time.time()
	m_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_time))
	print(f"[{m_time}] {log}")


print_as_log("Login...")
browser.get(URL)
login_btn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
mail_field = browser.find_element(By.NAME, "address")

mail_field.send_keys(MAIL)
time.sleep(1)
login_btn.click()

checked = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{MAIL}')]")))

if checked:
	print_as_log(colored("Logged in!", 'green'))
	balance_field = browser.find_element(By.ID, "balance")
	print_as_log(colored(f"Balance: ${balance_field.text}", 'cyan', attrs=['bold']))
	print_as_log("Preparing for new claim...")

	while True:
		try:
			login_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
			mail_field = browser.find_element(By.NAME, "address")
			mail_field.send_keys(MAIL)
			print_as_log("Login screen detected!")
			time.sleep(1)
			login_btn.click()
		except:
			pass

		c_btn = browser.find_element(By.ID, "requestdaily")
		c_btn.click()

		rec_frame = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]')))
		browser.switch_to.frame(rec_frame)
		time.sleep(5)
		rec_btn = browser.find_element(By.ID, "recaptcha-anchor")
		rec_btn.click()

		try:
			WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="recaptcha-checkbox-checkmark" and @style=""]')))
			print_as_log("Captcha solved successfully!")
			browser.switch_to.default_content()
		except:
			print_as_log(colored("Captcha not solved! Exiting...", "red"))
			browser.quit()
			exit()

		claim_btn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
		claim_btn.click()
		print_as_log(colored("= New claim triggered =", 'white', 'on_green'))
		ok_btn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//button[@class="swal-button swal-button--confirm"]')))
		ok_btn.click()
		time.sleep(5)
		balance_field = browser.find_element(By.ID, "balance")
		print_as_log(colored(f"Balance: ${balance_field.text}", 'cyan', attrs=['bold']))

		for i in tqdm(range(300), bar_format='{l_bar}{bar}|{remaining}', leave=False):
			time.sleep(1)
		print_as_log("Preparing for new claim...")
		browser.refresh()
		time.sleep(5)