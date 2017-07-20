# Submitter: devorek(DeVore, Kristen)
# Partner  : brizam(Martin del Campo, Briza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from collections import defaultdict
from goody import type_as_str


class Bag:
    def __init__(self, contents = 0):
        self.dictionary = defaultdict(int)
        
        if contents != 0:
            for k in contents:
                if k in self.dictionary:
                    self.dictionary[k] += 1
                else:
                    self.dictionary[k] = 1
   
    
    def __repr__(self) -> str:
        empty_str = ''
        new_list = []
        for k,v in self.dictionary.items():
            empty_str += (str(k) +' ') *v
        for item in empty_str.split():
            try:
                if int(item):
                    new_list.append(int(item))
            except ValueError:
                new_list.append(item)
        return 'Bag({})'.format(new_list)   
    
    def __str__(self) -> str:
        empty_str = ''
        for k,v in self.dictionary.items():
            empty_str += '{}[{}],'.format(k,v)
        return 'Bag({})'.format(empty_str[:-1])
    def __len__(self) -> int:
        count = 0 
        for v in self.dictionary.values():
            count += v
        return count
    def unique(self) -> int:
        count = 0
        for item in self.dictionary.keys():
            count += 1
        return count
    def __contains__(self, c) -> bool:
        return c in self.dictionary
    def count(self, c) -> int:
        item = 0
        if c in self.dictionary:
            item = self.dictionary[c]
        else:
            item = 0
        return item
    def add(self, c):
    
        if c in self.dictionary.keys():
            self.dictionary[c] += 1
        else:
            self.dictionary[c] = 1
            
    def remove(self,c):
        if c in self.dictionary.keys():
            self.dictionary[c] -= 1
            if self.dictionary[c] == 0:
                del self.dictionary[c]
        else:
            raise ValueError
    def __add__(self, variable):
        empty_list = []
        empty_str = ''
        if type(variable) == Bag:
            for k,v in self.dictionary.items():
                empty_str += (str(k) + ' ')*v
            for k,v in variable.dictionary.items():
                empty_str += (str(k) + ' ')*v
            for item in empty_str.split():
                try:
                    if int(item):
                        empty_list.append(int(item))
                except ValueError:
                    empty_list.append(item)
            return Bag(empty_list)
            
       
        else:
            raise TypeError('error in add operator of bag class')
#        
        
    def __eq__(self, c):
         return self.dictionary == c
    def __ne__(self,c):
        return self.dictionary != c
    
    def __iter__(self):
        def gen(values):
            for value in values.keys():
                for thing in range(values[value]):
                    yield value
        values = dict(self.dictionary)      
        return gen(values)
              #  print(value)

if __name__ == '__main__':
  #  x  = Bag[]
    #print('testing')
   # x = Bag([4,5,6])
    #print(x)
    #print(Bag())
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
