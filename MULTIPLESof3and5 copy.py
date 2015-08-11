

""" MULTIPLE OF THREE AND FIVE
What is the sum of the multiples of three and five under 100"""


def sum_multiple():
	sum_add = 0
	for i in range(0,1000):
		if i % 3 == 0 or i % 5 == 0:
			sum_add += i 

	return sum_add

result = sum_multiple()
print result 
