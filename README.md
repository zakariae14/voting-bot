# voting-bot
A bot that is capable of voting multiple votes on Strawpoll.


bot who can vote automatically in Strawpoll.
Strawpoll allows to vote based on an IP address (default setting in Strawpoll vote), so the idea is to rotate IP address

step 1: automate vote using Selenium library

Selenium is a library in Python, used for interacting with a dynamic Web site. 
when I use Selenium, and try to create a webdriver.Chrome/web driver.Edge object, Strawpoll didn't count the votes with this item.
so, I used 'msedge.selenium_tools' library (must be installed from pycharm terminal #pip install msedge.selenium_tools ), it has a chromium feature that can respond to the previous problem.
this browser should have some options: 
*options.use_chromium = True
*options.add_argument("disable-blink-features=AutomationControlled")
*options.headless = False (by default)

sure, we need the web driver tools (msedgedriver.exe) should be in "C:\Program Files (x86)" to be executable : 

step 2: IP rotating

for this step, we need a VPN tool that can provide us with some IP addresses such as : TunnelBear, UltraSurf
the best one is UltraSurf. Download its exe file (u.exe), and use it from the command line, or from Python script with os.system
Tunnel bear can be used in linux (tunnelbear_linux), but in Windows is complicated.


NB: Strawpoll can detect some VPN IPs, so we need to test a huge number of IPs.
