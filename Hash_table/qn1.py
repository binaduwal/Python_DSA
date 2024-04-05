# contains new york city weather for first few days in the month of January. Write a program that can answer following,
# Figure out data structure that is best for this problem
arr=[]
with open("Hash_table/nyc_weather.csv",'r') as f:
    for line in f:
        tokens=line.split(",")
        temp=int(tokens[1])
        arr.append(temp)
    print(arr)

# What was the average temperature in first week of Jan
average=sum(arr[0:7])/len(arr[0:7])
print("The average temperature in first week of Jan was",average)

# Figure out data structure that is best for this problem
maximum=max(arr[0:10])
print("The maximum temperature in first 10 days of Jan was",maximum)