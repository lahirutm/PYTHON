class Bmi:
	def calculate_bmi(self, weight, height):
		# Calculate BMI according to the standard formula
		self.bmi_value = float(weight) / (float(height) * float(height))


	def display(self):
		# Output the result
		print(f"Your boddy mass index (BMI) is: { round(self.bmi_value, 2) }")

def main():
	# Ask for user's weight
	weight = input("Enter your weight (Kg): ")
	# Ask for user's height
	height = input("Enter your height (m): ")

	bmi = Bmi()
	bmi.calculate_bmi(weight, height)
	bmi.display()
	

if __name__ == "__main__":
	main()