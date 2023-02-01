#DAY 10
from art import logo

def add(n1,n2):
	return n1 + n2
	
def subtract(n1,n2):
	return n1 - n2
	
def multiply(n1,n2):
	return n1 * n2
	
def divide(n1,n2):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}
def calculator():
	print(logo)
	print("---Available operations----")
	for symbol in operations:
		print(symbol)
	print("---------------------------")
	continueCalculating = True
	
	
	num1 = float(input("What´s the first number?: "))
	
	while continueCalculating:
		
		operation_symbol = input("What´s the operation?: ")
		num2 = float(input("What´s the next number?: "))
		calc_function = operations[operation_symbol]
		result = calc_function(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {result}")
		
		if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. : ").upper() == 'Y':
			num1 = result
		else:
			continueCalculating = False
			calculator()
			
calculator()