global_variable = 100
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


def process_numbers():
    global global_variable  # This 'global' declaration is unnecessary here
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)  # Removes even numbers from the list
        local_variable -= 1

    return numbers


my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}  # Sets automatically remove duplicates
result = process_numbers(
    numbers=my_set
)  # Error: process_numbers() takes 0 positional arguments but 1 was given


def modify_dict():
    local_variable = 10
    my_dict["key4"] = local_variable


modify_dict(5)  # Error: modify_dict() takes 0 positional arguments but 1 was given


def update_global():
    global global_variable
    global_variable += 10  # Increments the global variable by 10

    for i in range(5):
        print(i)
        i += 1  # Unnecessary: 'i' is controlled by the for-loop

    if my_set is not None and my_dict["key4"] == 10:
        print("Condition met!")

    if 5 not in my_dict:
        print(
            "5 not found in the dictionary!"
        )  # Potential issue: checking for integer 5 in a dict with string keys

    print(global_variable)
    print(my_dict)
    print(my_set)
