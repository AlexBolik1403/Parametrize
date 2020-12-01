import time

def test_guest_should_be_button_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element_by_css_selector("button.btn-add-to-basket")
        result = True
    except:
        result = False
    assert result==True, 'button add to basket not found'

