userName = raw_input("What is your name?")
greet = "Hello %s!" % userName

print greet

explain = "The purpose of the 'fizzbuzz' program is to output all \nof the numbers from 1 to 100. However, for multiples \nof three 'Fizz' will be printed instead of the number, \nand for multiples of five 'Buzz' will be printed. \nFinally, for numbers which are multiples of both \nthree and five 'FizzBuzz' will be printed."

print explain

def choice():
	userProceed = raw_input("Are you ready to see fizzbuzz in action?")
	
	if userProceed == 'yes':
		for i in range(1, 101):
			if i % 3 == 0 and i % 5 == 0:
				print('FizzBuzz')
			elif i % 3 == 0:
				print('Fizz')
			elif i % 5 == 0:
				print('Buzz')
			else:
				print(i)	

	else:
		print "WHAT?!?!? Fizzbuzz is SO COOL! Why don't I give you another chance to reconsider?"
		return choice()


if __name__ == '__main__':
	choice()
