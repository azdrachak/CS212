#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def higher(f1, f2):
    """
    Returns True if floor f1 is higher than floor f2
    """
    return True if f1 - f2 > 0 else False

def adjacent(f1, f2):
    """
    Returns True if floors f1 and f2 are adjacent to each other
    """
    return True if abs(f1 - f2) == 1 else False

def floor_puzzle():
    """
    Solves Floor puzzle.
    Returns a list of
    five floor numbers denoting the floor of Hopper, Kay,
    Liskov, Perlis, and Ritchie.
    """

    floors = [1,2,3,4,5]
    c_floors = itertools.permutations(floors)

    order = next([Hopper, Kay, Liskov, Perlis, Ritchie]
        for Hopper, Kay, Liskov, Perlis, Ritchie in c_floors
        if (Hopper != 5)
           and (Kay != 1)
           and (Liskov != 1 and Liskov != 5)
           and (higher(Perlis, Kay))
           and (not adjacent(Ritchie, Liskov))
    and (not adjacent(Liskov, Kay)))


    return order

print floor_puzzle()