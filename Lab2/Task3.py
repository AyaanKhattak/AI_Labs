def calculate_statistics(numbers):
    if not numbers:
        print("The list is empty!")
        return
    
    total_sum = 0
    for num in numbers:
        total_sum += num
    
    mean = total_sum / len(numbers)
    
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]
    
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    
    print("\nResults:")
    print(f"List of numbers: {numbers}")
    print(f"Sum: {total_sum}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")

# Example with predefined list
numbers = [4, 2, 7, 3]
calculate_statistics(numbers)