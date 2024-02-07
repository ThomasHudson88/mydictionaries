import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()
print(phonebook)
print(len(phonebook))

mydict = {}                 #this is will create an empty dictionary
mydict = dict(m=8,n=9)      #m and n are the keys and 8, 9 are the values
print(mydict)
num = mydict['m'] + mydict['n']
print(num)



print()
print('*****  end section 1 ********')
print()


print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'chris'

if name in phonebook:
    print(f"Name: {name} Phone Number: {phonebook[name]}")
else:
    print(f"{name} is not in the phone book")






print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Joe'] = '555-0123'
phonebook["Chris"] = '555-4444'

print(phonebook)

#can add a key or replace
#we would have to delete "Chris" and add in "chris" for the key value update for the case
#order of the pairs does not matter, random access, with the key we know where to go, not sequential


print()
print('*****  end section 3 ********')
print()




print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()




print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"The key is: {key} and the value is {phonebook[key]}")

for value in phonebook.values():
    print(value)

for key, vlaue in phonebook.items():
    print(f"The key is {key} and the vlaue is {value}")

for item_touple in phonebook.items():
    print(item_touple)


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()
#this method gives a defualt if there is an error

phone = phonebook.get('chris','defualt')
print(phone)
#if the key is nt found will get the defualt

phonebook.clear()
print(phonebook)
#clears out all of the key value pairs in the dictionary




print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
remove  = phonebook.pop('Chris', 'not found')
print(remove)
print(phonebook)
#dictionary is getting shorter and shorter, maybe remove them as processed




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()
#give both the key and value pair at the same time
print(phonebook)
a = phonebook.popitem()
print(a)
print(phonebook)
#always takng the last key value pair in the dictionary, supposed to be random




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

#How to use the random method with a dictionary, use a work around, we can make a list out of dictionary
#list_of_keys = list(phonebook) #defualt is the keys
#print(list_of_keys) #prints the three names

#random_key = random.choice(list_of_keys) #we imported random at the beggining
#print(random_key)
#print(phonebook[random_key])

print(f"Random Number: {phonebook[random.choice(list(phonebook))]}")


print()
print('*****  end section 9 ********')
print()

'''