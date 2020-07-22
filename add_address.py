from selenium import webdriver
import time
from random import randint
from details import *
import sys


for j in username:
    print(j)

#change this for first name acc. to your need
    First_Name_=['Aman','Siyaal','Manav','Brijesh','Bablu','Anika','Anamika','Akshita','Mannu','Nimit','Namrata','Sajjan','Binder','Charika','Chameli','Diksha','Drigesh','Emaan','Fakhtar','Faman','Golu','Harshit','Hemant']
#change this for surname name acc. to your need
    Surname_=[ 'Arora','Ameen','Bhateja','Bhatia','Chaurasia','Chetak','Daman','Dirgam','Mahajan','Mehta','Ankiteshwar','Sood','Pathak','Saifi','Puri','Sidana','Garg','Bansal','Aggarwal']

    final_name=First_Name_[randint(0,len(First_Name_)-1)] + ' '+ Surname_[randint(0,len(Surname_)-1)]
#change this for Area acc. to your need
    Area_=['Model Town','New Model Town','Old Model Town','Model Town Area','Model Town Post Office','Model Town Stadium']

    area=Area_[randint(0,len(Area_)-1)]

    House_=['H. No','House Number','H. Number','Flat No.','Flat number','Apartment No.','Apt. No.','Home No.']

    house=House_[randint(0,len(House_)-1)]

#change this for Address acc. to your need
    Address_=['PVR Cinemas Parking Gate','Golu Chicken Shop','Malhotra Food Services','Gali No. 76 opposite Mansarovar','Street Pin Number 34','Bosa ram Chowk','khajoor waali gali','Peepal ka ped aashram','Grand Plaza Hotel Shop','Reveira Furnishing Houses','Matrix Private Ltd. factory','Troops of pubg shops','Mankatangal Broom and Shops','Shiketan Grocery Store','Smile Dental Clinic Doctors','OnePlus Service Center','Samsung Mobile Repair Shop','Vivo Oppo Panipat Main Branch','SBI Bank Branch Panipat','ICICI Home Loan Solutions']

    address = Address_[randint(0,len(Address_)-1)]

#change this for landmark acc. to your need
    Landmark_=['Mangal Kesri Bhawan','Labour Chowk Point','Books n brew cafe','Trimank Cooler Repair','AC shop ogeneral and voltas','Khidki Pasand boutique','Mehak Beauty Parlour','Manan Bump House','Trikona Book Point','Pet Care Shop','Laptop and PC center','IITJEE Mains Coaching','Srimani Tent Service','Aakash Institution And Center','Advanced CAA Papers','Modi Panipat Shop','Patanjali Ayurvedic Store','Taminder Paaji di shop','Cafe Hub Point','Sector Number Plates']
#change this if you need some specfic code in your landmark
    final_landmark='Harshitabad ' + Landmark_[randint(0,len(Landmark_)-1)]
    near_=["near" , 'besides','opposite to','nearby']
    near=near_[randint(0,len(near_)-1)]
#change this for Address acc. to your need
    Address1=['PVR Cinemas Parking Gate','Golu Chicken Shop','Malhotra Food Services','Gali No. 76 opposite Mansarovar','Street Pin Number 34','Bosa ram Chowk','khajoor waali gali','Peepal ka ped aashram','Grand Plaza Hotel Shop','Reveira Furnishing Houses','Matrix Private Ltd. factory','Troops of pubg shops','Mankatangal Broom and Shops','Shiketan Grocery Store','Smile Dental Clinic Doctors','OnePlus Service Center','Samsung Mobile Repair Shop','Vivo Oppo Panipat Main Branch','SBI Bank Branch Panipat','ICICI Home Loan Solutions']

    address1 = Address1[randint(0,len(Address1)-1)]
#change this for pincode acc. to your need
    final_pincode='272003'

    final_area='Bahadurpur aksada chowraha ' + house + ' '+ str(randint(10,99)) + '/' + str(randint(100,999))  + ' ' + near + ' ' + address  + ' ' +  final_landmark

    final_locality= area + ' '+ address1

    final_email = ''
    for i in range(10):
        final_email +=chr(randint(97,122))
    final_email += str(randint(10,99))+ chr(randint(97,122)) + chr(randint(97,122)) + '@gmail.com'


    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    browser=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options=chrome_options)
    browser.get('https://www.flipkart.com/')
    time.sleep(5)
    mobile=browser.find_elements_by_css_selector('body > div.mCRfo9 > div > div > div > div > div.Km0IJL.col.col-3-5 > div > form > div:nth-child(1) > input')
    mobile[0].send_keys(j)
    password=browser.find_elements_by_css_selector('body > div.mCRfo9 > div > div > div > div > div.Km0IJL.col.col-3-5 > div > form > div:nth-child(2) > input')
    password[0].send_keys(passs)
    sumbit=browser.find_elements_by_css_selector('body > div.mCRfo9 > div > div > div > div > div.Km0IJL.col.col-3-5 > div > form > div._1avdGP > button')
    sumbit[0].click()

    time.sleep(4)

    browser.get('https://www.flipkart.com/account/addresses')

    time.sleep(5)
    try:
        address=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > button')
        address[0].click()
    except:
        print('Some error occured checking next number')
        browser.quit()
        continue

    time.sleep(3)

    name=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div:nth-child(2) > div:nth-child(1) > input')
    name[0].send_keys(final_name)

    phone=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div:nth-child(2) > div:nth-child(2) > input')
    phone[0].send_keys(username)

    pincode=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div:nth-child(3) > div:nth-child(1) > input')
    pincode[0].send_keys(final_pincode)
    time.sleep(0.7)

    locality=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div:nth-child(3) > div:nth-child(2) > input')
    locality[0].send_keys(final_locality)

    area=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div.uK6xOa._3g_m0J > div > div._2mJu7M.Th26Zc > textarea')
    area[0].send_keys(final_area)

    landmark=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div:nth-child(6) > div:nth-child(1) > input')
    landmark[0].send_keys(final_landmark)

    home=browser.find_elements_by_css_selector('#container > div > div._1VD0UF > div > div._5tT1ZC > div > div > div > div._1yf-9T > div > div > form > div > div._3XXwRR > div > div > label:nth-child(1) > div._6ATDKp')
    home[0].click()
    time.sleep(0.5)

    save=browser.find_elements_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[8]/button[1]')
    save[0].click()


    time.sleep(2)

    browser.get('https://www.flipkart.com/i-kall-k65/p/itm2985be6588cfb?pid=MOBFN6R2WNH6XBHZ&lid=LSTMOBFN6R2WNH6XBHZXQLFNH&marketplace=FLIPKART&srno=s_1_4&otracker=search&otracker1=search&fm=SEARCH&iid=en_7iO3fkAvt6TLBM3jJlKTiyPfrmdTt99hvwPGwbzX3dHhYKiI3V8QoR%2FMSY3zmL%2Fypm6suBfQbwxMG0%2FcK2jcew%3D%3D&ppt=sp&ppn=sp&ssid=0z8o1hif340000001595421326501&qH=eb4af0bf07c16429')
    time.sleep(3)
    try:
        buy_now=browser.find_elements_by_class_name("_279WdV")
        buy_now[0].click()

    except:
        print('Some error occured checking next number')
        browser.quit()
        continue



    time.sleep(5)
    try:
        email=browser.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[2]/span[1]/form/input')
        email[0].send_keys(final_email)
        continue_button=browser.find_elements_by_id('to-payment')
        time.sleep(1)
        continue_button[0].click()
    except :
        print('Some error occured checking next number')
        browser.quit()
        continue

    time.sleep(3)

    browser.get('https://www.flipkart.com/viewcart?otracker=Cart_Icon_Click')

    time.sleep(3)

    remove=browser.find_elements_by_css_selector('#container > div > div._5wt5ag > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div._3cto0P._2Mq1yq > div._3IO2ev._2K02N8._2x63a8 > div:nth-child(2)')
    try:
        remove[0].click()
    except:
        print('Some error occured checking next number')
        browser.quit()
        continue

    time.sleep(3)

    remove1=browser.find_elements_by_css_selector('#container > div > div._2ZtSUF._1xrsaD > div > div.row.LFy2Lc > div > div.gdUKd9._3Z4XMp._2nQDKB')
    remove1[0].click()


    print('Adress and email both are saved')
    time.sleep(3)
    browser.quit()
