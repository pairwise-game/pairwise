# Pairwise -- Generating and formatting finite projective planes

## `proj_plane.py`
This can be run independently with a variety of commandline options, `python proj_plane.py -h` for details. The only required argument is order, which must be prime (but is not checked.)

Some example uses:

`python proj_plane.py 5 -p` 
- prints out an order5 projective plane in list form, line by line.

`python proj_plane.py 3 -f readable -p`
- prints out an order 3 projective plane in the form (card id): (elements on the card)

`python proj_plane.py 3 -f readable -1 -p`
- The same as above, but indexing from 1 instead of 0