def remove_max_len_words(sentence):
    words=sentence.split()
    max_len=max(len(word)for word in words)
    filtered_words=[word for word in words if len(word)!= max_len]
    return "".join(filtered_words)

input_str="I love Python Programming"
output_str=remove_max_len_words(input_str)
print("Updated String: ",output_str)