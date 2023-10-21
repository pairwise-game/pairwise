import proj_plane as PP

#  Set the order of the projective plane, must be prime
#  number of "cards" (and symbols) will be order^2 + order + 1
#  number of things on each "card" will be order + 1
#  total number of occurences of any element will be order + 1
order = 5
D = PP.make_deck(order)
D = PP.index_from_one(D)
D = PP.format_deck(D, 'readable', True)
PP.file_output(D, 'test.txt')
for i in D:
    print(i)
