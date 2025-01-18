# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number
    
print (fizz_buzz(3))
print (fizz_buzz(5))
print (fizz_buzz(15))
print (fizz_buzz(4))



# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total

print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([2, 4, 6])) 



# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    
    vowels = "aeiouAEIOU"
    
    count = 0
    
    for char in string:
        if char in vowels: 
            count += 1 
            
    return count

print(count_vowels("hello"))
print(count_vowels("aeiou"))
print(count_vowels("xyz"))


# Question 4

# Write a function that counts the number of repeated characters in a string.

from collections import Counter
def count_repeats(string):
    
    char_count = Counter(string)
    
    repeats = {char: count for char, count in char_count.items() if count > 1}
    
    return repeats

result = count_repeats("hello")
print(result) 



if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
