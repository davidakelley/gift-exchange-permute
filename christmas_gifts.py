import numpy as np
import itertools
import pandas as pd

i6 = np.identity(6)

# Age ordered names:
names = ['Alex', 'Laura', 'Tom', 'David', 'Michelle', 'Allison']

# disallowed matrix: Insert a 1 in this matrix for any impossibility that you know. 
# The array is arranged such that the giver is associated with a row, the receiver is associated
# with the columns. So if Alex cannot give a gift to David, that means the [0,3] element must be 
# set to a one. The expectation is that if you know who a person has, you should fill in ones for 
# all of the other ones in that column/row to indicate that. 

# Pre-draw requirements
# disallowed = np.array([[1, 1, 0, 0, 0, 0], 
#                        [1, 1, 0, 0, 1, 0], 
#                        [0, 0, 1, 0, 0, 0], 
#                        [0, 0, 0, 1, 0, 1], 
#                        [0, 0, 1, 0, 1, 0], 
#                        [0, 0, 0, 1, 0, 1]])

# Fill in your information set here: 
disallowed = np.array([[1, 1, 0, 0, 0, 0], 
                       [1, 1, 0, 0, 1, 0], 
                       [0, 0, 1, 0, 0, 0], 
                       [0, 0, 0, 1, 0, 1], 
                       [0, 0, 1, 0, 1, 0], 
                       [0, 0, 0, 1, 0, 1]])

df_allowed = pd.DataFrame(1-disallowed, 
                          index=names, columns=names, dtype=int)
print("\nWhat relationships are allowed:")
print(df_allowed)

lst = list(range(6)) 

nAllowed = 0
nDisallowed = 0

# Iterate through all permutations
for perm in itertools.permutations(lst):
    draw_mat = i6[perm,:]
    if np.any((disallowed + draw_mat) == 2): 
        nDisallowed += 1
    else: 
        nAllowed += 1

summary_stats = pd.DataFrame(
    {'nAllowed': [nAllowed], 
     'nDisallowed': [nDisallowed], 
     'nTotal': [nAllowed + nDisallowed]}
)        
print("\nSummary statistics")
print(summary_stats)

possibles = np.zeros((6, 6, nAllowed))

i_possible = 0
for perm in itertools.permutations(lst):
    draw_mat = i6[perm,:]
    if ~np.any((disallowed + draw_mat) == 2): 
        possibles[:,:,i_possible] = draw_mat
        i_possible += 1

counts = np.sum(possibles, axis=2)
out_df = pd.DataFrame(counts, index=names, columns=names, dtype=int)

print("Sum of possible relationships")
print(out_df)
