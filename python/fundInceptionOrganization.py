from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import sys
import datetime

now = datetime.datetime.now()
# make the input file take in the first arg which will be the input file
inputFile = open(sys.argv[1], "r")
print 'Opened', sys.argv[1]
# Open file that holds ticker symbols to be searched
lines = inputFile.readlines()
count = 1
# Open file that holds 0-9 year old funds
zeroNineFile = open("0-9yrFunds.txt", "a")
# Open file that holds 10-19 year old funds
tenNineteenFile = open("10-19yrFunds.txt", "a")
# Open file that holds 20-29 year old funds
twentyTwentyNineFile = open("20-29yrFunds.txt", "a")
# Open file that holds 30-39 year old funds
thirtyThirtyNineFile = open("30-39yrFunds.txt", "a")
# Open file that holds 40-49 year old funds
fortyFortyNineFile = open("40-49yrFunds.txt", "a")
# Open file that holds 50-59 year old funds
fiftyFiftyNineFile = open("50-59yrFunds.txt", "a")
# Open file that holds 60+ year old funds
sixtyPlusFile = open("60yrPlusFunds.txt", "a")
# Open file for manual review funds
errorFile = open("errorFile.txt","a")


for currentTicker in lines:
    # Go to the summary page to get inception date then add to appropriate file
    driver = webdriver.Chrome()
    driver.get('https://finance.yahoo.com/quote/' + currentTicker + '?p=' + currentTicker + '&.tsrc=fin-srch')
    try:
#        tempName = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/h1").text
#        tempPrice = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]").text
#        tempCategory = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/span").text
#        tempExpenseRatio = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/span").text
#        tempHoldingsTurnover = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/span").text
        inceptionDate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[8]/td[2]/span").text
        if inceptionDate != 'N/A':
            if "-" not in inceptionDate and "." not in inceptionDate:
                tempInceptionDate = int(inceptionDate[-4:])
            elif "-" in inceptionDate:
                tempInceptionDate = int(inceptionDate[:4])
            else:
                print('Format error',currentTicker)
                tempInceptionDate = 4000
                outputFile = errorFile
            fundAge = (now.year - tempInceptionDate)
            if fundAge >= 0 and fundAge < 10:
#                zeroNineFile.write(currentTicker)
                outputFile = zeroNineFile
                print('added to 0-9')
            if fundAge >= 10 and fundAge < 20:
#                tenNineteenFile.write(currentTicker)
                outputFile = tenNineteenFile
                print('added to 10-19')
            if fundAge >= 20 and fundAge < 30:
#                twentyTwentyNineFile.write(currentTicker)
                outputFile = twentyTwentyNineFile
                print('added to 20-29')
            if fundAge >= 30 and fundAge < 40:
#                thirtyThirtyNineFile.write(currentTicker)
                outputFile = thirtyThirtyNineFile
                print('added to 30-39')
            if fundAge >= 40 and fundAge < 50:
#                fortyFortyNineFile.write(currentTicker)
                outputFile = fortyFortyNineFile
                print('added to 40-49')
            if fundAge >= 50 and fundAge < 60:
#                fiftyFiftyNineFile.write(currentTicker)
                outputFile = fiftyFiftyNineFile
                print('added to 50-59')
            if fundAge >= 60:
#                sixtyPlusFile.write(currentTicker)
                outputFile = sixtyPlusFile
                print('added to 60+')
            outputFile.write(currentTicker)
#            outputFile.write(currentTicker.rstrip("\n") + ",")
#            outputFile.write(tempName + ",")
#            outputFile.write(tempPrice + ",")
#            outputFile.write(tempCategory+ ",")
#            outputFile.write(tempExpenseRatio + ",")
#            outputFile.write(inceptionDate + ",")
#            outputFile.write("\n")
    except NoSuchElementException:
        errorFile.write(currentTicker)
        print(currentTicker + ' Summary Error added to error file')

    driver.quit()
    print count,'of',len(lines)
    count+=1
    continue

# Close all files
inputFile.close()
zeroNineFile.close()
tenNineteenFile.close()
twentyTwentyNineFile.close()
thirtyThirtyNineFile.close()
fortyFortyNineFile.close()
fiftyFiftyNineFile.close()
sixtyPlusFile.close()
errorFile.close()

print("All funds have been gathered.")
