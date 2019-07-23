# Iterators-and-Generators

Iterators:
      > Iterable is an object which one can iterate over. It creates an iterator object when passed to iter method. Iterator object can be iterated over using next() method.
      
For example, List in python is an iterable which can be iterated over using for function.When a for loop is executed, for statement calls iter() on the object, which it is supposed to loop over. If this call is successful, the iter call will return an iterator object that defines the method __next__(), which accesses elements of the object one at a time. The __next__() method will raise a StopIteration exception, if there are no further elements available

Program:

      An iterator class reverse_iter, that takes a list and iterates it from the reverse direction.
      
      
Generators:
      The above iterator looks cool. But writing a function with __iter__ and __next__ is tedious and we need to keep track of every internal variables between calls. What if a single statement could do that for you. Generators come in to action. Using Yield keyword, we can accomplish the same thing iterators are doing.
      
Taken from Internet: Below are the pros of having a generators in our program:      
      >Generator function contains one or more yield statement.
      >When called, it returns an object (iterator) but does not start execution immediately.
      >Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
      >Once the function yields, the function is paused and the control is transferred to the caller.
      >Local variables and their states are remembered between successive calls.
      >Finally, when the function terminates, StopIteration is raised automatically on further calls

Program:

      An generator program to reverse the string using yield statement.
