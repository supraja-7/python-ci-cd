from utils import is_even

def say_hello(name):
    print(f"Hello {name}")

def find_even_numbers_in_list(num_list):
    return [
        el for el in num_list
        if is_even(el)
    ]

if __name__ == "__main__":
    say_hello("RANDOM NAME")
    print(
        find_even_numbers_in_list(
            [5,8,3,6,1,9,0,-3,-4, -10]
        )
    )