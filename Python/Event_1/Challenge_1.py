# Challenge 1 for the Code Kata.

def wordwrap(string, num):
    """..."""
    arr = string.split(' ')
    n = ''
    for item in arr:
        while len(item) <= num:
            n += item

    

    return n


print(wordwrap('The quick brown fox jumps over the lazy dog', 15))