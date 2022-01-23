!pip install selenium
!pip install webdriver_manager
!pip install telegram_send
!apt-get update
!apt install chromium-chromedriver

# Code By Muhammad Novel
# Github : https://github.com/mnovel/BOT-ABSENSI-UMM
# Instagram : https://www.instagram.com/muhnovel._/

import time
import pytz
import telegram_send
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

id_ID = pytz.timezone('Asia/Jakarta')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')


matkul = [
    {
        "name": "Pemrograman Dasar",
        "id": 892991,
        "type": "khs",
        "day": "Wednesday",
        "time": "10"
    },
    {
        "name": "Pancasila",
        "id": 893015,
        "type": "khs",
        "day": "Friday",
        "time": "10"
    },
    {
        "name": "Kalkulus",
        "id": 892979,
        "type": "khs",
        "day": "Monday",
        "time": "08"
    },
    {
        "name": "Pengantar Teknologi Informasi",
        "id": 892967,
        "type": "khs",
        "day": "Friday",
        "time": "14"
    },
    {
        "name": "Pengantar Teknologi Informasi",
        "id": 89580,
        "type": "lms",
        "day": "Friday",
        "time": "14"
    },
    {
        "name": "Bahsa Indonesia",
        "id": 893027,
        "type": "khs",
        "day": "Friday",
        "time": "16"
    },
    {
        "name": "Bahsa Indonesia",
        "id": 84296,
        "type": "lms",
        "day": "Thursday",
        "time": "19"
    },
    {
        "name": "Organisasi Komputer",
        "id": 72870,
        "type": "lms",
        "day": "Wednesday",
        "time": "08"
    }
]

pages = [
    {
        "type": "khs",
        "login": "https://infokhs.umm.ac.id/",
        "refer": "https://infokhs.umm.ac.id/jadwal-kuliah/202120221/presensi/"
    },
    {
        "type": "lms",
        "login": "https://lms.umm.ac.id/login/index.php",
        "refer": "https://lms.umm.ac.id/mod/attendance/view.php?id="
    }
]


def sendTele(msg):
    telegram_send.send(messages=[msg])


def login(res, username, password, dates):

    name = res["name"]
    id = res["id"]
    type = res["type"]

    for i in pages:
        if(i["type"] == type):

            driver = webdriver.Chrome("chromedriver", options=chrome_options)

            driver.implicitly_wait(3)
            driver.get(i["login"])
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)

            if type == "khs":
                try:
                    btn = driver.find_element(By.CLASS_NAME, "submit")
                    btn.click()
                    driver.implicitly_wait(3)
                    driver.get(str(i["refer"]) + str(id))
                    driver.implicitly_wait(3)
                    driver.find_element(By.LINK_TEXT, "Hadir").click()
                    sendTele("[+] Berhasil Absen " + name + " Pada " + dates)
                    print("[+] Berhasil Absen", name, "Pada", dates)
                except NoSuchElementException:
                    print("[-]", dates, "WIB >> Belum Waktu Absen", name)
            elif type == "lms":
                try:
                    btn = driver.find_element(By.ID, "loginbtn")
                    btn.click()
                    driver.implicitly_wait(3)
                    driver.get(str(i["refer"]) + str(id))
                    driver.implicitly_wait(3)
                    driver.find_element(
                        By.LINK_TEXT, "Submit attendance").click()
                    try:
                        driver.implicitly_wait(3)
                        driver.find_element(
                            By.XPATH, "/html/body/div[2]/div[5]/div/div/section/div/div/div[1]/form/fieldset/div/div/div[2]/fieldset/div/label[1]/input").click()
                        driver.implicitly_wait(3)
                        driver.find_element(By.ID, "id_submitbutton").click()
                    except NoSuchElementException:
                        pass
                    sendTele("[+] Berhasil Absen " + name + " Pada " + dates)
                    print("[+] Berhasil Absen", name, "Pada", dates)
                except NoSuchElementException:
                    print("[-]", dates, "WIB >> Belum Waktu Absen", name)

            driver.implicitly_wait(10)
            driver.quit()


while True:
    for res in matkul:
        now = datetime.now(id_ID)
        day = now.strftime("%A")
        times = now.strftime("%H")
        username = 123
        password = 123

        if str(res["day"]) == str(day) and str(res["time"]) == str(times):
            login(res, username, password, now.strftime("%A, %H:%M:%S"))
        else:
            print("[-]", now.strftime("%A, %H:%M:%S"),
                  "WIB >> Belum Waktu Absen", res["name"])
        time.sleep(5)
