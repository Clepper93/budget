#import daily expenditures from file, define daily_spending
f = open('budgetlines.txt','r+')
daily_spending = []
for line in f:
    if line == "\n": #skip blank lines
        pass
    else:
        daily_spending.append(int(line))
#import large expenses from file, define large_expenses
e = open('large_expenses.txt','r+')
large_expenses_file = []
for line in e:
    if line == "\n":
        pass
    else:
        large_expenses_file.append(int(line))
large_expenses = large_expenses_file[-1] #work only with last item in list
#define daily_budget, does not change from day to day
daily_budget = 15
#determine if any money in large expenses fund was spent, and subtract from fund
large_spending = int(input("How much did you spend in large expenses? If none, enter '0'. \n"))
large_expenses -= large_spending
#determine if day was net savings or loss; add or subtract budget remainder from large expenses fund
expensereport = int(input("How much did you spend today? \n"))
netgain = (daily_budget - expensereport)
netloss = (expensereport - daily_budget)
if expensereport < daily_budget:
    large_expenses += netgain
    print("You saved ${}! Money in large expenses fund now ${}.".format(netgain,large_expenses))
    e.write("\n" + str(large_expenses))
elif expensereport > daily_budget:
    large_expenses -= netloss
    print("You overspent by ${}. Money in large expenses fund now ${}.".format(netloss, large_expenses))
    e.write("\n" + str(large_expenses))
else:
    large_expenses += 0
    print("You stayed exactly on budget. No net loss or gain.")
    e.write("\n" + str(large_expenses))
f.write("\n" + str(expensereport))
f.close()
e.close()

