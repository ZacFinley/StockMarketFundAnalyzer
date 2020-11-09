from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

outputFile = open("A_Funds_Results.csv", "w")
# set header row
outputFile.write("Ticker,")
outputFile.write("Name,")
outputFile.write("Price,")
outputFile.write("Category,")
outputFile.write("Expense Ratio,")
outputFile.write("Holding Turnover,")
outputFile.write("Inception Date(mm/dd),")
outputFile.write("Inception Date(yyyy),")
outputFile.write("Cash,")
outputFile.write("Stocks,")
outputFile.write("Bonds,")
outputFile.write("Others,")
outputFile.write("Preferred,")
outputFile.write("Convertable,")
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
outputFile.write("YTD,")
outputFile.write("1-Month,")
outputFile.write("3-Month,")
outputFile.write("1-Year,")
outputFile.write("3-Year,")
outputFile.write("5-Year,")
outputFile.write("10-Year")
outputFile.write("\n")
# Open file that holds ticker symbols to be searched
inputFile = open("A_Funds.txt", "r")
lines = inputFile.readlines()
count = 1
for currentTicker in lines:

    # If you want to open Chrome
    # Summary
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '?p=' + currentTicker + '&.tsrc=fin-srch')
    try:
        tempName = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/h1").text
        tempPrice = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]").text
        tempCategory = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/span").text
        tempExpenseRatio = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/span").text
        tempHoldingsTurnover = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/span").text
        tempInceptionDate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[8]/td[2]/span").text
    except NoSuchElementException:
        print(currentTicker + ' Summary Error')

    outputFile.write(currentTicker + ",")
    outputFile.write(tempName + ",")
    outputFile.write(tempPrice + ",")
    outputFile.write(tempCategory+ ",")
    outputFile.write(tempExpenseRatio + ",")
    outputFile.write(tempHoldingsTurnover + ",")
    outputFile.write(tempInceptionDate + ",")
    driver.quit()

    # Holdings
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '/holdings?p=' + currentTicker)
    # Overall Portfolio Composition %
    try:
        tempCash = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[1]/div/div[1]/span[2]").text
        tempStocks = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[1]/div/div[2]/span[2]").text
        tempBonds = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[1]/div/div[3]/span[2]").text
        tempOthers = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[1]/div/div[4]/span[2]").text
        tempPreferred = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[1]/div/div[5]/span[2]").text
        tempConvertable = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[1]/div/div[6]/span[2]").text
    except NoSuchElementException:
        print(currentTicker + 'Error')

    outputFile.write(tempCash + ",")
    outputFile.write(tempStocks + ",")
    outputFile.write(tempBonds + ",")
    outputFile.write(tempOthers + ",")
    outputFile.write(tempPreferred + ",")
    outputFile.write(tempConvertable + ",")

    # Sector Weightings %
    try:
        tempBasicMaterials = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[2]/span[3]").text
        tempConsumerCyclical = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[3]/span[3]").text
        tempFinancialServices = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[4]/span[3]").text
        tempRealestate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[5]/span[3]").text
        tempConsumerDefensive = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[6]/span[3]").text
        tempHealthcare = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[7]/span[3]").text
        tempUtilities = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[8]/span[3]").text
        tempCommunicationServices = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[9]/span[3]").text
        tempEnergy = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[10]/span[3]").text
        tempIndustrials = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[11]/span[3]").text
        tempTechnology = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[1]/div[2]/div/div[12]/span[3]").text
    except NoSuchElementException:
        print(currentTicker + ' Sector Weighting Error')

    outputFile.write(tempBasicMaterials + ",")
    outputFile.write(tempConsumerCyclical + ",")
    outputFile.write(tempFinancialServices + ",")
    outputFile.write(tempRealestate + ",")
    outputFile.write(tempConsumerDefensive + ",")
    outputFile.write(tempHealthcare + ",")
    outputFile.write(tempUtilities + ",")
    outputFile.write(tempCommunicationServices + ",")
    outputFile.write(tempEnergy + ",")
    outputFile.write(tempIndustrials + ",")
    outputFile.write(tempTechnology + ",")
    driver.quit()
    
    # Performance
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '/performance?p=' + currentTicker)
    try:
        tempYearToDate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[2]/span[2]").text
        tempOneMonth = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[3]/span[2]").text
        tempThreeMonth = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[4]/span[2]").text
        tempOneYear = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[5]/span[2]").text
        tempThreeYear = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[6]/span[2]").text
        tempFiveYear = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[7]/span[2]").text
        tempTenYear = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div/div[8]/span[2]").text
    except NoSuchElementException:
        print(currentTicker + ' Performance Error')
    outputFile.write(tempYearToDate + ",")
    outputFile.write(tempOneMonth + ",")
    outputFile.write(tempThreeMonth + ",")
    outputFile.write(tempOneYear + ",")
    outputFile.write(tempThreeYear + ",")
    outputFile.write(tempFiveYear + ",")
    outputFile.write(tempTenYear + "\n")
    driver.quit()
    print("Funds gathered: ")
    print(count)
    print("\n")
    count+=1
    continue

outputFile.close()
inputFile.close()

print("All funds have been gathered.")
