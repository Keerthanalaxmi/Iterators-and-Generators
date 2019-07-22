# Iterators-and-Generators

Iterators:
      > Iterable is an object which one can iterate over. It creates an iterator object when passed to iter method. Iterator object can be iterated over using next() method.
      
      For example, List in python is an iterable which can be iterated over using for function.
      When a for loop is executed, for statement calls iter() on the object, which it is supposed to loop over. If this call is successful, the iter call will return an iterator object that defines the method __next__(), which accesses elements of the object one at a time. The __next__() method will raise a StopIteration exception, if there are no further elements available
