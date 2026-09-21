from typing import List

def count_unique_words(words: List[str]) -> int:
    i = len(words)
    p = 0
    
    if (i == 0):
        return 0
    else:
       my_set = set(words)
       for o in range(len(my_set)):
           p = p + 1
       return p
    pass

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
