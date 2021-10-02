from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

##"https://stockx.com/air-jordan-5-retro-moonlight-2021"

ShoeLink = input("paste your shoe link here")

driver.get(ShoeLink)

LastSale = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[2]/div[2]/div[1]/p[2]')

print(LastSale.text + " Is the Price of the last shoe sold")

BuyPrice = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div/dl/dd')

print(BuyPrice.text + " Is the current Price to buy")

##ShoeSku = 

PriceFormula = 1.2

PriceAdjustment = (float(LastSale.text) * float(PriceFormula))

print(PriceAdjustment)

