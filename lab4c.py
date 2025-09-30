#!/usr/bin/env python3
# Author: Amit Kumar
# ID: akumar250

def create_dictionary(keys, values):
    """Return dictionary built from two lists: keys + values."""
    return dict(zip(keys, values))

def shared_values(dict1, dict2):
    """Return a set of values present in BOTH dictionaries."""
    return set(dict1.values()) & set(dict2.values())

if __name__ == "__main__":
    k = ["a", "b", "c"]
    v = [1, 2, 3]
    d1 = create_dictionary(k, v)
    d2 = {"x": 2, "y": 3}
    print("dict:", d1)               # {'a':1,'b':2,'c':3}
    print("shared:", shared_values(d1, d2))  # {2,3}
