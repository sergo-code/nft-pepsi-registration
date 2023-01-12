import undetected_chromedriver as uc
from pepsi.main_page import MainPage
from utils import Human
from time import sleep
from gmail import read_email
from secrets import token_hex


driver = uc.Chrome()
page = MainPage(driver)
page.go_to_site('https://themicdrop.pepsi.com/')
human = Human()
page.start_create_account()
page.fill_in_the_fields(human)
page.end_create_account()
sleep(7)

#Get an activation link from the email
key = True
while key:
    sleep(3)
    link_activation = read_email()
    if link_activation:
        key = False

page.go_to_site(link_activation)

page.set_password(human.password)

sleep(1000)