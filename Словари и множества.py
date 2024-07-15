#----Dictionary-----
my_dict = {'Fedor':2004, 'Artem':2000}
print('Dict:',my_dict)
print('Existing value:',my_dict['Fedor'])
print('Not existing value:',my_dict.get('Eva', 'Такого ключа нет'))
my_dict.update({'Sasha':2011,
                'Dima':2003})
print('Deleted value:',my_dict.pop('Artem'))
print('Modified dictionary:',my_dict)
#----------Set-----------
my_set = {1,2,3,8,9,8,5,3,2,True,False,'Fedor',(1,2,3)}
print('Set:',my_set)
my_set.add(54), my_set.add('Eva')
my_set.discard(False)
print('Modified set:',my_set)