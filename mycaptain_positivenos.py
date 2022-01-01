no_of_terms=int(input('Enter the number of terms: '))
list1=[]
list2=[]
print('Enter',no_of_terms,' number of terms.')
for i in range(no_of_terms):
    list1.append(int(input('Term: ')))
for i in list1:
    if i >0:
        list2.append(i)
print(list2)