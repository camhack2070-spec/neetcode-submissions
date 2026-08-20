def first_n_characters(s: str, n: int) -> str:
    length = len(s)
    if n <= length:
        return (s[:n])
    pass

def last_n_characters(s: str, n: int) -> str:
    length = len(s)
    n = len(s) - n
    if n <= length:
        return(s[n:])
    pass


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
