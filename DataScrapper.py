## Created By: Austin Roberts
## Date: Corona 2020

import os
from os.path import isfile, join
import requests
import urllib.request
import urllib.parse
from pathlib import Path
import pandas
import glob as glob
import xlwt
import openpyxl


# ExcelLocation = input("Enter a file path you would like to store the excel files: ")
ExcelLocation = r''

# ExcelLocation = ""  ## Make sure there is a slash '/' at the end.
MasterFile = ExcelLocation + "Master_file.xls"

# As of May 22nd 2021 they changed their link but the current still works. May need updating soon.
urls = [
    'https://advisors.voya.com/document/holdings/voya-corporate-leaders-100-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-global-equity-dividend-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-global-high-dividend-low-volatility-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-global-multi-asset-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-large-cap-value-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-large-cap-growth-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-mid-cap-research-enhanced-index-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-midcap-opportunities-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-multi-manager-emerging-markets-equity-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-multi-manager-international-equity-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-multi-manager-international-factors-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-multi-manager-mid-cap-value-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-small-company-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-smallcap-opportunities-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-us-high-dividend-low-volatility-fund-monthly-holdings-xls.xls'
]

# Verifying that the http return code is successful, return code 200 is ideal.
#################################################
def url_ok(*url):
    for i in range(0, len(url)):
        url_Obj = requests.head(url[i])
        print(url_Obj)
        if (url_Obj.status_code != 200):
            print("URL's that are not working properly:\n", url[i])

    return (url_Obj.status_code == 200)

# Collects each file off Voya's webpage
################################################
def Collector(*url):

    checkerton = url_ok(*url)
    try:
        #  checkerton == 1
        if (checkerton == 1):
            print("Executing requests...")

            # Iterates through the url list and parses with "/" as a delimiter to then create a unique file path
            for i in range(0, len(url)):
                #  Parses the URL and appends the file name onto the filepath given, within the os
                appendPath = urllib.parse.urlparse(url[i])
                pathArray = appendPath.path.split("/")

                print("Downloading... " + pathArray[3])
                # nice
                newPath = ExcelLocation + pathArray[3]  # Appending the file name at the end of the path given above.

                urllib.request.urlretrieve(url[i], newPath) # These urllib methods allow us to collect the object (file) off the webpage. Requires a filename & place to drop it.

                # Leave these as empty strings for the next iteration
                newPath = ""

        else:
            print("URL passed is possibly no longer valid\n")
            print("URL returned: ", checkerton, "\nHTTPS RETURN CODES:\n1xx informational response – the request was received, continuing process\n2xx successful – the request was successfully received, understood, and accepted\n3xx redirection – further action needs to be taken in order to complete the request\n4xx client error – the request contains bad syntax or cannot be fulfilled\n5xx server error – the server failed to fulfil an apparently valid request")

    except Exception as e:
        print(e)

################# Concats all the files and appends a new column ########################
def concatExcel(filePath):
    os.chdir(filePath)

    files = glob.glob(filePath + "/*.xls")

    concatAll = pandas.DataFrame()
    for file in files:
        df = pandas.read_excel(file, header = 3)
        # print(df)
        concat_all_sheets_single_file = pandas.concat([df])
        concat_all_sheets_single_file['Filename'] = os.path.basename(file)
        concatAll = concatAll.append(concat_all_sheets_single_file)

    writer = pandas.ExcelWriter(MasterFile)
    concatAll.to_excel(writer)
    writer.save()


######## FUNCTION CALLS ########
Collector(*urls)
concatExcel(ExcelLocation)

print("         __   __")
print("             __ \ / __")
print("             /  \ | /  \ ")
print("                 \|/")
print("            _,.---v---._")
print("   /\__/\  /            \ ")
print("   \_  _/ /              \ " + "         That was over-whale-ming!")
print("     \ \_|           @ __|")
print("      \                \_")
print("       \     ,__/       /")
print("     ~~~`~~~~~~~~~~~~~~/~~~~")
