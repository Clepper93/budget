import openpyxl
from datetime import datetime

# Row 1 is a header row; data starts at Row 2

wb = openpyxl.load_workbook('budget.xlsx')
sheet = wb.active

maxrow = sheet.max_row
nextrow = 0

def getnext():
	global nextrow
	nextrow = (maxrow + 1)

getnext()

# A column is today's date

def getAcol():
	sheet['A{}'.format(nextrow)] = datetime.today()
getAcol()

# B column is large expenses input

large_spending = int(input("How much did you spend in large expenses? If none, enter '0'. \n"))

def getBcol():
        sheet['B{}'.format(nextrow)] = large_spending

getBcol()

# C column is daily expenses input

daily_spending = int(input("How much did you spend today? If none, enter '0'. \n"))
net = 0
svg = 0
def getCcol():
        sheet['C{}'.format(nextrow)] = daily_spending

getCcol()

def determineNet(db):
        global net
        global svg
        gross = db - daily_spending
        if gross >= 8:
                svg = 2
                net = gross - svg
        elif 6 > gross >= 3:
                svg = 1
                net = gross - svg
        elif 3 > gross
                svg = 0
                net = gross

determineNet(15)

# D column is large expense fund remaining (col D maxrow - large_spending +/- remainder from daily)

def getDcol()
        sheet['D{}'.format(nextrow)] = (sheet['D{}'.format(maxrow)] - large_spending + net)

getDcol()

# E column is accumulated savings for the period

def getEcol()
        sheet['E{}'.format(nextrow)] = (sheet['E{}'.format(maxrow)] + svg)

getEcol()

# save and close workbook


