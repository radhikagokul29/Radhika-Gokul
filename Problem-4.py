def count_multiples(lst):
    multiples_count = {}
    for i in range(1, 10):
        count = sum(1 for num in lst if num % i == 0)
        multiples_count[i] = count
    return multiples_count
if __name__ == "__main__":
    # Sample input
    input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    print("Input List:", input_list)
    result = count_multiples(input_list)
    print("Multiples Count:")
    for key in result:
        print(f"{key}: {result[key]}")
