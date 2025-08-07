def generate_conditional_odd_series(a):
    result = []
    for i in range(1, a + 1, 2):
        result.append(i)
    return result

if __name__ == "__main__":
    try:
        a = int(input("Enter a number: "))
        if a <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_conditional_odd_series(a)
            print("Conditional Odd Series:", ", ".join(map(str, series)))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
