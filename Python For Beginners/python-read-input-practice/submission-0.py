def add_two_numbers() -> int:
    user_input = input()
    addint = user_input.split(',')
    a = 0
    for i in addint:
        a = a + int(i)
    return a    
    pass



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
