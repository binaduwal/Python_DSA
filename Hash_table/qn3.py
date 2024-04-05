# Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8

arr={}
with open("Hash_table/poem.txt","r") as f:
    for line in f:
        words=line.split()
        for word in words:
            print(word)
            if word in arr:
                arr[word] += 1
            else:
                arr[word]=1

for word,count in arr.items():
    print(f"{word}:{count}")
