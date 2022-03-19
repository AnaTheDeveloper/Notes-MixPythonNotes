# A function is an object that is able to accept some sort of input, possibly modify it, and return some sort of
# output. In Python, a lambda function is a one-line shorthand for function.

add_two = lambda my_input: my_input + 2

print(add_two(3))
print(add_two(100))
print(add_two(-2))

# Let’s break this syntax down:
#
# 1. The function is stored in a variable called add_two
# 2. lambda declares that this is a lambda function (if you are familiar with normal Python functions, this is similar to how we use def to declare a function)
# 3. my_input is what we call the input we are passing into add_two
# 4. We are returning my_input plus 2 (with normal Python functions, we use the keyword return)

# Let’s write a lambda function that checks if a string is a substring of the string “This is the master string”.
is_substring = lambda my_string: my_string in "This is the master string"

print(is_substring('I'))
print(is_substring('am'))
print(is_substring('the'))
print(is_substring('master'))

# We might want a function that will perform differently based on different inputs. Let’s say that we have a
# function check_if_A_grade that outputs 'Got an A!' if a grade is at least 90, and otherwise says you 'Did not get an A'.
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

print(check_if_A_grade(91))
print(check_if_A_grade(70))
print(check_if_A_grade(20))

# Lambda functions only work if we’re just doing a one line command. If we wanted to write something longer, we’d
# need a more complex function. Lambda functions are great when you need to use a function once. Because you aren’t
# defining a function, the reusability aspect functions is not present with lambda functions. By saving the work of
# defining a function, a lambda function allows us to efficiently run an expression and produce an output for a
# specific task, such as defining a column in a table, or populating information in a dictionary.
