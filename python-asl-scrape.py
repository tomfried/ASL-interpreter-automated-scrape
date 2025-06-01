import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get('https://myaccount.rid.org/Public/Search/Member.aspx')
driver.maximize_window()
#driver.find_element(By.XPATH, '//#FormContentPlaceHolder_Panel_zipCodeTextBox')
#driver.findElement(By.xpath("//html/body/div[1]/div[3]/div[1]/form/div/div/input")).sendKeys("92101"");
select_element = driver.find_element(By.NAME, 'ctl00$FormContentPlaceHolder$Panel$stateDropDownList')
select = Select(select_element)
options = select.options
#print(len(options))

time.sleep(1)

content = []
content = [["Name", "City", "State", "Zip", "Email", "Phone", "Certificates", "Additional Languages or Specialties", "Category", "Freelance Status"]]

# generate a alert via javascript 
#driver.execute_script("alert('Alert via selenium')")
#time.sleep(5)

# For each state in dropdown
for i in range(1,len(options)):
    if i < 58:
        continue
    if i != 1:
        select_element = driver.find_element(By.NAME, 'ctl00$FormContentPlaceHolder$Panel$stateDropDownList')
        select = Select(select_element)
        options = select.options
    state_name = options[i].text
    #print(options[i].text)
    if i != 1:
        select_element = driver.find_element(By.NAME, 'ctl00$FormContentPlaceHolder$Panel$stateDropDownList')
        select = Select(select_element)
        options = select.options
    if "Armed" in state_name:
        continue
    select.select_by_visible_text(state_name)
    time.sleep(1)
    driver.find_element(By.ID, 'FormContentPlaceHolder_Panel_searchButtonStrip_searchButton').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)

    # Calculate total results
    result_count = ""
    if driver.find_elements(By.CSS_SELECTOR, 'tr.EmptyRowStyle'):
        result_count = "0"
    else:
        try:
            result_count = driver.find_element("xpath", "//*[contains(text(), ' items in ')]").text
        except:
            result_count = driver.find_element("xpath", "//*[contains(text(), ' item in ')]").text
    result_count = result_count.split(" ")
    if len(result_count) > 2:
        items = int(result_count[0])
        pages = int(result_count[3])
    else:
        items = 0
        pages = 0
    print(state_name + " has " + str(items) + " Items and " + str(pages) + " Pages.")

    # for each page in pagination
    for page_id in range(1, pages + 1, 1):
        #print(str(page_id))
        if page_id != 1:
            driver.execute_script("__doPostBack('ctl00$FormContentPlaceHolder$Panel$resultsGrid','Page$" + str(page_id) + "')")
            #__doPostBack('ctl00$FormContentPlaceHolder$Panel$resultsGrid','Page$11')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')#, from_encoding="iso-8859-8")
        rows = soup.find_all("tr", {"class": "RowStyle"})
        cells = []

        # for each table row on page
        for tr in rows:
            children = tr.findChildren("td" , recursive=False)
            row_index = len(content)
            temp_array = []
            # for each table cell on row. Add text together to make CSV
            for td in children:
                cell = ''.join(td.get_text().split())
                temp_array.append(cell)
            #print(temp_array)
            content.append(temp_array)

        with open('output.csv','w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            #for item in cells:
            #    wr.writerow([item])
            wr.writerows(content)
    #break

driver.quit();
