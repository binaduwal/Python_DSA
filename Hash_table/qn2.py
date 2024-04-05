# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#    Figure out data structure that is best for this problem

dict={}
with open("Hash_table/nyc_weather.csv","r") as f:
    for line in f:
        tokens=line.split(",")
        day=tokens[0]
        temperature=int(tokens[1])
        dict[day]=temperature

 #(a) What was the temperature on Jan 9?
print("The temperature on Jan 9 was",dict["Jan 9"])

#    (b) What was the temperature on Jan 4?
print("The temperature on Jan 9 was",dict["Jan 4"])
