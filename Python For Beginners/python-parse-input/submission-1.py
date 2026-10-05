from typing import List

def read_integers() -> List[int]:
    readint =  input()
    return [int(x) for x in readint.split(",")]
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
