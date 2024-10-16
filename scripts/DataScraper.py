## Created By: Austin Roberts
## Date: Corona 2020

import os

from tools.tools import *

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
    'https://advisors.voya.com/document/holdings/voya-us-high-dividend-low-volatility-fund-monthly-holdings-xls.xls',
    'https://advisors.voya.com/document/holdings/voya-corporate-leaders-trust-fund-series-b-monthly-holdings-xls.xls'
]


def main():

    tools = Tools()

    tools.download_excel(urls)

    tools.create_master_file()
    
    tools.remove_rows_by_keyword()

if __name__ == "__main__":
    main()


