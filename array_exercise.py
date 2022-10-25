'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''


class Exercise01:
	def __init__(self):
		self.expenses = [{
		"January": 2200,
		"February": 2350,
		"March": 2600,
		"April": 2130,
		"May": 2000,
		}]

	def first_question(self):
		self.extra_money = self.expenses[0]["February"] - self.expenses[0]["January"]
		print(f"compared to January i have spent total {self.extra_money} in February")

	def second_question(self):
		self.total_expense = self.expenses[0]["January"] + self.expenses[0]["February"] + self.expenses[0]["March"]
		print(f"My total expense in the first quarter of the year is {self.total_expense}")


	def third_question(self):
		for index in range(len(self.expenses)):
			for key in self.expenses[index]:
				if self.expenses[index][key] == 2000:
					print(f"You've spent 2000 in the month of {list(self.expenses[index].keys())[4]}")
			
	def fourth_question(self):
		for index in range(len(self.expenses)):
			self.expenses[index].update({"June": 1980})
			print(self.expenses[index])

	def fifth_question(self):
		self.expenses[0]["April"] = self.expenses[0]["April"] - 2000
		for index in range(len(self.expenses)):
			print(self.expenses[index])

'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

class Exercise02:
	def __init__(self):
		self.given_list = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

	def first_question(self):
		self.length = len(self.given_list)
		print(self.length)

	def second_question(self):
		self.given_list.append("black panther")
		print(self.given_list)

	def third_question(self):
		# append black panther to the list
		self.given_list.append("black panther")
		# first remove black panther from the list
		del self.given_list[-1]
		# add black panther after hulk
		self.given_list.insert(3, "black panther")
		print(self.given_list)

	def fourth_question(self):
		# append black panther to the list
		self.given_list.append("black panther")
		# first remove black panther from the list
		del self.given_list[-1]
		# add black panther after hulk
		self.given_list.insert(3, "black panther")
		# self.given_list.remove("thor")
		# self.given_list.remove("hulk")
		self.given_list[1:3] = ["doctor strange"]
		# fifth question
		self.given_list.sort()
		print(self.given_list)

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
class OddNumbers:
	def __init__(self):
		self.max_number = int(input("Enter the maximum number\n"))

	def get_odd(self):
		for numbers in range(1, self.max_number + 1):
			if numbers%2 != 0:
				print(numbers)

# array insertion complexity is O(n)


'''
Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution01:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for s in range(1, len(nums)):
            if nums[s] != nums[s-1]:
                nums[l] = nums[s]
                l += 1
        return l