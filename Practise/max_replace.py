def update_str(sentence,reg_no):
    words=sentence.split()
    max_len=max(len(word)for word in words)
    update_word=[word if len(word)!=max_len else reg_no for word in words]
    return "".join(update_word)

input_str = "I love Python Programming"
registration_no = "L1F22BSCS0224"
output_str = update_str(input_str, registration_no)
print("Updated String:", output_str)