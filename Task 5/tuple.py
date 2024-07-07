planet='saturn'
tup=tuple(planet)
print(tup)


seq=((1, 3, 5), (2, 4, 6), (5, 10, 15))
for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')

# use either *rest or *_ for accessing rest of variables in a seq
a, *rest = seq
print(a)
print(rest)
