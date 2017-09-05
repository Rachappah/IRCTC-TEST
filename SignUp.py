'''
Created on 24/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class SignUp(object):
    url="https://www.irctc.co.in/eticketing/userSignUp.jsf"
    submit=".//*[@id='userRegistrationForm:checkavail']"
    fname=".//*[@id='userRegistrationForm:userName']"
    pwd=".//*[@id='userRegistrationForm:password']"
    cpwd=".//*[@id='userRegistrationForm:confpasword']"
    select=".//*[@id='userRegistrationForm:securityQ']"
    pawd=".//*[@id='userRegistrationForm:password']"
    cpwdd=".//*[@id='userRegistrationForm:confpasword']"
    selectt=".//*[@id='userRegistrationForm:securityQ']"
    answer=".//*[@id='userRegistrationForm:securityAnswer']"
    unmaried=".//*[@id='userRegistrationForm:maritalStatus:1']"
    adharcard=".//*[@id='userRegistrationForm:uidno']"
    email=".//*[@id='userRegistrationForm:email']"
    flat=".//*[@id='userRegistrationForm:address']"
    #state="userRegistrationForm:statesName"
    button=".//*[@id='userRegistrationForm:j_idt489']"
    '''
    classdocs
    '''


    def __init__(self):
        self.driver=webdriver.Firefox()

    def launchSign(self):
        self.driver.get(self.url)
        time.sleep(5) 
        self.driver.find_element_by_xpath(self.submit).click()
        time.sleep(10)
        #alert
        alert=self.driver.switch_to_alert()
        alert.accept()
    def firstName(self):
        self.driver.find_element_by_xpath(self.fname).send_keys("Rachappa")
        time.sleep(3)
    def launchPassword(self):    
        self.driver.find_element_by_xpath(self.pwd).send_keys("Rachappa22")
        self.driver.find_element_by_xpath(self.cpwd).send_keys("rach")
        self.driver.find_element_by_xpath(self.select).click()
        time.sleep(3)
        Alert=self.driver.switch_to_alert()
        Alert.accept()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.pawd).send_keys("Rachappa22")
        time.sleep(5)
        self.driver.find_element_by_xpath(self.cpwdd).send_keys("Rachappa22")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.selectt).click()
        time.sleep(3)
        #select the single element in lists
        e2=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:securityQ']")
        e2.click()
        e2.send_keys("What is your all time favorite sports team?")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.answer).send_keys("India")
        time.sleep(3)
        #select language
        e3 = self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:prelan']")
        e3.click()
        e3.send_keys("English")
        #select name details 
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:firstName']").send_keys("rachappa")
        time.sleep(4)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:middleName']").send_keys("rachu")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:lastName']").send_keys("halinge")
        time.sleep(3)
        #launch gender
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:gender:0']").click()
        time.sleep(3)
    def launchUnmaried(self):
        self.driver.find_element_by_xpath(self.unmaried).click()
        time.sleep(3)
        element=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:dobDay']")
        element.click()
        element.send_keys("12")
        time.sleep(3)
        element=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:dobMonth']")
        element.click()
        element.send_keys("DEC")
        element=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:dateOfBirth']")
        element.click()
        element.send_keys("1990")
        e1=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:occupation']")
        e1.click()
        e1.send_keys("Professional")
        time.sleep(3)
    def launcDetails(self):
        self.driver.find_element_by_xpath(self.adharcard).send_keys("661492193797")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:idno']").send_keys("BREPR2464P") 
        time.sleep(3)
        self.driver.find_element_by_xpath(self.email).send_keys("Rachappahalinge@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:mobile']").send_keys("7353249488")
        #select the nationaliti in lists
        element=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:nationalityId']")
        element.click()
        element.send_keys("India")
        time.sleep(3)
    def launchResidental(self):
        self.driver.find_element_by_xpath(self.flat).send_keys("389/10") 
        time.sleep(4)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:street']").send_keys("14th cross vijayanagar")   
        time.sleep(4)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:area']").send_keys("Vijayanagar/Bangalore")
        time.sleep(8)
        #select country
        e4=self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:countries']")
        e4.click()
        e4.send_keys("India")
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:pincode']").send_keys("560040") 
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:landline']").send_keys("7353249488")
        time.sleep(3)
        #self.driver.find_elements_by_id("captcha").send_keys("")
        #time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='userRegistrationForm:irctcsbicard:0']").click()
        time.sleep(3)
    def launchButton(self):
        self.driver.find_element_by_xpath(self.button).click()
        time.sleep(3)
        alert=self.driver.switch_to_alert()
        alert.accept() 
        time.sleep(3)
        #select the city
        element=self.driver.find_element_by_id("userRegistrationForm:cityName")
        element.click()
        element.send_keys("Bangalore")
        time.sleep(3)
        #select postoffice
        element=self.driver.find_element_by_id("userRegistrationForm:postofficeName")
        element.click()
        element.send_keys("---- Select a Post Office ----")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.button).click()
        time.sleep(3)
        alert=self.driver.switch_to_alert()
        alert.accept() 
        #<input type="image" alt="" src="/user/captcha" id="captcha" name="captcha">
           
        
   
        
        
        
        
        
        
            
        
