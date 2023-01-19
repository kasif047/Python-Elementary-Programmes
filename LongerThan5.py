noOfStrgs= int(input('Enter the no. of names you want to give: '))
lst = []
for i in range(1,noOfStrgs+1):
  a = input(f'Enter the name no. {i}').strip()
  lst.append(a)
print(lst)
def nam(a):
    if len(a)>5:
      return True
    else:
      return False 
for name in lst:
  print(f' length of {name} is greater than 5 : {nam(name)}')
  
     
