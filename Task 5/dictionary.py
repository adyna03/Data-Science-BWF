# dict={'a':'apple', 'b':'banana', 'c':'carrot'}
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# dict.update({'e':'elephant', 'f':'fan'})
# print(dict)

# to create a dict from a seq
# mapping = {}
# for key, value in zip(key_list, value_list):
#  mapping[key] = value
#  zip “pairs” up the elements of a number of lists, tuples, or other sequences to create a list of tuples

tuples=zip(range(5), reversed(range(5)))
dic=dict(tuples)
print(dic)
