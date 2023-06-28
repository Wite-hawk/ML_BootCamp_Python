# Assignment 18

# Q1
def hours():
    print('Open 9-5 daily')

# Also done in interacive interpreter
import zoo
zoo.hours()

# Q2
import zoo as menagerie
menagerie.hours()

# Q3
from zoo import hours as info

# Q4
info()

# Q5
plain_dict = {'a': 1, 'b': 2, 'c': 3}
print(plain_dict)

# Q6
from collections import OrderedDict

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

# Q7
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])


