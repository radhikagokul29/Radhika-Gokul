def generate_odd_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

if __name__ == "__main__":
    try:
        a = int(input("Enter a number: "))
        if a <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_odd_series(a)
            print("Odd series:", ", ".join(map(str, series)))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
