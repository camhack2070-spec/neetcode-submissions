from typing import List

def read_integers() -> List[int]:
    reading = input()
    reading1 = reading.split(',')
    result = []
    for x in reading1:
        result.append(int(x))
    return result
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
