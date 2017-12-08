# budget
A small project I completed to help me budget, and also practice using Python's I/O features. 

A static daily budget is set at $15. A 'large expenses' fund is initialized at a given number (in the sample file, it is set to 150). 
User is prompted to enter money spent, if any, from the large expenses fund. This amount is subtracted from the last listed amount in the large_expenses.txt file, and the updated amount is appended to the text document. 
User is then promted to input money spent from $15 daily budget. Any remainder, when expenses are subtracted from budget, is added to the last item in the large_expenses file, and the new amount appended. Any amount spent over budget is subtracted from the large_expenses item, in the same way. The amount spent that day is then appended to the budgetlines.txt file, to keep track of spending over the budget period.

Functionality for adding some money to a savings account added 12/7/17 to branch budget-plus-savings. If daily netgain is greater than or equal to $10, $2 is sent to a savings file, and the rest is added to the large expenses fund. $1 is added to savings if netgain is between $5 and $9. No money is sent to savings if netgain is less than $5. 
