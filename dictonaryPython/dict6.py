# Q.Write a Python program to remove duplicates from the dictionary.



student_data = {'id1': 
   {'name': ['sourabh'], 
    'class': ['12'], 
    'subject': ['english, math, science']
   },
 'id2': 
  {'name': ['vivek'], 
    'class': ['12'], 
    'subject': ['english, math, science']
   },
 'id3': 
    {'name': ['yash'], 
    'class': ['12'], 
    'subject': ['english, math, science']
   },
 'id4': 
   {'name': ['shivam'], 
    'class': ['12'], 
    'subject': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)