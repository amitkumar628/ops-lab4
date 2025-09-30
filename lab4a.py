#!/usr/bin/env python3
# Author: Amit Kumar
# Author ID: 153260237
# Date Created: 2025/09/30

# --- Functions for Set Operations ---

# Function to join two sets
def join_sets(set1, set2):
    return set1 | set2   # union

# Function to find intersection of two sets
def match_sets(set1, set2):
    return set1 & set2   # intersection

# Function to find symmetric difference of two sets
def diff_sets(set1, set2):
    return set1 ^ set2   # symmetric difference


# --- Main testing area (only runs when executed directly) ---
if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 1, 0, -1, -2}

    print("Join:", join_sets(set1, set2))
    print("Match:", match_sets(set1, set2))
    print("Diff:", diff_sets(set1, set2))
