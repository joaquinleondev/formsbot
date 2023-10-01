from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
from time import sleep

for _ in range(50):
    options = Options()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://forms.gle/xC95yEiS3uVNtyqNA")
    sleep(1)

    age_input = driver.find_element('xpath', "//input[@tabindex='0']")
    age_input.send_keys(randint(18, 70))


    def obtain_label_by_text_content(text_content):
        return driver.find_element('xpath', f"//label[contains(@class, 'docssharedWizToggleLabeledContainer')]["
                                            f".//div[.//div[contains(@class, 'YEVVod')][.//div[.//span[text()["
                                            f"contains(., '{text_content}')]]]]]]")


    sex_options = [obtain_label_by_text_content('Masculino'), obtain_label_by_text_content('Femenino')]

    sex_options[randint(0, 1)].click()

    travel_options = [obtain_label_by_text_content('Colectivo de linea'), obtain_label_by_text_content('Avión'),
                      obtain_label_by_text_content('Auto')]

    travel_options[1].click()

    yes_options = driver.find_elements('xpath', "//label[contains(@class, 'docssharedWizToggleLabeledContainer')]["
                                                ".//div[.//div[contains(@class, 'YEVVod')][.//div[.//span[text()["
                                                "contains(., 'Si')]]]]]]")
    si = driver.find_elements('xpath', "//label[contains(@class, 'docssharedWizToggleLabeledContainer')][.//div["
                                       ".//div[contains(@class, 'YEVVod')][.//div[.//span[text()[contains(., "
                                       "'Sí')]]]]]]")
    finals_yes = [si[0], yes_options[0], yes_options[1], si[1], si[2], yes_options[2]]
    no_options = driver.find_elements('xpath', "//label[contains(@class, 'docssharedWizToggleLabeledContainer')]["
                                               ".//div[.//div[contains(@class, 'YEVVod')][.//div[.//span[text()["
                                               "contains(., 'No')]]]]]]")

    for i in range(6):
        if randint(0, 1) == 0:
            finals_yes[i].click()
        else:
            no_options[i].click()

    submit_button = driver.find_element('xpath', "//span[text()[contains(., 'Enviar')]]")
    submit_button.click()
