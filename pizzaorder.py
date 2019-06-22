import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import addressA, cityA, zipcodeA, first, last, phone, email

cheese = sys.argv[1]
coke = sys.argv[2]

browser = webdriver.Chrome()
action = webdriver.common.action_chains.ActionChains(browser)
browser.implicitly_wait(30)
browser.get(('https://www.dominos.com/en/'))
browser.get(
    ('https://www.dominos.com/en/pages/order/#!/locations/search/?type=Delivery'))
address = browser.find_element_by_name('Street')
address.send_keys(addressA)
city = browser.find_element_by_name('City')
city.send_keys(cityA)
select = Select(browser.find_element_by_id('Region'))
select.select_by_value('NY')
zipcode = browser.find_element_by_name('Postal_Code')
zipcode.send_keys(zipcodeA)
zipcode.send_keys(u'\ue007')


def pizzaorder():
    button = browser.find_element_by_id('entree-BuildYourOwn').click()
    button2 = browser.find_element_by_css_selector(
        'button.btn.btn--large.js-isNew.js-addPizza.btn--block.c-order-addToOrder').click()
    button3 = browser.find_element_by_css_selector(
        'button.card--overlay__close.js-closeButton')
    browser.get(('https://www.dominos.com/en/pages/order/#!/checkout/'))
    button4 = browser.find_element_by_link_text(
        'No, Go to Checkout').click()
    item = browser.find_element_by_css_selector(
        'input[class="cross-sell-radio"][aria-label="Coke®"]')
    browser.execute_script("arguments[0].click();", item)
    item_buy = browser.find_element_by_css_selector(
        'button.btn.js-isNew')
    browser.execute_script("arguments[0].click();", item_buy)
    browser.get(('https://www.dominos.com/en/pages/order/payment.jsp'))
    firstname = browser.find_element_by_id('First_Name')
    firstname.send_keys(first)
    lastname = browser.find_element_by_id('Last_Name')
    lastname.send_keys(last)
    emailA = browser.find_element_by_id('Email')
    emailA.send_keys(email)
    phonenum = browser.find_element_by_id('Callback_Phone')
    phonenum.send_keys(phone)
    paydelivery = browser.find_element_by_css_selector(
        'input.c-order-payment-cash.js-paymentType')
    browser.execute_script("arguments[0].click();", paydelivery)
    # ONLY IF YOU ARE SERIOUS ABOUT ORDERING
    placeorder = browser.find_element_by_css_selector(
        'button.btn.btn--large.btn--block.submitButton.submitButton--place-order.qa-PcpBu.js-placeOrder.c-order-placeorder')
    browser.execute_script("arguments[0].click();", placeorder)


if __name__ == "__main__":
    pizzaorder()
