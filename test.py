from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
for x in range(100):
# open Chrome
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);

    driver = webdriver.Chrome(
        'C:/Users/ADMIN/Downloads/chromedriver.exe', options=option  )

    # Open URL
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfv-tBPe0Tf6EqqNYcrgPY9dY_tFHazd56pUW_rkK5o_ecK1A/viewform')

    # wait for one second, until page gets fully loaded
    time.sleep(1)

    """
    from selenium import webdriver

    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    #option.add_argument("--headless") Use this and the following option to run Headless
    #option.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path='/home/srujan/chromedriver', options=option)

    browser.get("https://forms.gle/FoAoauz53Xy7A4n68")

    # Use the following snippets to get elements by their class names
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

    # Use the following snippets to get elements by their XPath
    otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")

    textboxes[0].send_keys("Hello World")

    radiobuttons[2].click()

    checkboxes[1].click()
    checkboxes[3].click()

    submitbutton[0].click()

    #browser.close()

    eBFwI
    """

    # Use the following snippets to get elements by their XPath

    checkboxes1 = driver.find_elements_by_class_name('uVccjd')
    a = random.randint(0,4)
    checkboxes1[a].click()

    checkboxes2 = driver.find_elements_by_class_name('uVccjd')
    b = random.randint(6,8)
    checkboxes2[b].click()

    checkboxes3 = driver.find_elements_by_class_name('uVccjd')
    c = random.randint(10,13)
    checkboxes3[c].click()


    checkboxes2 = driver.find_elements_by_class_name('nWQGrd')
    b = random.randint(0,4)
    checkboxes2[b].click()

    checkboxes3 = driver.find_elements_by_class_name('nWQGrd')
    c = random.randint(5,9)
    checkboxes3[c].click()


    # click on submit button
    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    # fill another response
    another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

    # close the window
    driver.close()



