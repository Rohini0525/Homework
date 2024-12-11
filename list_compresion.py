# square of range
list=[i**2 for i in range(5)]
print(list)

#Even number in range
list1=[i for i in range(10) if i%2==0]
print(list1)

#Odd number in range
list2=[i for i in range(10) if i%2!=0]
print(list2)

#Transform Elements
Names=["rohini" , "sarphale"]
Capitalize=[name.capitalize() for name in Names]
print(Capitalize)

book_list = ['Data Structure',"Data Structure", 'Algorithm', 'Web dev']
#book_list.count('Data Structure')
#print(book_list.count('Data Structure'))
book_list.remove('Data Structure')
print(book_list)      

