import random
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import os
import random
import threading
import imaplib
import email
import urllib.request
from email.header import decode_header
import webbrowser
import os
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path
def alias(driver):
    outset = 0
    for i in range(10):
        time.sleep(10)
        driver.find_element_by_xpath("//a[@id='idAddAliasLink']").click()
        time.sleep(15)
        with open(r'data\firstnames.txt') as fn:
            firsts = fn.readlines()
        l=[]
        for i in range(0,len(firsts)-1):
            x=firsts[i]
            z=len(x)
            a=x[:z-1]
            l.append(a)
        l.append(firsts[i+1])
        FirstName=random.choice(l)
        with open(r'data\lastnames.txt') as ln:
            lasts = ln.readlines()
        l=[]
        for i in range(0,len(lasts)-1):
            x=lasts[i]
            z=len(x)
            a=x[:z-1]
            l.append(a)
        l.append(lasts[i+1])
        LastName=random.choice(l)
        with open(r'input\password.txt') as ps2:
            ps2 = ps2.readline()
            ps2=ps2.split("['")[0]
        username = FirstName + LastName
        time.sleep(4)
        if(driver.find_elements_by_xpath("//option[@value='outlook.com']")):
            driver.find_element_by_xpath("//option[@value='outlook.com']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//input[@id='AssociatedIdLive']").send_keys(username)
        time.sleep(4)
        driver.find_element_by_xpath("//input[@id='SubmitYes']").click()
        time.sleep(4)
        if(driver.find_elements_by_xpath("//div[@id='iAddErrorLive']")):
            time.sleep(4)
            driver.find_element_by_xpath("//input[@id='AssociatedIdLive']").clear()
            with open(r'data\firstnames.txt') as fn:
                firsts = fn.readlines()
            l=[]
            for i in range(0,len(firsts)-1):
                x=firsts[i]
                z=len(x)
                a=x[:z-1]
                l.append(a)
            l.append(firsts[i+1])
            FirstName=random.choice(l)
            with open(r'data\lastnames.txt') as ln:
                lasts = ln.readlines()
            l=[]
            for i in range(0,len(lasts)-1):
                x=lasts[i]
                z=len(x)
                a=x[:z-1]
                l.append(a)
            l.append(lasts[i+1])
            LastName=random.choice(l)
            username = FirstName + LastName
            if(driver.find_elements_by_xpath("//option[@value='outlook.com']")):
                driver.find_element_by_xpath("//option[@value='outlook.com']").click()
            time.sleep(4)
            driver.find_element_by_xpath("//input[@id='AssociatedIdLive']").send_keys(username)
            time.sleep(4)
            driver.find_element_by_xpath("//input[@id='SubmitYes']").click()
            time.sleep(4)
            if(driver.find_elements_by_xpath("//div[@id='iAddErrorLive']")):
                time.sleep(4)
                driver.find_element_by_xpath("//input[@id='AssociatedIdLive']").clear()
                with open(r'data\firstnames.txt') as fn:
                    firsts = fn.readlines()
                l=[]
                for i in range(0,len(firsts)-1):
                    x=firsts[i]
                    z=len(x)
                    a=x[:z-1]
                    l.append(a)
                l.append(firsts[i+1])
                FirstName=random.choice(l)
                with open(r'data\lastnames.txt') as ln:
                    lasts = ln.readlines()
                l=[]
                for i in range(0,len(lasts)-1):
                    x=lasts[i]
                    z=len(x)
                    a=x[:z-1]
                    l.append(a)
                l.append(lasts[i+1])
                LastName=random.choice(l)
                username = FirstName + LastName
                if(driver.find_elements_by_xpath("//option[@value='outlook.com']")):
                    driver.find_element_by_xpath("//option[@value='outlook.com']").click()
                time.sleep(4)
                driver.find_element_by_xpath("//input[@id='AssociatedIdLive']").send_keys(username)
                time.sleep(4)
                driver.find_element_by_xpath("//input[@id='SubmitYes']").click()
                time.sleep(4)
                driver.find_element_by_xpath("//odiv[@class='mectrl_header']").click()
                driver.get("https://login.live.com/logout")
        emailytu = username + "@outlook.com:"+ps2
        with open('emails+aliases.txt', 'a+') as file:
            file.write("\n" + emailytu)
        with open("emails+aliases.txt","r") as f:
                lines=f.readlines()
        with open("emails+aliases.txt","w") as f:
            [f.write(line) for line in lines if line.strip() ]
        time.sleep(4)
def imap(driver):
    time.sleep(4)
    with open(r'input\password.txt') as ps2:
        ps2 = ps2.readline()
        ps2=ps2.split("['")[0]
    with open(r'input\recupemail.txt', "r") as recem:
        recems = recem.readlines()
        r=[]
        for i in range(0,len(recems)-1):
            x=recems[i]
            z=len(x)
            a=x[:z-1]
            r.append(a)
        r.append(recems[i+1])
        recemchose=random.choice(r)
    with open(r'input\recupemail.txt', "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if recemchose not in i:
                f.write(i)
        f.truncate()
    email_user=recemchose.split(":")[0]
    email_pass=recemchose.split(":")[1]
    driver.find_element_by_xpath("//input[@id='EmailAddress']").send_keys(email_user)
    time.sleep(4)
    driver.find_element_by_xpath("//input[@id='iNext']").click()
    time.sleep(20)
    mail = imaplib.IMAP4_SSL('outlook.office365.com')
    mail.login(email_user, email_pass)
    mail.select()
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
    codesec = str(email_message).split("Security code: ", 1)[1].split("If", 1)[0]
    codesec = str(codesec)
    driver.find_element_by_xpath("//input[@id='iOttText']").send_keys(codesec)
    time.sleep(4)
    driver.find_element_by_xpath("//img[@class='tile-img']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name='ProofConfirmation']").send_keys(email_user)
    driver.find_element_by_xpath("//input[@id='idSubmit_SAOTCS_SendCode']").click()
    time.sleep(20)
    mail = imaplib.IMAP4_SSL('outlook.office365.com')
    mail.login(email_user, email_pass)
    mail.select()
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
    codesec = str(email_message).split("Security code: ", 1)[1].split("If", 1)[0]
    codesec = str(codesec)
    driver.find_element_by_xpath("//input[@name='otc']").send_keys(codesec)
    time.sleep(12)
    driver.find_element_by_xpath("//a[@id='iCancel']").click()
    time.sleep(10)
    alias(driver)
def emailio():
    with open(r'data\firstnames.txt') as fn:
        firsts = fn.readlines()
    l=[]
    for i in range(0,len(firsts)-1):
        x=firsts[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(firsts[i+1])
    FirstName=random.choice(l)
    with open(r'data\lastnames.txt') as ln:
        lasts = ln.readlines()
    l=[]
    for i in range(0,len(lasts)-1):
        x=lasts[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(lasts[i+1])
    LastName=random.choice(l)
    username = FirstName + LastName
    with open(r'input\password.txt') as ps2:
        ps2 = ps2.readline()
        ps2=ps2.split("['")[0]
    month = random.randint(1,12)
    day = random.randint(13,28)
    year = random.randint(1960,1998)
    unleash = 0
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1,725")
    chrome_options.add_argument("--disable-setuid-sandbox")
    if (os.stat(r'input\proxies.txt').st_size != 0):
        prox = Proxy()
        with open(r'input\proxies.txt') as pr:
            proxies = pr.readlines()
        p=[]
        for i in range(0,len(proxies)-1):
            x=proxies[i]
            z=len(x)
            a=x[:z-1]
            p.append(a)
        p.append(proxies[i+1])
        ip=random.choice(p)
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = ip
        prox.ssl_proxy = ip
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(r'data\ab.crx')
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--disable-setuid-sandbox")
    if (os.stat(r'input\proxies.txt').st_size != 0):
        driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://signup.live.com/signup")
    time.sleep(4)
    driver.find_element_by_xpath("//a[@id='liveSwitch']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//a[@id='easiSwitch']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//a[@id='liveSwitch']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//select[@id='LiveDomainBoxList']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//option[@value='outlook.com']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='MemberName']").send_keys(username)
    time.sleep(4)
    driver.find_element_by_xpath("//input[@id='iSignupAction']").click()
    time.sleep(8)
    driver.find_element_by_xpath("//input[@id='PasswordInput']").send_keys(ps2)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='iSignupAction']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='FirstName']").send_keys(FirstName)
    driver.find_element_by_xpath("//input[@id='LastName']").send_keys(LastName)
    driver.find_element_by_xpath("//input[@id='iSignupAction']").click()
    time.sleep(4)
    driver.find_elements_by_xpath("//option[@value='"+str(month)+"']")[0].click()
    time.sleep(2)
    driver.find_element_by_xpath("//option[@value='"+str(day)+"']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//option[@value='"+str(year)+"']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='iSignupAction']").click()
    gud = 0
    time.sleep(6)
    img = driver.find_element_by_xpath("//img[contains(@aria-label, 'Visual')][contains(@aria-label, 'Challenge')]")
    src = img.get_attribute('src')
    with open(r"data\nb.txt", 'r+') as capn:
        nbvalue = int(capn.read())

        nbvalue = nbvalue +1
        capn.seek(0)
        capn.truncate()
        capn.write(str(nbvalue))
    with open(r"data\captchaadress.txt", 'a+') as cap:
        cap.write(src +" / "+ str(nbvalue)+"\n")
    while True:
        with open(r"data\captchavalue.txt") as capad:
            linescapad = capad.readlines()
            searchcap = "/"+str(nbvalue)
            for line in linescapad:
                if (searchcap in line):
                    capfinal = line.split("/")[0]
                    print(capfinal)
                    gud = 1
        if(gud==1):
            break
    driver.find_element_by_xpath("//input[@type='text']").send_keys(capfinal)
    driver.find_element_by_xpath("//input[@id='iSignupAction']").click()
    element = WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "//a[@id='help-links-msa-info']")))
    emailwr= username+ "@outlook.com"
    with open(r'output\emails.txt', 'a+') as file:
        file.write("\n" + emailwr + ":"+ ps2)
    with open(r'output\emails.txt',"r") as f:
            lines=f.readlines()
    with open(r'output\emails.txt',"w") as f:
        [f.write(line) for line in lines if line.strip() ]
    with open(r'output\emails+aliases.txt', 'a+') as file:
        file.write("\n" + emailwr + ":"+ ps2)
    with open(r'output\emails+aliases.txt',"r") as f:
            lines=f.readlines()
    with open(r'output\emails+aliases.txt',"w") as f:
        [f.write(line) for line in lines if line.strip() ]
    driver.get("https://outlook.live.com/owa/")
    element = WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "//span[@data-automationid='splitbuttonprimary']")))
    driver.get("https://account.microsoft.com/profile/")
    element = WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "//a[@cms-link='$ctrl.links.personalManageEmail']")))
    time.sleep(4)
    element.click()
    time.sleep(10)
    driver.find_element_by_xpath("//option[@value='Email']").click()
    imap(driver)
emailio()
