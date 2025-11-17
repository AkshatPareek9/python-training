def reverse_list(lst):
  if len(lst) == 0:
    return []
  else:
    lst[-1]+reverse_list(lst[:-1])

my_list=[1,2,3,4,5]
rev_list = reverse_list(my_list)

#o/p: [5,4,3,2,1]
