# if the range is too big it takes a considerable amount of time
# second character MUST be even as a made up rule

test_range = range(100, 10000000)

for number in test_range:
	number = str(number)
	# if the second char must be even, its implied that the first char must be odd
	# and the third char must be odd too
	if (int(number[1]) % 2 == 0 
	and int(number[0]) % 2 != 0 
	and int(number[2]) % 2 != 0):

		# sets parameter for the second and following iterations
		previous_iteration_number = number[0]

		c = 0

		# compares current iteration number with previous iteration number
		for current_number in number:
			if current_number == str(int(previous_iteration_number)+1):
				c += 1

				# checks if the current number is the last one; if it is, 
				# print the found sequence
				if c + 1 == len(number):
					print("Found a sequence:", number)
				previous_iteration_number = current_number