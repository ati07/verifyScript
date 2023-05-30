# This is a sample Python script.
# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver


# driver = webdriver.Chrome()
#
# driver.get("https://verifi-one.visa.com/vdm/")
# time.sleep(30)
# url2 = driver.execute_script("return document.documentElement.outerHTML")
# soup1 = BeautifulSoup(url2,'lxml')
# print(soup1)
#
# soup1.find('input',)
# driver.quit()
# import asyncio
from playwright.sync_api import sync_playwright
# from playwright.async_api import async_playwright
import pandas as pd
from pymongo.mongo_client import MongoClient
# import csv

def main():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://verifi-one.visa.com/vdm/")

    page.fill('input#orgId','chargebackprolatamincpid')
    page.fill('input#username','jeankra')
    page.fill('input#password','Panama2023!')
    page.click('button[type=submit]')
    page.is_visible('div.vds-input-bar')
    page.wait_for_timeout(5000)
    # html = page.inner_html('#cybs-ui')
    # soup1 = BeautifulSoup(html, 'lxml')
    page.goto('https://verifi-one.visa.com/vdm/app/vdmCaseActivity')
    # page.wait_for_timeout(5000)
    page.is_visible('button.vds-btn-icon.vds-btn-icon--light-tiny.css-1pf6dds')
    # page.locator('#MqyT7bfajgW').click()
    page.click('#main > div:nth-child(3) > div:nth-child(1) > div.css-6x9632-CSS-CSS > div > div > div > div.css-xa13nd-CSS-CSS-structPadding-dark > div.css-1f6bywb-CSS-CSS > div > div:nth-child(3) > div > div:nth-child(1) > div > div > div > button')
    page.is_visible("#custom-list-item-0-5")
    page.click('#custom-list-item-0-5')
    page.is_visible("//html/body/div[1]/div[2]/div/div[2]/main/div[2]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/fieldset/div/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/input")
    # page.is_visible("input#input-t91JaBuabze")
    # page.wait_for_timeout(5000)
    # page.get_by_role('input',name="Start Date (MM/DD/YYYY)").fill('05/26/2023')
    page.fill('//html/body/div[1]/div[2]/div/div[2]/main/div[2]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/fieldset/div/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/input', '05/26/2023')
    # page.fill('input#input-t91JaBuabze', '05/26/2023')
    page.click('#main > div:nth-child(3) > div:nth-child(1) > div.css-6x9632-CSS-CSS > div > div > div > div.css-zn1cdn-structPadding-structPadding-structPadding > div > div > button.vds-btn-text--primary.css-118k6bc-smallViewportStyles-highContrastStyles-highContrastStyles-structMargin-structMargin')
    page.locator('//*[@id="template-main"]/div/div[1]/div[2]/div/button').click()
    page.is_visible('//*[@id="react-aria-modal-dialog"]/div/div[3]/div/div/div/button[1]')
    page.locator('//*[@id="react-aria-modal-dialog"]/div/div[3]/div/div/div/button[1]').click()
    page.on("download", lambda download: download.save_as("C:/Users/atiur/PycharmProjects/verifyScript/newData.xlsx"))
    # print(download.path())
    # input-zaL0_Nz72xn
    # input-zaL0_Nz72xn
    page.wait_for_timeout(5000)

    # print(soup1)
    # print("wow",page.title())

    # browser.close()
main()
file_name = r"newfile.csv"
# opening the CSV file
# with open('./file.csv', mode='r',encoding="cp437", errors='ignore') as file:
#    # reading the CSV file
#    csvFile = csv.reader(file)
#
#    # displaying the contents of the CSV file
#    for lines in csvFile:
#       print(lines)
# df = pd.read_csv(file_name, sep='|', encoding='ISO-8859-1')
# csv_file = open(file_name, newline='', encoding='ISO-8859-1')
#
# csv_reader = list(csv.reader(csv_file, delimiter='|'))

# [['first_name', 'last_name'], ['Alice', 'Smith'], ['Bobby', 'Hadz']]
# print(csv_reader)
df = pd.read_excel('./newData.xlsx')
# print('df',df.columns)
keys=[]
for col in df.columns:
    keys.append(col)
    # print(col)
data = df.values.tolist()
print('keys',keys)
print('df',df.values.tolist())
objData =[]
for j in data:
    objData.append({
        keys[0]:j[0],
        keys[1]: j[1],
        keys[2]: j[2],
        keys[3]: j[3],
        keys[4]: j[4],
        keys[5]: j[5],
        keys[6]: j[6],
        keys[7]: j[7],
        keys[8]: j[8],
        keys[9]: j[9],
    })
print('objData',objData)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://testUser:test123@cluster0.bq15jz4.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print('clinet',client.list_database_names())
    db = client['test']
    dbCollection= db['rdrs']
    dbCollection.insert_many(objData)
    print('clinetDB',)

except Exception as e:
    print(e)

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')
# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
