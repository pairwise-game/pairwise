# Pairwise-Games: Generating and formatting finite projective planes
## Background
This module generates and formats finite projective planes. A projective plane order n is a Steiner system S(2, n+1, n^2+n+1).  It's also the driving structure behind the game Dobble (aka Spot-It). 

In this setting, I refer to the PP as a *deck* and the lines as *cards*.  Notably for the purposes of games, there is assured to be exactly one element in common between any two cards.

I implemented this following [Some Maths for Dobble](https://blog.polettix.it/some-maths-for-dobble/).

## Notes for PP order N
- N must be prime
- Total cards in a deck will be N^2 + N + 1
- Total elements across the deck will also be N^2 + N + 1
- Total elements on each card will be N + 1

## `main.py`
As of now, just some example usage. Later, some kind of UI for deciding what you want to do with the projective planes, and being able to do them.

## `proj_plane.py`
This can be run independently with a variety of commandline options, `python proj_plane.py -h` for details. The only required argument is order, which must be prime (but is not checked.)

### Some example uses:
 
Print out an order5 projective plane in list form, line by line:
- `python proj_plane.py 5 -p`

Print out an order 3 projective plane in the form (card id): (elements on the card):
- `python proj_plane.py 3 -f readable -p`

Print just the numbers for an order 3 projective plane, but index from 1 instead of 0:
- `python proj_plane.py 3 -f nums -1 -p`

Write a csv file of an order7 projective plane as "order7.csv":
- `python proj_plane.py 7 -f csv -o order7.csv`

Print and write an order11 projective plane as just numbers, with card number as the first element of each card, indexing from 1 instead of 0:
- `python proj_plane.py 11 -f nums -p -o output.txt -1 -c`