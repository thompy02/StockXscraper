from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://stockx.com/air-jordan-5-retro-moonlight-2021")

LastSale = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[2]/div[2]/div[1]/p[2]')

print(LastSale)


##BuyPrice = 


##ShoeSku = 