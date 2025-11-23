# Odd/Even Counter

def count_odd_even(numbers):
    odd_count = 0
    even_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
    return odd_count, even_count

# Example usage
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_count, even_count = count_odd_even(numbers)
print(f"Odd count: {odd_count}, Even count: {even_count}")