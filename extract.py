from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from langdetect import detect


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    return driver.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")

def getIt(link):
    mylinklist=[]
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("----disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    url=link
    myDriver.get(url)
    links=myDriver.find_elements_by_tag_name("a")
    for lnk in links:
        mylinklist.append(lnk.get_attribute("href"))
        
    words= myDriver.find_element_by_tag_name('body').text
    row_list = words.split('\n')

    hi=0
    leng=len(row_list)
    for i in row_list:
        dt1= detect(i)

        if dt1=="hi":
            hi+=1

    ratio1=hi/leng
    if ratio1 <=0.60:
        print("Bad Translation",ratio1)

    else:
        return {"Main Page is Hindi Language":" "}
        
