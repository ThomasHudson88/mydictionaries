#Create a Student Dictionary

Student = {'Name' : 'Thomas',
           'Age' : 23 ,
           'Major': 'Accounting',
           'hobbies': ['reading','running','archery']}

#Add State to the dictionary
Student['State'] = 'Texas'

#Add 1 to the age
Student['Age'] += 1

#iterate over the key-value pairs in the student dictionary and print each pair on a new line
for key, value in Student.items():
    print(f"The key is: {key}, and the value is: {value}\n")