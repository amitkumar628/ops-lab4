#!/usr/bin/env python3
# Author: Amit Kumar
# Author ID: 153260237
# Date Created: 2025/09/30

# -----------------------------
# List Operations (Lab 4B)
# -----------------------------

def join_lists(list1, list2):
    """Return a new list with all unique elements from both lists"""
    return list(set(list1) | set(list2))

def match_lists(list1, list2):
    """Return a list of elements that are common to both lists"""
    return list(set(list1) & set(list2))

def diff_lists(list1, list2):
    """Return a list of elements that are in one list or the other but not both"""
    return list(set(list1) ^ set(list2))

if __name__ == "__main__":
    # Demo
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 1, 0, -1, -2]
    print("Join:", join_lists(l1, l2))
    print("Match:", match_lists(l1, l2))
    print("Diff:", diff_lists(l1, l2))
