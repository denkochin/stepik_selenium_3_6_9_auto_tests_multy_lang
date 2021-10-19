import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_add_to_cart_button_visible(browser):
    browser.get(link)
    time.sleep(5)
    btn_add_to_basket = browser.find_element_by_css_selector(".btn-add-to-basket").is_enabled()
    assert btn_add_to_basket, '"Add to cart" button is missing'
