global_variable = 100
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


def process_numbers(numbers):
    # Added 'numbers' parameter to accept input
    local_variable = 5
    numbers = list(numbers)  # Ensure 'numbers' is a list to use list methods

    while local_variable > 0:
        if local_variable % 2 == 0 and local_variable in numbers:
            numbers.remove(local_variable)  # Remove even numbers
        local_variable -= 1

    return numbers


my_set = {1, 2, 3, 4, 5}  # Removed duplicate values
result = process_numbers(numbers=my_set)


def modify_dict(local_variable):
    # Added 'local_variable' parameter to accept input
    my_dict["key4"] = (
        local_variable  # Modify the dictionary with the new key-value pair
    )


modify_dict(5)


def update_global():
    global global_variable
    global_variable += 10  # Increase global_variable by 10

    for i in range(5):
        print(i)
        # Removed 'i += 1' as it's unnecessary

    if my_set is not None and my_dict["key4"] == 10:
        print("Condition met!")  # This won't execute since my_dict['key4'] == 5

    if "5" not in my_dict:
        # Checking for string '5' since dictionary keys are strings
        print("5 not found in the dictionary!")

    print(global_variable)  # Should print 110
    print(my_dict)  # Display the updated dictionary
    print(my_set)  # Display the set


update_global()
