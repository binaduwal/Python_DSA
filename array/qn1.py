# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,


# 1. In Feb, how many dollars you spent extra compare to January?
months=[{
        "january":2200,
        "february":2350,
        "march":2600,
        "april":2130,
        "may":2190
    }]
index=months[0]
amount=[]
for key in index:
    value=index[key]
    amount.append(value)
# print(amount)  #amount of months in list
1.   
extra=amount[1]-amount[0]
print(f"In feb,${extra} is spent extra compare to january.")

2.
total_expense=amount[0]+amount[1]+amount[2]
print("Total expense of three month is",total_expense)

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spend exactly 2000$ in any month?",2000 in index)

print("Before adding june:",months) #after adding june in dictionary

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
index["june"]=1980
print("After adding june:",months) #after adding june in dictionary

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
index["april"]=index["april"]-200
print(months)