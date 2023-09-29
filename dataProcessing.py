# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Python 888888888888888888888888")
###Sdding new model to Fraud Detection
###AAAAAAAAAAAAAAAAAAAAAAAAa
##SSSSSSSSSSSSS

tupleSample = ('text','para')
listSample = ['123','456']
dictSample = {'1':'AI','2':'ML'}

print(tupleSample)
print(listSample)
print(dictSample)

print(dictSample['2'])
dictSample['3']='DataScience'
print(dictSample)

#for loops

for i in range(1,5):
    print(i)
    
print("------------------")   
#for loop with step counter
for i in range(1,10,2):
    print(i) #prints all 3 numbers

print("------------------")  
sampleText = "This is a sample text"
#loop thru text
for char in sampleText:
    print(char)
    
#print a pattern
str=""
for i in range(0,9):
    if(i<=5):
        str+="*"
        print(str)
    elif i>4:
        str=str[:-2]
        print(str)


print("------------------") 
#loop enumeration
for n,i in enumerate(sampleText):
    print(i,n)
    
    
print("------------------")     
for i in range(100):
    print (i)
    if i>50:
        continue
        print("Hello")
    
print("------------------")   
#Odd and Even check and consoldiation
sampleNum = '498127310831247102410958245930458340'    
oddNums = ''
evenNums = ''

for nums in sampleNum:
    if int (nums)%2==0:
        evenNums += nums
    else:
        oddNums += nums
        
print("Odd",oddNums)
print('Even',evenNums)


#sentence Split
print("------------------")   
myText = "Why is #python so #trending now or has it been like this #always"
for eachWord in myText.split('#'):
    print(eachWord)
    
for word in myText.split():
    if word.startswith('#'):
        print(word)
        
        
print("-----------------------------")
students_data = {1:['Shivam Bansal', 24] , 2:['Udit Bansal',25], 3:['Sonam Gupta', 26], 4:['Saif Ansari',24], 5:['Huzefa Calcuttawala',27]}
for key,value in students_data.items():
    print(key, value)


print("-----------------------------")    
increment = 12
displ = 1
while displ <90:
    displ += increment
print("Total Display",displ)    

print("-----------------------------")  
d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
for i in d:
    print(i)
    
d = {0, 1, 2}
for x in d:
    print("-------",d.add(x))
    
print("-----------------------------")
#while loop concepts

