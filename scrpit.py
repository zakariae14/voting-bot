import os
from msedge.selenium_tools import Edge, EdgeOptions
import time



web_page ="https://strawpoll.com/polls/1MnwORDedn7"
option_ID = "option-1MnwORDedn7-6QnMDENakye"  # in html web page
N = 100 # number of tries




start = time.time()

path = "C:\Program Files (x86)\msedgedriver.exe"
class_name = "w-40"
class_autorise = "fc-button"

options = EdgeOptions()
options.use_chromium = True
options.add_argument("disable-blink-features=AutomationControlled")
options.headless = False

for i in range(N):

    os.system("cd C:\Program Files (x86) & start u.exe")
    time.sleep(5)
    try:
        driver = Edge(executable_path=path, options=options)
        print("Process number : ", i + 1)
        driver.get(web_page)

        try:
            butt = driver.find_element_by_class_name(class_autorise)
            butt.click()
        except:
            pass

        butt1 = driver.find_element_by_id(option_ID)
        butt1.click()

        butt2 = driver.find_element_by_class_name(class_name)
        butt2.click()
        time.sleep(10)
        os.system("cd C:\Program Files (x86) & taskkill /im u.exe /f")
        driver.quit()
        time.sleep(2)
    except:
        try:
            os.system("cd C:\Program Files (x86) & taskkill /im u.exe /f")
            driver.quit()
            time.sleep(2)
        except:
            pass

finish = time.time()

print("The process time (seconde) is : ",finish-start)