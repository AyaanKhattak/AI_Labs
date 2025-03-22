def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

print("Sorted sentence:", sort_sentence("hello world this is a test"))