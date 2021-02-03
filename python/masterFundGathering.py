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

def notApplicableLogic(input):
    if "N/" in input:
        return "-1"
    else:
        return input

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
    # Profile driver
    driverProfile = webdriver.Chrome()
    driverProfile.get('https://finance.yahoo.com/quote/' + currentTicker + '/profile?p=' + currentTicker)
    
    # Profile
    try:
        name = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div[1]/h3').text
        name = name.replace(',', '')
        price = driverProfile.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').text
        price = price.replace(',', '')
        # Take the last char off it is a '%'
        expenseRatio = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[3]/div/div[2]/span[2]').text[:-1]
        category = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[1]/span[2]').text
        morningStar = len(driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[6]/span[2]/span').text)
        netAssets = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[3]/span[2]').text
        # Take the last char off it is a '%'
        holdingsTurnover = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[2]/div/div[3]/span[2]').text[:-1]
        holdingsTurnover = holdingsTurnover.replace(',','')
        # Date format YYYY-MM-DD
        inceptionDate = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[7]/span[2]/span').text
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
        fundFamily = driverProfile.find_element_by_xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[2]/div[1]/div/div[2]/span[2]').text
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Profile Error')

    if "ETF" in name:
        isEtf = True
    else:
        isMutualFund = True

    driverProfile.quit()
    print "25%",
    sys.stdout.flush()

    # Holdings driver
    driverHoldings = webdriver.Chrome()
    driverHoldings.get('https://finance.yahoo.com/quote/' + currentTicker + '/holdings?p=' + currentTicker)

    # Holdings
    # Overall Portfolio Composition %
    try:
        cash = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[1]/span[2]').text[:-1]
    except NoSuchElementException:
        cash = 0
        print(currentTicker + 'Holdings Cash Error')

    try:
        stocks = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[2]/span[2]').text[:-1]
    except NoSuchElementException:
        stocks = 0
        print(currentTicker + 'Holdings Stocks Error')

    try:
        bonds = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[3]/span[2]').text[:-1]
    except NoSuchElementException:
        bonds = 0
        print(currentTicker + 'Holdings Bonds Error')

    try:
        others = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[4]/span[2]').text[:-1]
    except NoSuchElementException:
        others = 0
        print(currentTicker + 'Holdings Others Error')

    try:
        preferred = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[5]/span[2]').text[:-1]
    except NoSuchElementException:
        preferred = 0
        print(currentTicker + 'Holdings Preferred Error')

    try:
        convertable = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[1]/div/div[6]/span[2]').text[:-1]
    except NoSuchElementException:
        convertable = 0
        print(currentTicker + 'Holdings Convertable Error')

    # Sector Weightings %
    try:
        basicMaterials = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[2]/span[3]').text[:-1]
        consumerCyclical = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[3]/span[3]').text[:-1]
        financialServices = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[4]/span[3]').text[:-1]
        realestate = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[5]/span[3]').text[:-1]
        consumerDefensive = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[6]/span[3]').text[:-1]
        healthcare = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[7]/span[3]').text[:-1]
        utilities = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[8]/span[3]').text[:-1]
        communicationServices = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[9]/span[3]').text[:-1]
        energy = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[10]/span[3]').text[:-1]
        industrials = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[11]/span[3]').text[:-1]
        technology = driverHoldings.find_element_by_xpath('//*[@id="Col1-0-Holdings-Proxy"]/section/div[1]/div[2]/div/div[12]/span[3]').text[:-1]
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Sector Weighting Error')

    driverHoldings.quit()
    print "\r50%",
    sys.stdout.flush()

    # Performance driver
    driverPerformance = webdriver.Chrome()
    driverPerformance.get('https://finance.yahoo.com/quote/' + currentTicker + '/performance?p=' + currentTicker)

    # Performance
    try:
        numOfYearsUp = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[1]/div/div[1]/div[4]/span[2]').text
        numOfYearsDown = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[1]/div/div[1]/div[5]/span[2]').text
        yearToDate = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[2]/span[2]').text[:-1]
        oneMonth = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[3]/span[2]').text[:-1]
        threeMonth = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[4]/span[2]').text[:-1]
        oneYear = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[5]/span[2]').text[:-1]
        threeYear = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[6]/span[2]').text[:-1]
        fiveYear = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[7]/span[2]').text[:-1]
        tenYear = driverPerformance.find_element_by_xpath('//*[@id="Col1-0-Performance-Proxy"]/section/div[2]/div/div[8]/span[2]').text[:-1]
#       sinceInception = driverPerformance.find_element_by_xpath("").text
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Performance Error')

    driverPerformance.quit()
    print "\r75%",
    sys.stdout.flush()
    # Purchase Info driver
    driverPurchInfo = webdriver.Chrome()
    driverPurchInfo.get('https://finance.yahoo.com/quote/' + currentTicker + '/purchase-info?p=' + currentTicker)

    # Purchase Info
    try:
        minInitInv = driverPurchInfo.find_element_by_xpath('//*[@id="Col1-0-PurchaseInfo-Proxy"]/section/div[1]/div/div[1]/div[1]/span[2]').text
        minInitInv = minInitInv.replace(',', '')
        minSubInv = driverPurchInfo.find_element_by_xpath('//*[@id="Col1-0-PurchaseInfo-Proxy"]/section/div[1]/div/div[2]/div[1]/span[2]').text
        minSubInv = minSubInv.replace(',', '')
    except NoSuchElementException:
        hasError = True
        print(currentTicker + ' Purchase Info Error')

#    driverProfile.quit()
#    driverHoldings.quit()
#    driverPerformance.quit()
    driverPurchInfo.quit()

    fundAge = (now.year - int(inceptionDate[:4]))
    if fundAge >= 0 and fundAge < 10:
        outputFile = open("../ageBasedFlatFiles/0-9yrFunds.csv", "a")
        print('\radded to 0-9')
    if fundAge >= 10 and fundAge < 20:
        outputFile = open("../ageBasedFlatFiles/10-19yrFunds.csv", "a")
        print('\radded to 10-19')
    if fundAge >= 20 and fundAge < 30:
        outputFile = open("../ageBasedFlatFiles/20-29yrFunds.csv", "a")
        print('\radded to 20-29')
    if fundAge >= 30 and fundAge < 40:
        outputFile = open("../ageBasedFlatFiles/30-39yrFunds.csv", "a")
        print('\radded to 30-39')
    if fundAge >= 40 and fundAge < 50:
        outputFile = open("../ageBasedFlatFiles/40-49yrFunds.csv", "a")
        print('\radded to 40-49')
    if fundAge >= 50 and fundAge < 60:
        outputFile = open("../ageBasedFlatFiles/50-59yrFunds.csv", "a")
        print('\radded to 50-59')
    if fundAge >= 60:
        outputFile = open("../ageBasedFlatFiles/60yrPlusFunds.csv", "a")
        print('\radded to 60+')

    if (not hasError):
        outputFile.write(currentTicker.rstrip() + ",")
        outputFile.write(name + ",")
        outputFile.write(price + ",")
        outputFile.write(expenseRatio + ",")
        outputFile.write(category + ",")
        outputFile.write(str(morningStar) + ",")
        outputFile.write(netAssets + ",")
        outputFile.write(notApplicableLogic(holdingsTurnover) + ",")
        outputFile.write(inceptionDate + ",")
        outputFile.write(fundFamily + ",")
        outputFile.write(notApplicableLogic(cash) + ",")
        outputFile.write(notApplicableLogic(stocks) + ",")
        outputFile.write(notApplicableLogic(bonds) + ",")
        outputFile.write(notApplicableLogic(others) + ",")
        outputFile.write(notApplicableLogic(preferred) + ",")
        outputFile.write(notApplicableLogic(convertable) + ",")
        outputFile.write(notApplicableLogic(basicMaterials) + ",")
        outputFile.write(notApplicableLogic(consumerCyclical) + ",")
        outputFile.write(notApplicableLogic(financialServices) + ",")
        outputFile.write(notApplicableLogic(realestate) + ",")
        outputFile.write(notApplicableLogic(consumerDefensive) + ",")
        outputFile.write(notApplicableLogic(healthcare) + ",")
        outputFile.write(notApplicableLogic(utilities) + ",")
        outputFile.write(notApplicableLogic(communicationServices) + ",")
        outputFile.write(notApplicableLogic(energy) + ",")
        outputFile.write(notApplicableLogic(industrials) + ",")
        outputFile.write(notApplicableLogic(technology) + ",")
        outputFile.write(notApplicableLogic(numOfYearsUp) + ",")
        outputFile.write(notApplicableLogic(numOfYearsDown) + ",")
        outputFile.write(notApplicableLogic(yearToDate) + ",")
        outputFile.write(notApplicableLogic(oneMonth) + ",")
        outputFile.write(notApplicableLogic(threeMonth) + ",")
        outputFile.write(notApplicableLogic(oneYear) + ",")
        outputFile.write(notApplicableLogic(threeYear) + ",")
        outputFile.write(notApplicableLogic(fiveYear) + ",")
        outputFile.write(notApplicableLogic(tenYear) + ",")
        outputFile.write("NULL,")
        outputFile.write(notApplicableLogic(minInitInv) + ",")
        outputFile.write(notApplicableLogic(minSubInv) + ",")
        outputFile.write(str(isMutualFund) + ",")
        outputFile.write(str(isEtf) + ",")
        outputFile.write(now.strftime('%Y-%m-%d'))
        outputFile.write("\n")
    else:
        errorFile = open("../ageBasedFlatFiles/errorFile.txt","a")
        errorFile.write(currentTicker)
        errorFile.write("\n")
        errorFile.close()
    print count,'of',len(lines),'|',len(lines)-count,'Remaining',datetime.datetime.now()
    count+=1
    continue

outputFile.close()

#zeroNineFile.close()
#tenNineteenFile.close()
#twentyTwentyNineFile.close()
#thirtyThirtyNineFile.close()
#fortyFortyNineFile.close()
#fiftyFiftyNineFile.close()
#sixtyPlusFile.close()
#errorFile.close()
inputFile.close()

print("All funds have been gathered.")
