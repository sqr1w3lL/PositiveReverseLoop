def process_numbers(numbers):

    positive_numbers = []

    for number in numbers:

        if number > 0:
            positive_numbers.append(number)

    positive_numbers.reverse()

    return positive_numbers


numbers = [2, 8, -10, 61, -9, 3, -5, 1]

result = process_numbers(numbers)

print(result)
