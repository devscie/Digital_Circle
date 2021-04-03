import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'./Caso_Uso_2/chromedriver.exe')  # argument, local path
driver.get('https://www.verdemaratevoce.com.br/')

driver.implicitly_wait(10)

enterOk = driver.find_element_by_xpath('//*[@id="largeModal"]/div/div/div[3]/button')
enterOk.click()

driver.implicitly_wait(10)

searchbox = driver.find_element_by_xpath('//*[@id="inputBuscaRapida"]')
searchbox.send_keys('"cerveja Heineken"')

driver.implicitly_wait(10)

searchButton = driver.find_element_by_xpath('/html/body/app-root/app-header/div/div/div/div/div/div[2]/form/button')
searchButton.click()

driver.implicitly_wait(10)

#caption = driver.find_element_by_xpath('/html/body/app-root/app-produto-busca/div/div/div[1]/div/div/app-produto-card/div/div/div[2]/p[1]/a')
#print(caption.text)

#preco = driver.find_element_by_xpath('/html/body/app-root/app-produto-busca/div/div/div[1]/div/div/app-produto-card/div/div/app-tag-preco/div/div[2]')
#print(preco.text)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-produto-busca'))
    )

    precos = main.find_elements_by_tag_name('app-tag-preco')
    for preco in precos:
        infopreco = preco.find_element_by_class_name('info-price')
        print(infopreco.text)
finally:
    driver.quit()