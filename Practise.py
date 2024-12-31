def gen_by_terms(n):
    if n <= 0:
        return []

    fibo_series = [0, 1]
    for _ in range(2, n):
        fibo_series.append(fibo_series[-1] + fibo_series[-2])
    return fibo_series[:n]


def gen_by_max_value(max_value):
    if max_value < 0:
        return []

    fibo_series = [0, 1]
    while True:
        next_value = fibo_series[-1] + fibo_series[-2]
        if next_value > max_value:
            break
        fibo_series.append(next_value)
    return fibo_series


def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                num_terms = int(input("Enter the number of terms: "))
                if num_terms < 0:
                    print("Please enter a non-negative integer.")

                else:
                    series = gen_by_terms(num_terms)
                    print(f"Fibonacci series ({num_terms} terms): {', '.join(map(str, series))}")

            elif choice == 2:
                max_value = int(input("Enter the maximum value: "))
                if max_value < 0:
                    print("Please enter a non-negative integer.")

                else:
                    series = gen_by_max_value(max_value)
                    print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, series))}")

            elif choice == 3:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()