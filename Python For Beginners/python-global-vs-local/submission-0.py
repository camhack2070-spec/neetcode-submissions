n = 100

def print_local_variable(num: int) -> None:
    num = n
    print(num)

print_local_variable(n)

print(n)
