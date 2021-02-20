# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #error handling
from selenium.common.exceptions import TimeoutException #timeout if not found
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# initialise chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = r"C:\chromedriver.exe"
univ=[]
# check for universitites according to alphabetical order
for j in range(2,28):

    y=f'https://www.4icu.org/reviews/index{j}.htm'
    driver = webdriver.Chrome('C:\\Users\\Saurav Telge\\chromedriver.exe')
    driver.get(y)
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 250)
    # count the number of universities on the page
    cnt= driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/table/tbody").get_attribute("outerHTML")
    count1 = cnt.count('<tr>')
    for i in range(1,count1+1):
        # check if the university provides Engineering (Computer/IT engineering)
        button=driver.find_element_by_xpath(f"/html/body/div[1]/div[4]/div/table/tbody/tr[{i}]/td[1]/a")
        ActionChains(driver).move_to_element(button).click(button).perform()
        chk=driver.find_element_by_xpath("/html/body/div[3]/div[5]/div[2]/div[1]/table/tbody/tr[5]/td[3]/i").get_attribute("outerHTML")
        # if the university provides engineering then extract all the details such as country, college name, website, contact number
        if chk.count('d1')==1:
            ctry=driver.find_element_by_xpath("/html/body/div[2]/ol/li[3]/a/span").get_attribute("innerHTML")
            clg=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td/a/span/strong").get_attribute("innerHTML")
            wbs=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td/a").get_attribute("href")
            tele=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/span").get_attribute("innerHTML")
            univ.append([ctry,clg,wbs,tele])
            driver.back()
            WebDriverWait(driver, 100)
        else:
            driver.back()
# sort the list of list according to country names
univ.sort()
# store all the details in a csv
with open("universities.csv", 'w') as myfile:
    for row in univ:
        for x in row:
            myfile.write(str(x) + ',')
        myfile.write('\n')

