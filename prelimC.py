import xml.etree.ElementTree as et
import csv

#Parsing
xml = et.parse("covid_cases_xml.xml")
root = xml.getroot()


#XML Information
dateRep = []
countryterritoryCode = []
cases = []
deaths = []

header = ["Date Reported", "Countries and Teritories", "Number of Cases", "Deaths"]

#For Loop for the XML
for FDate in root.iter('dateRep'):
    dateRep.append(FDate.text)

for FCountry in root.iter('countryterritoryCode'):
    countryterritoryCode.append(FCountry.text)

for FCase in root.iter('cases'):
    cases.append(FCase.text)

for FDeath in root.iter('deaths'):
    deaths.append(FDeath.text)

#Creating New CSV File for the XML
lenght = len(dateRep)

with open("SaveData", newline = "", mode="w") as f:

#Write Header
    covid_write = csv.writer(f)
    covid_write.writerow(header)

#For Loop Row
    for Data in range(lenght):
        row = [dateRep[Data], countryterritoryCode[Data], cases[Data], deaths[Data]]
        covid_write.writerow(row)