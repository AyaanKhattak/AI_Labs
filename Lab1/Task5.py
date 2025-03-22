def count_pattern(pattern, lst):
    count = 0
    pattern_length = len(pattern)
    for i in range(len(lst) - pattern_length + 1):
        if tuple(lst[i:i + pattern_length]) == pattern:
            count += 1
    return count

print("Pattern count:", count_pattern(('a', 'b'), ('a','b', 'c', 'e', 'b', 'a', 'b', 'f')))
print("Pattern count:", count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a','b', 'a')))
