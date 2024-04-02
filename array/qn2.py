# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the list in alphabetical order

# 1. Length of the list
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print("List after adding at the end of the list",heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
heros.pop()
heros.insert(3,"black panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
del heros[1:3]
heros.insert(1,"doctor strange")

# 5. Sort the list in alphabetical order
heros=sorted(heros)
print(heros)