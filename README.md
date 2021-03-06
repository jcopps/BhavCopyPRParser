# BhavCopyPRParser
A simple parser to consume PR files available with NSE. 

National Stock Exchange of India Limited
Capital Market Information Service 

Information related to  files in nuprddmmyy.zip:

This is to inform all the news-vendors and news agencies that, on NSE various instruments like Equities, Debentures, Warrants, Partly Paid Shares etc. are traded.

The nuprddmmyy.zip contains the following files:

Anddmmyy.txt
Bcddmmyy.csv
bhddmmyy.csv
Bmddmmyy.txt
cdddmmyyyy.zip
corpbondddmmyy.csv
etfddmmyy.csv
foddmmyyyy.zip
Glddmmyy.csv
HLddmmyy.csv
Pdddmmyy.csv
Prddmmyy.csv
Readme.txt
smeddmmyy.csv
Ttddmmyy.csv

Anddmmyy.txt file contains name of the co., its symbol and the announcements made during the day.    

Bcddmmyy.csv file contains the corporate action details for securities.

bhddmmyy.csv file contains a list of securities which have hit their price bands during the day.

Bmddmmyy.txt file contains details of Board Meetings of companies.

cdddmmyyyy.zip folder contains press files for Currency Derivative segment.

corpbondddmmyy.csv file contains market data of Corporate bonds traded during the day.

etfddmmyy.csv file contains market data of exchange traded funds traded during the day.

foddmmyyyy.zip folder contains press files for Future & Options Segment.

Glddmmyy.csv file contains a list of the gainers and losers for Nifty Securities, Nifty Next 50 Securities and for other Securities.

HLddmmyy.csv file contains a list of securities which have reached a new high or a new low.

Pdddmmyy.csv file also contains Symbol and Series codes for each Security in addition to the information contained in the prddmmyy.csv file.

Prddmmyy.csv file contains security wise market data information along with the Index details.

Readme.txt is a informative file which contains information about data and structure of all other files.

smeddmmyy.csv file contains market data of SME securities traded during the day.

Ttddmmyy.csv file contains a list of top twenty five securities by traded value.


```
class BhavPR:
    Function: get_company(search_string)
        Returns a list of company name, symbol pairs as a set that matches the search_string.

    Function: collect(date_start, date_end)
        Returns a bool implying the success of the collection. 
        Collects the PR files available on the server for the provided date range. 
            date_start: Format as 01-01-2020 DD-MM-YYYY
            date_end: Format as 05-01-2020 DD-MM-YYYY
    
    Function: get_symbol(search_string, on_symbol=False)
        Returns a list of matched company records.
        on_symbol: Limit to symbol field

    Function: set_company(company_name)
        Returns a bool of the context set.
``` 
    
## Build instructions

```
Test environment
# Ensure the following is executed within a virtual environment. 
python3 -m pip install --upgrade build
python3 setup.py sdist
python3 setup.py bdist_wheel

python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps bhavpr-jcopps


Real environment [ Caution ]
# Ensure the following is executed within a virtual environment. 
python3 -m pip install --upgrade build
python3 setup.py sdist
python3 setup.py bdist_wheel

python3 -m pip install --upgrade twine
python3 -m twine upload dist/*

pip3 install bhavpr

```
