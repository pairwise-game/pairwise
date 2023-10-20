# Implementing from https://blog.polettix.it/some-maths-for-dobble/

# Move comments to notes

# only prime order
# number of coords will be order^2 + order + 1
# projective plane order n is a Steiner system S(2, n+1, n^2+n+1)

# from all possible triples, (0,0,0) to (n,n,n) skip:
#  - (0,0,0)
#  - tuples that are multiples of other tuples, ie (0,0,1) and (0,0,2)

# algo: start counting, jump elements whose leftmost non-0 element != 1
import itertools


def f(t):
    match t:
        case (0,0,0):
            return False
        case(x,y,z) if x > 1:
            return False
        case(0,y,z) if y > 1:
            return False
        case(0,0,z) if z > 1:
            return False
        case _:
            return True

def homog_coords(order):
    trips = [i for i in itertools.product(range(order), repeat=3)]
    return list(filter(lambda x: f(x), trips))

def dotprod(x,y, order):
    return (x[0]*y[0] + x[1]*y[1] + x[2]*y[2]) % order

def make_deck(order):
    H = homog_coords(order)
    deck = []
    for i in range(len(H)):
        card = [H.index(n) for n in H if dotprod(n, H[i], order) == 0]
        deck.append(card)
    return deck

#  Some testing
def main():
    assert len(homog_coords(3)) == 13
    assert len(homog_coords(11)) == 133

    A = make_deck(3)
    print(A)


if __name__ == '__main__':
    main()