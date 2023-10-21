# Implementing from https://blog.polettix.it/some-maths-for-dobble/

# TODO: Move background/notes to markdown

# only prime order
# number of coords will be order^2 + order + 1
# projective plane order n is a Steiner system S(2, n+1, n^2+n+1)
import itertools

#  From all possible triples (0,0,0) to (n,n,n) reject:
#  - (0,0,0)
#  - tuples that are multiples of other tuples, ie (0,0,2) is (0,0,1) * 2
#  - This amounts to rejecting tuples where the left-most value is not 0 or 1
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

#  Generate all triples and send through the filter
def homog_coords(order):
    trips = [i for i in itertools.product(range(order), repeat=3)]
    return list(filter(lambda x: f(x), trips))

#  Our dot product, for triples of elements mod order
def dotprod(x,y, order):
    return (x[0]*y[0] + x[1]*y[1] + x[2]*y[2]) % order

#  Put together the "deck"
def make_deck(order):
    H = homog_coords(order)
    deck = []
    for i in range(len(H)):
        card = [H.index(n) for n in H if dotprod(n, H[i], order) == 0]
        deck.append(card)
    return deck

def format_deck(deck, format, one_index):
    match format:
        # readable:  <card id>:  <card elements>
        case 'readable':
            if one_index:
                deck = list(enumerate(deck, start=1))  # indexing from 1
            else:
                deck = list(enumerate(deck))           # indexing from 0, default
            for i in range(len(deck)):
                deck[i] = f"{str(deck[i][0]).rjust(3)}: {' '.join(str(e).rjust(3) for e in deck[i][1])}"
        # nums:  3 4 9 11
        case 'nums':
            for i in range(len(deck)):
                deck[i] = ' '.join(str(v) for v in deck[i])  
        # csv:   3,4,9,11
        case 'csv':
            for i in range(len(deck)):
                deck[i] = ','.join(str(v) for v in deck[i])
    return deck

#  Output to a file
#  TODO:  handle errors
def file_output(deck, filename):
    with open(filename, 'w') as file:
            for line in deck:
                file.write(str(line) + '\n')

#  Adjust deck to be 1..n instead of 0..n-1
def index_from_one(deck):
    for i in range(len(deck)):
        deck[i] = list(v+1 for v in deck[i])
    return deck

#  Default behavior for running this file
def main(args):
    order = args.order
    deck = make_deck(order)
    assert len(homog_coords(order)) == order**2 + order + 1
    #  TODO: change to try/except, probably only fails if non-prime order, might accidentally succeed though
    assert all(len(elems) == order+1 for elems in deck)
    
    if args.one:
        deck = index_from_one(deck)   
    deck = format_deck(deck, args.format, args.one)
    if args.print:
        for i in deck:
            print(i)
    if args.output:
        file_output(deck, args.output)

#  Call proj_plane.py <order> <options> to generate the deck of that order
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate a finite projective plane.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('order', type=int, help='Specify the order, must be prime.')
    parser.add_argument('-f', '--format', type=str, choices=['lists', 'readable', 'nums', 'csv'], 
                        default='lists', 
                        required=False,
                        help='Format: "lists", "readable", or "nums"')
    parser.add_argument('-p', '--print', 
                        action="store_true",
                        default=False, 
                        help='Print the PP')
    parser.add_argument('-o', '--output',
                        type=str,
                        help="Output in plaintext to a file. Specify filename.")
    parser.add_argument('-1', '--one',
                        action='store_true',
                        default=False,
                        help='Index from 1 instead of 0')
    args = parser.parse_args()
    main(args)