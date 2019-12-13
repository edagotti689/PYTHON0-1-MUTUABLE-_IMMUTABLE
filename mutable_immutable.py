n = 123
print(id(n))
n = 222
print(id(n))

# For string
name = 'sri'
print(' \n name id :', id(name))
name = 'ram'
print(' \n name id :', id(name))

# For List
names = ['sri','ram','balu']
print(' \n names id :', id(names))
names.append('nagesh')
print(' \n names id :', id(names))
print(' \n names :', names)


# For set
names = {'sri','ram','balu'}
print(' \n set id :', id(names))
names.add('OK')
print(' \n set id :', id(names))
print(' \n names :', names)

# For List
emp_det = {'name':'sri','dname':'IT'}
print(' \n emp_det id :', id(emp_det))
emp_det['eid'] = 45
print(' \n emp_det id :', id(emp_det))
print(' \n emp_det :', emp_det)


