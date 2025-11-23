# Find Max, Min, Average (function)

def find_max_min_avg(numbers):
    if not numbers:
        return None, None, None
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    return maximum, minimum, average

# Example usage
numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(float, numbers.split()))
max_num, min_num, avg_num = find_max_min_avg(numbers_list)
print(f"Maximum: {max_num}, Minimum: {min_num}, Average: {avg_num}")