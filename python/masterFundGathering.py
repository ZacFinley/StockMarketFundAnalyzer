from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import sys
import datetime

def writeHeader(outputFile):
    # Set header row
    outputFile.write("Ticker,")
    outputFile.write("Name,")
    outputFile.write("Price,")
    outputFile.write("Expense Ratio,")
    outputFile.write("Category,")
    outputFile.write("Morning Star Rating,")
    outputFile.write("Net Assets,")
    outputFile.write("Holdings Turnover,")
    outputFile.write("Inception Date,")
    outputFile.write("Fund Family,")
    # Portfolio Composition
    outputFile.write("Cash,")
    outputFile.write("Stocks,")
    outputFile.write("Bonds,")
    outputFile.write("Others,")
    outputFile.write("Preferred,")
    outputFile.write("Convertable,")
    # Sector Weight
    outputFile.write("Basic Materials,")
    outputFile.write("Consumer Cyclical,")
    outputFile.write("Financial Services,")
    outputFile.write("Realestate,")
    outputFile.write("Consumer Defensive,")
    outputFile.write("Healthcare,")
    outputFile.write("Utilities,")
    outputFile.write("Communication Services,")
    outputFile.write("Energy,")
    outputFile.write("Industrials,")
    outputFile.write("Technology,")
    # Performance
    outputFile.write("Number Years Up,")
    outputFile.write("Number Years Down,")
    outputFile.write("YTD,")
    outputFile.write("1-Month,")
    outputFile.write("3-Month,")
    outputFile.write("1-Year,")
    outputFile.write("3-Year,")
    outputFile.write("5-Year,")
    outputFile.write("10-Year,")
    outputFile.write("Inception,")
    outputFile.write("Minimum Initial Investment,")
    outputFile.write("Minimum Subsequent Investment,")
    outputFile.write("Mutual Fund,")
    outputFile.write("ETF,")
    outputFile.write("Capture Date")
    outputFile.write("\n")

# Open file that holds 0-9 year old funds
zeroNineFile = open("../ageBasedFlatFiles/0-9yrFunds.csv", "a")
#writeHeader(zeroNineFile)
# Open file that holds 10-19 year old funds
tenNineteenFile = open("../ageBasedFlatFiles/10-19yrFunds.csv", "a")
#writeHeader(tenNineteenFile)
# Open file that holds 20-29 year old funds
twentyTwentyNineFile = open("../ageBasedFlatFiles/20-29yrFunds.csv", "a")
#writeHeader(twentyTwentyNineFile)
# Open file that holds 30-39 year old funds
thirtyThirtyNineFile = open("../ageBasedFlatFiles/30-39yrFunds.csv", "a")
#writeHeader(thirtyThirtyNineFile)
# Open file that holds 40-49 year old funds
fortyFortyNineFile = open("../ageBasedFlatFiles/40-49yrFunds.csv", "a")
#writeHeader(fortyFortyNineFile)
# Open file that holds 50-59 year old funds
fiftyFiftyNineFile = open("../ageBasedFlatFiles/50-59yrFunds.csv", "a")
#writeHeader(fiftyFiftyNineFile)
# Open file that holds 60+ year old funds
sixtyPlusFile = open("../ageBasedFlatFiles/60yrPlusFunds.csv", "a")
#writeHeader(sixtyPlusFile)
# Open file for manual review funds
errorFile = open("../ageBasedFlatFiles/errorFile.txt","a")

now = datetime.datetime.now()
isMutualFund = False
isEtf = False
hasError = False
# make the input file take in the first arg which will be the input file
inputFile = open(sys.argv[1], "r")
print 'Opened', sys.argv[1]
# Open file that holds ticker symbols to be searched
lines = inputFile.readlines()
count = 1

for currentTicker in lines:
    currentTicker = currentTicker.rstrip("\n")
#     Profile
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '/profile?p=' + currentTicker)
    try:
        name = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div[1]/h3').text
        price = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').text
        price = price.replace(',', '')
        # Take the last char off it is a '%'
        expenseRatio = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[3]/div/div[2]/span[2]').text[:-1]
        category = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[1]/span[2]').text
        morningStar = len(driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[6]/span[2]/span').text)
        netAssets = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[3]/span[2]').text
        # Take the last char off it is a '%'
        holdingsTurnover = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[2]/div/div[3]/span[2]').text[:-1]
        # Date format YYYY-MM-DD
        inceptionDate = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[7]/span[2]/span').text
        if "-" not in inceptionDate and "." not in inceptionDate:
            tempDate = inceptionDate.split()
            tempYear = tempDate[2]
            tempDay = tempDate[1][:-1]
            if len(tempDay) == 1:
                tempDay = "0" + tempDay
            tempMonth = tempDate[0]
            if "Jan" in tempMonth:
                tempMonth = "01"
            elif "Feb" in tempMonth:
                tempMonth = "02"
            elif "Mar" in tempMonth:
                tempMonth = "03"
            elif "Apr" in tempMonth:
                tempMonth = "04"
            elif "May" in tempMonth:
                tempMonth = "05"
            elif "Jun" in tempMonth:
                tempMonth = "06"
            elif "Jul" in tempMonth:
                tempMonth = "07"
            elif "Aug" in tempMonth:
                tempMonth = "08"
            elif "Sep" in tempMonth:
                tempMonth = "09"
            elif "Oct" in tempMonth:
                tempMonth = "10"
            elif "Nov" in tempMonth:
                tempMonth = "11"
            elif "Dec" in tempMonth:
                tempMonth = "12"
            inceptionDate = (tempYear + "-" + tempMonth + "-" + tempDay)
        fundFamily = driver.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[2]/span[2]').text
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Profile Error')

    driver.quit()

    if "ETF" in name:
        isEtf = True
    else:
        isMutualFund = True


    # Holdings
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '/holdings?p=' + currentTicker)
    # Overall Portfolio Composition %
    try:
        cash = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[1]/span[2]').text[:-1]
    except NoSuchElementException:
        cash = 0
        print(currentTicker + 'Holdings Cash Error')

    try:
        stocks = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[2]/span[2]').text[:-1]
    except NoSuchElementException:
        stocks = 0
        print(currentTicker + 'Holdings Stocks Error')

    try:
        bonds = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[3]/span[2]').text[:-1]
    except NoSuchElementException:
        bonds = 0
        print(currentTicker + 'Holdings Bonds Error')

    try:
        others = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[4]/span[2]').text[:-1]
    except NoSuchElementException:
        others = 0
        print(currentTicker + 'Holdings Others Error')

    try:
        preferred = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[5]/span[2]').text[:-1]
    except NoSuchElementException:
        preferred = 0
        print(currentTicker + 'Holdings Preferred Error')

    try:
        convertable = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[6]/span[2]').text[:-1]
    except NoSuchElementException:
        convertable = 0
        print(currentTicker + 'Holdings Convertable Error')

    # Sector Weightings %
    try:
        basicMaterials = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[2]/span[3]').text[:-1]
        consumerCyclical = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[3]/span[3]').text[:-1]
        financialServices = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[4]/span[3]').text[:-1]
        realestate = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[5]/span[3]').text[:-1]
        consumerDefensive = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[6]/span[3]').text[:-1]
        healthcare = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[7]/span[3]').text[:-1]
        utilities = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[8]/span[3]').text[:-1]
        communicationServices = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[9]/span[3]').text[:-1]
        energy = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[10]/span[3]').text[:-1]
        industrials = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[11]/span[3]').text[:-1]
        technology = driver.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[12]/span[3]').text[:-1]
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Sector Weighting Error')

    driver.quit()
    
    # Performance
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '/performance?p=' + currentTicker)
    try:
        numOfYearsUp = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[1]/div/div[1]/div[4]/span[2]').text
        numOfYearsDown = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[1]/div/div[1]/div[5]/span[2]').text
        yearToDate = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[2]/span[2]').text[:-1]
        oneMonth = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[3]/span[2]').text[:-1]
        threeMonth = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[4]/span[2]').text[:-1]
        oneYear = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[5]/span[2]').text[:-1]
        threeYear = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[6]/span[2]').text[:-1]
        fiveYear = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[7]/span[2]').text[:-1]
        tenYear = driver.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[8]/span[2]').text[:-1]
#       sinceInception = driver.find_element_by_xpath("").text
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Performance Error')

    driver.quit()

    # Purchase Info
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '/purchase-info?p=' + currentTicker)
    try:
        minInitInv = driver.find_element_by_xpath('//*[@id="Col1-0-PurchaseInfo-Proxy"]/section/div[1]/div/div[1]/div[1]/span[2]').text
        minInitInv = minInitInv.replace(',', '')
        minSubInv = driver.find_element_by_xpath('//*[@id="Col1-0-PurchaseInfo-Proxy"]/section/div[1]/div/div[2]/div[1]/span[2]').text
        minSubInv = minSubInv.replace(',', '')
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Purchase Info Error')
    driver.quit()

    fundAge = (now.year - int(inceptionDate[:4]))
    if fundAge >= 0 and fundAge < 10:
        outputFile = zeroNineFile
        print('added to 0-9')
    if fundAge >= 10 and fundAge < 20:
        outputFile = tenNineteenFile
        print('added to 10-19')
    if fundAge >= 20 and fundAge < 30:
        outputFile = twentyTwentyNineFile
        print('added to 20-29')
    if fundAge >= 30 and fundAge < 40:
        outputFile = thirtyThirtyNineFile
        print('added to 30-39')
    if fundAge >= 40 and fundAge < 50:
        outputFile = fortyFortyNineFile
        print('added to 40-49')
    if fundAge >= 50 and fundAge < 60:
        outputFile = fiftyFiftyNineFile
        print('added to 50-59')
    if fundAge >= 60:
        outputFile = sixtyPlusFile
        print('added to 60+')

    if (not hasError):
        outputFile.write(currentTicker.rstrip("\n") + ",")
        outputFile.write(name + ",")
        outputFile.write(price + ",")
        outputFile.write(expenseRatio + ",")
        outputFile.write(category + ",")
        outputFile.write(str(morningStar) + ",")
        outputFile.write(netAssets + ",")
        outputFile.write(holdingsTurnover + ",")
        outputFile.write(inceptionDate + ",")
        outputFile.write(fundFamily + ",")
        outputFile.write(cash + ",")
        outputFile.write(stocks + ",")
        outputFile.write(bonds + ",")
        outputFile.write(others + ",")
        outputFile.write(preferred + ",")
        outputFile.write(convertable + ",")
        outputFile.write(basicMaterials + ",")
        outputFile.write(consumerCyclical + ",")
        outputFile.write(financialServices + ",")
        outputFile.write(realestate + ",")
        outputFile.write(consumerDefensive + ",")
        outputFile.write(healthcare + ",")
        outputFile.write(utilities + ",")
        outputFile.write(communicationServices + ",")
        outputFile.write(energy + ",")
        outputFile.write(industrials + ",")
        outputFile.write(technology + ",")
        outputFile.write(numOfYearsUp + ",")
        outputFile.write(numOfYearsDown + ",")
        outputFile.write(yearToDate + ",")
        outputFile.write(oneMonth + ",")
        outputFile.write(threeMonth + ",")
        outputFile.write(oneYear + ",")
        outputFile.write(threeYear + ",")
        outputFile.write(fiveYear + ",")
        outputFile.write(tenYear + ",")
        outputFile.write("NULL,")
        outputFile.write(minInitInv + ",")
        outputFile.write(minSubInv + ",")
        outputFile.write(str(isMutualFund) + ",")
        outputFile.write(str(isEtf) + ",")
        outputFile.write(now.strftime('%Y-%m-%d'))
        outputFile.write("\n")
    else:
        errorFile.write(currentTicker)
    print count,'of',len(lines),'|',len(lines)-count,'Remaining',datetime.datetime.now()
    count+=1
    continue

zeroNineFile.close()
tenNineteenFile.close()
twentyTwentyNineFile.close()
thirtyThirtyNineFile.close()
fortyFortyNineFile.close()
fiftyFiftyNineFile.close()
sixtyPlusFile.close()
errorFile.close()
inputFile.close()

print("All funds have been gathered.")
