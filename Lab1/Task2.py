def triangle():
    value = 1
    row = 1
    while row <= 10:
        column = 1
        while column <= row:
            if column != row:
                print(value, ' ', sep='', end='')
            else:
                print(value)
            value = value + 1
            column = column + 1
        row = row + 1

# Call the function to print the pattern
triangle()
