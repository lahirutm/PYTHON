def main():
	# Ask user to enter two numbers one by one
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")

	# Convert to float
	number1 = float(num1)
	number2 = float(num2)

	# Calculate Sum and Product
	sum_value = number1 + number2
	product_value = number1 * number2

	# Show the output
	print("Sum of the two numbers are: " + str(sum_value))
	print("Product of the two numbers are: " + str(product_value)) 

if __name__ == "__main__":
    main()