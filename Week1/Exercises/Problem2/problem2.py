def main():
	# Ask for user's weight
	weight = input("Enter your weight (Kg): ")
	# Ask for user's height
	height = input("Enter your height (m): ")

	# Calculate BMI according to the standard formula
	bmi = float(weight) / (float(height) * float(height))

	# Output the result
	print(f"Your boddy mass index (BMI) is: { round(bmi, 2) }")

if __name__ == "__main__":
	main()