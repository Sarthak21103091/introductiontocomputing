#question 1
string='Python is a case sensitive language'

#part a
length=len(string)
print(length)

#part b
print(string[::-1])

#part c
new_string=string[10:26]
print(new_string)

#part d
print(string.replace('a case sensitive','object oriented'))

#part e
print(string.index('a'))

#part f
print(string.replace(' ',''))



#question 2
print('name')
n1=input()

print('sid')
n2=input()

print('department')
n3=input()

print('cgpa')
n4=input()

#now print a string containing required data
print('Hey',n1,'Here!')
print('my sid is',int(n2))
print('I am from',n3,'department and my cgpa is',n4)


#question 3
a=56
b=10

#a
print(a&b)

#b
print(a|b)

#c
print(a^b)

#d
print(a<<2)
print(b<<2)

#e
print(a>>2)
print(b>>4)


#question 4
num1=float(input('enter the first number:'))
num2=float(input('enter the second number:'))
num3=float(input('enter the third number:'))

if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3

print('largest number is:',largest)


#question 5
str='my name is sarthak'

if 'name' in str:
    print('yes')
else:
    print('no')


#question 6
num1=int(input('enter the length of first side'))
num2=int(input('enter the length of second side'))
num3=int(input('enter the length of third side'))

if num1+num2>num3 and num2+num3>num1 and num3+num1>num2:
    print('yes,a triangle can be formed')
else:
    print('no,a triangle cannot be formed')
    
    
