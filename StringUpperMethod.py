# This code is used to explain the working principle of .upper() method in python
#Logic
'''The concept and algorithm of this code is that two lists are created, one of them is small letters
while the other one consists of capital letters. 
A loop is carried out on them and the index of those letters in the small letters list is gotten 
the index is saved into a list 
the list is looped and the items at the int type of list is passed as an index arguement in the capital
letters list the answer is them added to an empty string that was created earlier'''

class String(): 
	"""class creation to explain the working principle of all string method"""


	def __init__(self, string):
		self.string = string


	def upper_ken(self):
		small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
		'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #small letters of the english alphabeth
		capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
		'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #capital letters of the english alphabeth

		result = '' # empty string to help store future values
		get_index = []

		for i in self.string:
			if i in capital_letters and i not in small_letters:
				get_index.append(capital_letters.index(i))#checking the index of the letters in the input
				#from the small_letters list and adding the integer value to the get_index empty list that was
				#created
			elif i in small_letters:
				get_index.append(small_letters.index(i))
			elif i not in small_letters and i not in capital_letters:
				small_letters.append(i)
				capital_letters.append(i)
				get_index.append(small_letters.index(i))
			else:
				return self.string
		for i in get_index: # looping through the integer values stored in the get_index list
			capital_letter = capital_letters[i] # getting the items at that particular index in the capital let_
			result += capital_letter

		return result

#examples and Testing


value = String('tech_with ken')
print(value.upper_ken ())