#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  single_nums = []
  for n in nums:
      if not n in single_nums:
          single_nums.append(n)
  return single_nums
          
def remove_adjacent2(nums):
  removed_list = []
  numberHolder = None
  for number in nums:
    if number != numberHolder:
       removed_list.append(number)
       numberHolder = number
  return removed_list
  
#more info http://stackoverflow.com/questions/2488651/trouble-with-this-python-newbie-exercise-using-lists-and-finding-if-two-adjacen

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

#a naive solution (log(n))
def linear_merge(list1, list2):
  # +++your code here+++
  return sorted(list1 + list2)


#better solution

def mergeSortedLists(a, b):
    l = []
    while a and b:
        if a[0] < b[0]:
            l.append(a.pop(0))
        else:
            l.append(b.pop(0))
    return l + a + b

#more info http://stackoverflow.com/questions/4173225/my-implementation-of-merging-two-sorted-lists-in-linear-time-what-could-be-imp

#probably best solution:
"""
Here's a generator approach. You've probably noticed that a whole lot of these "generate lists" can be done well as generator functions. They're very useful: they don't require you to generate the whole list before using data from it, to keep the whole list in memory, and you can use them to directly generate many data types, not just lists.

This works if passed any iterator, not just lists.

This approach also passes one of the more useful tests: it behaves well when passed an infinite or near-infinite iterator, eg. linear_merge(xrange(10**9), xrange(10**9)).

The redundancy in the two cases could probably be reduced, which would be useful if you wanted to support merging more than two lists, but for clarity I didn't do that here.
"""

def linear_merge2(list1, list2):
    """
    >>> a = [1, 3, 5, 7]
    >>> b = [2, 4, 6, 8]
    >>> [i for i in linear_merge(a, b)]
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> [i for i in linear_merge(b, a)]
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> a = [1, 2, 2, 3]
    >>> b = [2, 2, 4, 4]
    >>> [i for i in linear_merge(a, b)]
    [1, 2, 2, 2, 2, 3, 4, 4]
    """
    list1 = iter(list1)
    list2 = iter(list2)

    value1 = next(list1)
    value2 = next(list2)

    # We'll normally exit this loop from a next() call raising StopIteration, which is
    # how a generator function exits anyway.
    while True:
        if value1 <= value2:
            # Yield the lower value.
            yield value1
            try:
                # Grab the next value from list1.
                value1 = next(list1)
            except StopIteration:
                # list1 is empty.  Yield the last value we received from list2, then
                # yield the rest of list2.
                yield value2
                while True:
                    yield next(list2)
        else:
            yield value2
            try:
                value2 = next(list2)

            except StopIteration:
                # list2 is empty.
                yield value1
                while True:
                    yield next(list1)


# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
    

  #print 'remove_adjacent'
  #test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  #test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  #test(remove_adjacent([]), [])
  #print 'remove_adjacent2'
  #test(remove_adjacent2([1, 2, 2, 3]), [1, 2, 3])
  #test(remove_adjacent2([2, 2, 3, 3, 3]), [2, 3])
  #test(remove_adjacent2([]), [])

  #print
  #print 'linear_merge'
  #test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
   #    ['aa', 'bb', 'cc', 'xx', 'zz'])
  #test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
  #     ['aa', 'bb', 'cc', 'xx', 'zz'])
  #test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
  #     ['aa', 'aa', 'aa', 'bb', 'bb'])
  #print 'other linear_merge'
  #test(mergeSortedLists(['aa', 'xx', 'zz'], ['bb', 'cc']),
  #     ['aa', 'bb', 'cc', 'xx', 'zz'])
  #test(mergeSortedLists(['aa', 'xx'], ['bb', 'cc', 'zz']),
  #     ['aa', 'bb', 'cc', 'xx', 'zz'])
  #test(mergeSortedLists(['aa', 'aa'], ['aa', 'bb', 'bb']),
  #     ['aa', 'aa', 'aa', 'bb', 'bb'])

  foo = 'foo'
  foo = 'hello word';
  
  print 'linear_merge'
  test(linear_merge2(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])



if __name__ == '__main__':
  main()
