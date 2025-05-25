def non_repeating_elements(s):
    count={}
    for char in s:
        if char!='':
            count[char]=count.get(char,0)+1
    return [char for char in count if count[char]==1]
input_str = "civic car"
result = non_repeating_elements(input_str)
print("Non-repeating characters:", result)