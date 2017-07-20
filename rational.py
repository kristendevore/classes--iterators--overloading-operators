# Submitter: devorek(DeVore, Kristen)
# Partner  : brizam(Martin del Campo, Briza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from goody import irange, type_as_str
import math
from _ast import Num
from tkinter.constants import OUTSIDE

class Rational:
    
    @staticmethod
    # Called as Rational._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    def _gcd(x : int, y : int) -> int:
        assert type(x) is int and type(y) is int and x >= 0 and y >= 0,\
          'Rational._gcd: x('+str(x)+') and y('+str(y)+') must be integers >= 0'
        while y != 0:
            x, y = y, x % y
        return x
    
    @staticmethod
    # Called as Rational._validate_arithmetic(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Rational or int is...
    # Rational._validate_arithmetic(right, {Rational,int},'+','Rational',type_as_str(right))
    def _validate_arithmetic(v : object, t : {type}, op : str, left_type : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+left_type+'\' and \''+right_type+'\'')        

    @staticmethod
    # Called as Rational._validate_relational(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v : object, t : {type}, op : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Rational() '+op+' '+right_type+'()') 
                   
    
    def __init__(self, num = 0, denom = 0):
        
        if type(num) != int:
            raise AssertionError('Rational.__init__ numerator is not int: '+ str(num))
        elif type(denom) != int:
            raise AssertionError('Rational.__init__ denominator is not int: ' + str(denom))
        elif denom == 0:
            raise AssertionError(('Rational.__init__ denominator cannot be zero'))
        elif num == 0:
            self.num = num
            self.denom = 1
    
        else:
            if denom < 0:
                num =  -(num)
                denom = abs(denom)
                
            self.num = num//Rational._gcd(abs(num),denom)
            #print(self.num)
            
            self.denom = denom//Rational._gcd(abs(num),denom)
         #   print(self.denom)
            
    def __str__(self):
        return('{}/{}'.format(self.num, self.denom))   

    def __repr__(self):
        return('Rational({},{})'.format(self.num, self.denom))     
        
    def __bool__(self):
        if ('{},{}'.format(self.num, self.denom)) == (0,1):
            return False
        elif self.num == 0:
            return False
        else:
            return True
        
    def __getitem__(self,value):
        if type(value) == int:
            if value ==  0:
                return self.num
            elif value == 1:
                return self.denom
            else:
                raise TypeError('Rational.__getitem__ index value is incorrect')

        if type(value) == str:
            value_new = value.lower()
            if value_new in ('numerator'):
                return self.num   
            elif value_new in ('denominator'):
                return self.denom
            else:
                raise TypeError('Rational.__getitem__ index value is incorrect')
            
    def __pos__(self):
        return(Rational(self.num, self.denom))

    def __neg__(self):
        return(Rational(-self.num,self.denom))
    
    def __abs__(self):
        return(Rational(abs(self.num),abs(self.denom)))
    
    def __add__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__add__ value attempted to add is incorrect')
        else:
            if type(value) == int:
                new =  Rational(value,1)
                new_num = new.num * self.denom
                final_num = new_num + self.num
                return(Rational(final_num,self.denom))
            else:
                new_self_num = self.num * value.denom
                new_self_denom = self.denom * value.denom
                new_value_num = value.num * self.denom
                final_num = new_self_num + new_value_num
                return(Rational(final_num,new_self_denom))
            
    def __radd__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__radd__ value attempted to add is incorrect')
        else:
            if type(value) == int:
                new =  Rational(value,1)
                new_num = new.num * self.denom
                final_num = new_num + self.num
                return(Rational(final_num,self.denom))
            else:
                new_self_num = self.num * value.denom
                new_self_denom = self.denom * value.denom
                new_value_num = value.num * self.denom
                final_num = new_self_num + new_value_num
                return(Rational(final_num,new_self_denom))
            
    def __sub__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__sub__ value attempted to subtract is incorrect')
        else:
            if type(value) == int:
                new =  Rational(value,1)
                new_num = new.num * self.denom
                final_num = new_num - self.num
                if new_num > self.num:
                     return(Rational(-final_num,self.denom))
                else:
                     return(Rational(final_num,self.denom))     
            else:
                new_self_num = self.num * value.denom
                new_self_denom = self.denom * value.denom
                new_value_num = value.num * self.denom
                final_num = new_self_num - new_value_num
                return(Rational(final_num,new_self_denom))
            
    def __rsub__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__rsub__ value attempted to subtract is incorrect')
        else:
            if type(value) == int:
                new =  Rational(value,1)
                new_num = new.num * self.denom
                final_num = new_num - self.num
                if new_num < self.num:
                    return(Rational(-final_num,self.denom))
                else:
                     return(Rational(final_num,self.denom))
            else:
                new_self_num = self.num * value.denom
                new_self_denom = self.denom * value.denom
                new_value_num = value.num * self.denom
                final_num = new_self_num - new_value_num
                return(Rational(final_num,new_self_denom))
            
    def __mul__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__mul__ value attempted to multiply is incorrect')
        else:
            if type(value) == int:
                new = Rational(value, 1)
                new_num = new.num * self.num
                return(Rational(new_num,self.denom))
            else:
                final_num = value.num * self.num
                final_denom = value.denom * self.denom
                return(Rational(final_num, final_denom))
    def __rmul__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__rmul__ value attempted to multiply is incorrect')
        else:
            if type(value) == int:
                new = Rational(value, 1)
                new_num = new.num * self.num
                return(Rational(new_num,self.denom))
            else:
                final_num = value.num * self.num
                final_denom = value.denom * self.denom
                return(Rational(final_num, final_denom))
    
    def __truediv__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__truediv__ value attempted to divide is incorrect')
        else:
            if type(value) == int:
                new = Rational(value,1)
                new_num = new.num * self.denom
                return(Rational(self.num,new_num)) 
            else:
                new_num = self.denom * value.num
                new_denom = self.num * value.denom
                return(Rational(new_denom,new_num))
            
    def __rtruediv__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__rtruediv__ value attempted to divide is incorrect')
        else:
            if type(value) == int:
                new = Rational(value,1)
                new_num = new.num * self.denom
                return(Rational(new_num,self.num))
            else:
                new_num = self.denom * value.num
                new_denom = self.num * value.denom
                return(Rational(new_num,new_denom))
            
    def __pow__(self,value):
        if type(value) != int:
            raise TypeError('Rational.__pow__ value attempted to take power is incorrect')
        else:
            
            if value > 0: 
                new_denom = self.denom ** value
                return Rational(self.num,new_denom)
            else:
                new_num = self.num ** abs(value)
                return Rational(self.denom,new_num)
            
    def __eq__(self,value):
        if type(value) not in (Rational, int):
            raise TypeError('Rational.__eq__ value attempted to calculate is not an int or Rational type')
        else:
            if type(value) == int:
                new_num = Rational(value,1)
                if new_num.num == self.num and new_num.denom == self.denom:
                    return True
                else:
                    return False
            else:
                if value.num == self.num and value.denom == self.denom:
                    return True
                else:
                    return False
                
    def __ne__(self,value):
        if type(value) not in (Rational,int):
            raise TypeError('Rational.__ne__ value attempted to calculate is not an int or Rational type')
        else:
            if type(value) == int:
                new_num = Rational(value,1)
                if new_num.num == self.num and new_num.denom == self.denom:
                    return False
                else:
                    return True
            else:
                if value.num == self.num and value.denom == self.denom:
                    return False
                else:
                    return True
                
    def __lt__(self,right): 

        if type(self) is Rational and type(right) is Rational:
            new_self_num = self.num * right.denom
            new_self_denom = self.denom * right.denom
            new_value_num = right.num * self.denom
            new_value_denom = right.denom * self.denom
            return(int(new_self_num) < int(new_value_num))
              
        elif type(self) is Rational and type(right) in [int]:
            new_num = Rational(right,1)
            new_value_num = new_num.num * self.denom
            return(int(self.num) < int(new_value_num))
#         
        elif type(self) == int and type(right) is Rational:
            new_num = Rational(self,1)
            new_value_num = new_num.num * right.denom
            return(new_value_num < right.num)

   
        else:
            raise TypeError('Rational.__lt__ value attempted to see if less than is not an int or Rational type')           
        
    def __gt__(self,right):
        if type(self) is Rational and type(right) is Rational:
            new_self_num = self.num * right.denom
            new_self_denom = self.denom * right.denom
            new_value_num = right.num * self.denom
            new_value_denom = right.denom * self.denom
            return(int(new_self_num) > int(new_value_num))
              
        elif type(self) is Rational and type(right) in [int]:
            new_num = Rational(right,1)
            new_value_num = new_num.num * self.denom
            return(int(self.num) > int(new_value_num))
#         
        elif type(self) == int and type(right) is Rational:
            new_num = Rational(self,1)
            new_value_num = new_num.num * right.denom
            return(new_value_num > right.num)

   
        else:
            raise TypeError('Rational.__gt__ value attempted to see if greater than is not an int or Rational type') 
        
    def __le__(self,right):
        if type(self) is Rational and type(right) is Rational:
            new_self_num = self.num * right.denom
            new_self_denom = self.denom * right.denom
            new_value_num = right.num * self.denom
            new_value_denom = right.denom * self.denom
            return(int(new_self_num) <= int(new_value_num))
              
        elif type(self) is Rational and type(right) in [int]:
            new_num = Rational(right,1)
            new_value_num = new_num.num * self.denom
            return(int(self.num) <= int(new_value_num))
#         
        elif type(self) == int and type(right) is Rational:
            new_num = Rational(self,1)
            new_value_num = new_num.num * right.denom
            return(new_value_num <= right.num)
        
        else:
            raise TypeError('Rational.__le__ value attempted to see if less than or equal to is not an int or Rational type')
        
    def __ge__(self,right):
        if type(self) is Rational and type(right) is Rational:
            new_self_num = self.num * right.denom
            new_self_denom = self.denom * right.denom
            new_value_num = right.num * self.denom
            new_value_denom = right.denom * self.denom
            return(int(new_self_num) >= int(new_value_num))
              
        elif type(self) is Rational and type(right) in [int]:
            new_num = Rational(right,1)
            new_value_num = new_num.num * self.denom
            return(int(self.num) >= int(new_value_num))
#         
        elif type(self) == int and type(right) is Rational:
            new_num = Rational(self,1)
            new_value_num = new_num.num * right.denom
            return(new_value_num >= right.num)
        
        else:
            raise TypeError('Rational.__ge__ value attempted to see if greater than or equal to is not an int or Rational type') 
    
    def __setattr__(self, name, item):
        values_dict = ['num', 'denom']
        if name in self.__dict__:
            raise NameError('Rational.__setattr__ value of attribute cannot be changed')
        elif name not in values_dict:
            raise NameError('Rational.__setattr__ new attributes cannot be created')
        self.__dict__[name] = item
    
    def __call__(self,item):
        inside = self.num
        outside = self.denom
        final = []
        count = item 
        new_str = '.'
        newer_str = '.1'
        original_str = ''
        if inside < outside:
            while len(final) != item: 
                inside*=10
                multiple=inside//outside
                final.append(multiple)
                new_outside = outside*multiple
                new_inside = inside - new_outside
                inside = new_inside
            for item in final:
                new_str += str(item)
            return new_str
        
        elif inside > outside:
            
            original_str += str(inside//outside)

            while len(final) != item: 
                inside*=10
                multiple=inside//outside
                final.append(multiple)
                new_outside = outside*multiple
                new_inside = inside - new_outside
                inside = new_inside
            original_str += newer_str
            #print(final)
            for item in final[1:]:
                original_str += str(item)
            return original_str
                
        else:
            raise TypeError('Rational.__call__ cannot be done')



 
def compute_e(n):
    answer = Rational(1)
    for i in irange(1,n):
        answer += Rational(1,math.factorial(i))
    return answer

# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer
    
    answer = Rational(1,2)
    x      = Rational(1,2)
    for i in irange(1,n):
        big = 2*i+1
        answer += Rational(prod(range(1,big,2)),prod(range(2,big,2)))*x**big/big       
    return 6*answer

if __name__ == '__main__':
    #Simple tests before running driver

  #  x = Rational(500,4) 
   # print(x.__call__(2))
    #print(x+x)
    #print(2*x)
    #print(x(30))
    
    print()
    import driver    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
