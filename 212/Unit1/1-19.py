# -----------
# User Instructions
# 
# Define a function, two_pair(ranks).

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return pair, low_pair
    return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def test():
    """Test cases for the functions in poker program."""
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "TD TC 9D 9C 6H".split() # Two Pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert two_pair(tpranks) == (10, 9)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) is None
    assert kind(2, fkranks) is None
    assert kind(1, fkranks) == 7
    return 'tests pass'

def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks
print test()

