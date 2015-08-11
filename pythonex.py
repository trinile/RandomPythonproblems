"""Write a function that counts the frequency of items in a list.  
It should take a list input and output a dictionary with the frequency counts 
for all of the objects in the list.  For example:  

Input:  ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']
Result:  {'a': 3, 'q': 2, 'c': 2, 'b': 1}"""


from collections import Counter 
def frequency_count():

	list_input = ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']
	freqs = Counter(list_input)
	print(freqs)
frequency_count()

"""
1. sort out unique words in the list
2. go through every word in the list and count how many instances of word in list.
	
"""

freq_ct = []
list_input = ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']

from sys import argv
script, filename = argv

def frequency_count2(list_input):
	freq_list = {}
	#list_set = set(list_input)
	#list_input2 = list(list_set)
	#print list_input2
	
	for letter in list_input:
		freq_list[letter] = freq_list.get(letter, 0) + 1
		freq_list_sorted = freq_list.items()
		freq_list_sorted.sort()
	print "Dictionary: ", freq_list 
	print "Sorted alphabetically: ", freq_list_sorted

	#target = open(filename,'w')
	#target.write('\tLetter, Frequency\n')
	#target.close()

	with open(filename, 'a') as f:
	   f.write('\tLetter, Frequency\n')
	   for letter, frequency in freq_list.items():
		  x =  "\t %s, %s \n " % (letter, frequency)
		  print x
		  f.write(x)
	
frequency_count2(list_input)


def lettercount(letters):
	outdict = {}
	for letter in letters: 
		try:
			outdict[letter] = outdict[letter] + 1
		except(KeyError):
			outdict[letter] = 1
	return outdict

print lettercount(['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q'])



#frequency_count2()
#print str(zip(list_input,freq_ct))

	#count()

#index = 0
#list_input = ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']

#def freq_count():
	#while index < len(list_input):
 