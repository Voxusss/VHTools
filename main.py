import random
import csv
import eel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import subprocess
import random
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import traceback
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
eel.init("web")
captchaIndex = 0
with open("nb.txt", 'r+') as capn:
    capn.write("0")
with open("captchavalue.txt", 'r+') as capv:
    capv.seek(0)
    capv.truncate()
@eel.expose
def writecaptchavalue(captchaValue, captchaValueIndex):
    with open("captchavalue.txt", "a+") as capvalue:
        if (captchaValueIndex != 0):
            capvalue.write(str(captchaValue)+"/"+str(captchaValueIndex)+"\n")
def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      pass
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay
@eel.expose
def updateCapIndex():
    global captchaIndex
    captchaIndex = captchaIndex+1
lineurlindex = ''
settedaf = 0
def wala():
    nbcaptchas = 0
    urlimg = ""
    with open("captchaadress.txt", "r") as capa:
        if (os.stat("captchaadress.txt").st_size != 0):
            global settedaf
            if(settedaf==0):
                eel.setaffiched()
                settedaf = 1
            global lineurlindex
            lineurlindex = capa.readlines()[captchaIndex]
            urlimg=lineurlindex.split(" /")[0]
            indexCaptcha = lineurlindex.split("/ ")[1]
            eel.captchahar(urlimg)
    with open("captchaadress.txt", "r") as capa:
        for line in capa:
            nbcaptchas = nbcaptchas+1
        eel.updateCaptchaNb(nbcaptchas)
with open("captchaadress.txt", 'r+') as cap:
    cap.seek(0)
    cap.truncate()
threading.Thread(target=lambda: every(1, wala)).start()
def emaily(emailRange):
    for i in range(emailRange):
        subprocess.Popen(["python.exe", 'emailt.py'])
@eel.expose
def goemail(emailRange):
    emailRange = int(emailRange)
    emaily(emailRange)
if (__name__ == "__main__"):
    with open ('data\data.vextools', 'r') as data:
        data = data.read()
        finished = data.split("= ")[1]
        finished = finished.split("i")[0]
        finished = int(finished)
        ignored = data.split("= ")[2]
        ignored = ignored.split("t")[0]
        ignored = int(ignored)
        total = data.split("= ")[3]
        total = int(total)
@eel.expose
def telgo(country, rangetel):
    for i in range (int(rangetel)):
        tel(country)
@eel.expose
def tel(country):
    if country == 'France':
        randNumber = random.randint(10000000,99999999)
        prefix = 336
        phoneNumber = "+"+ str(prefix)+str(randNumber)
        with open('phone_out.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([phoneNumber])
    if country == 'United Kingdom':
        randNumber = random.randint(100000000,999999999)
        prefix = 447
        phoneNumber = "+"+ str(prefix)+str(randNumber)
        with open('phone_out.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([phoneNumber])
    if country == 'United States':
        randNumber = random.randint(100000,999999)
        prefix = 1
        areacode = random.randint(201,219)
        phoneNumber = "+"+ str(prefix)+str(areacode)+str(randNumber)
        with open('phone_out.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([phoneNumber])
@eel.expose
def go(rangeGo):
    global finished
    global ignored
    global total
    total = int(rangeGo) + total
    for i in range (int(rangeGo)):
        main()
    ignored = total - finished
    eel.output(finished, ignored)
    with open ('data\data.vextools', 'w') as data:
        strfinished = "finished = "+str(finished)+ "\n"
        strignored = "invalid = "+str(ignored)+ "\n"
        strtotal = "total = "+str(total) + "\n"
        data.writelines([strfinished,strignored,strtotal])
@eel.expose
def add(one,two):
    print(one,two)
    result = int(one)+int(two)
    return result
@eel.expose
def minus(one,two):
    print(one,two)
    result = int(one)-int(two)
    return result
def main():
    adressesIndex = random.randint(1,17)
    adressLink = r'Adresses\adresses'+str(adressesIndex)+'.csv'
    with open(adressLink, 'r') as file:
        reader = csv.reader(file)
        count = 0
        wanted = 10
        chosen_row = random.choice(list(reader))
        string = chosen_row[0]
        adresse1 = string.split(';;')[1]
        adresse1 = adresse1.split(';')[0]
        number = string.split(';')[2]
        number = number.split(';')[0]
        adresse = number + " " +adresse1
        cp = string.split(';')[5]
        ville = string.split(';')[7]
        country = "France"
        index = len(adresse)
        region = ""
        if index > 4:
            with open("regions.txt", 'r+') as fileuiop:
                for line in fileuiop:
                    print("oeoeoeooeoe")
                    lineid = line.split(":")[0]
                    if(lineid in cp[:2]): region = line.split(":")[1]
                    print(region)
            print(adresse, cp, ville, country, region)
            global finished
            finished = finished + 1
            print(finished)
            with open('adresse_out.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([adresse, cp, ville, country, region])
            with open('adresse_out.csv', 'r+', newline='') as file:
                data = file.read()
                data = data.replace('"', '')
                lines = data.split("\n")
                non_empty_lines = [line for line in lines if line.strip() != ""]
                string_without_empty_lines = ""
                for line in non_empty_lines:
                    string_without_empty_lines += line + "\n"
                file.seek(0)
                file.truncate(0)
                file.write(string_without_empty_lines)
@eel.expose
def init():
    eel.output(finished, ignored)
if (__name__ == "__main__"):
    eel.start('address.html', port=0, size=(1200,600))
