def nthFibonacci(n):
    if n <= 1:
        return n

    # stores current Fibonacci number
    curr = 0

    # To store the previous two Fibonacci numbers
    prev1 = 1
    prev2 = 0

    for i in range(2, n + 1):
        curr = prev1 + prev2
        
        prev2 = prev1
        prev1 = curr

    return curr

def main():
    print("Enter a number \n")
    i_number = int(input())
    print("\nYou entered " + str(i_number))

    nth_fibonacci_number = nthFibonacci(i_number)
    print(str(i_number) + "th Fibonacci number is: " + str(nth_fibonacci_number))


if __name__=="__main__":
    main()