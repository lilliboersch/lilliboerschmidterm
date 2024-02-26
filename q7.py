import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Remove odd numbers and double the even numbers
processed_numbers = [num * 2 for num in random_numbers if num % 2 == 0]

print("Processed list:", processed_numbers)

import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
processed_numbers = []
for j in range(len(random_numbers)):
    if random_numbers[j] % 2 == 0:  # Check if the number is even
        processed_numbers.append(random_numbers[j] * 2)  # Double it and add to the processed list
# The processed list with odd numbers removed and even numbers doubled
print("Processed list:", processed_numbers)

