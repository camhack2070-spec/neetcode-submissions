def divide_numbers(a: str, b: str) -> None:
    
    try:
        c = int(a)
        d = int(b)
        e = c/d
        print(e)
    except Exception as error:
        print("An error occurred:",error)
    pass



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
