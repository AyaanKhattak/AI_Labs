a = [
    (1,),           # First tuple with 1 element
    (2, 3),         # Second tuple with 2 elements
    (4, 5, 6)       # Third tuple with 3 elements
]

print("Second element of second tuple in a:", a[1][1])

b = [
    [1, 2, 3, 4],   # First list
    [5, 6, 7, 8],   # Second list
    [9, 10, 11, 12],# Third list
    [13, 14, 15, 16]# Fourth list
]
print("Last two elements of first list in b:", b[0][-2:])