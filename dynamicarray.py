import ctypes

class DynamicArray(objects):
	'''
		Dynamic array class (Similar to python list)
	'''

	def __init__(self):
		self.n = 0 # count actual elements (default is 0)
		self.capacity = 1 # default capacity
		self.A = self.make_array(self.capacity)

	def __len__(self):
		'''
		return number of elements sorted in array
		'''
		return self.n

	def __getitem(self, k):
		'''
		return element at index k
		'''
		if not 0 <= k <= self.n:
			# check it k index is in bounds of array
			return IndexError('k is out of bounds!')

		return self.A[k] # retrieve from the array at index k

	def append(self, ele):
		'''
		add element to the end of the array
		'''
		if self.n == self.capacity:
			# Double capacity if not enought room
			self._resize(2 * self.capacity)
		self.A[self.n] = ele # set self.n index to element
		self.n += 1

	def insertAt(self, item, index):
		'''
		This function inserts the item at any specified index
		'''

		if index < 0 or index > self.n:
			print("Please enter appropriate index..")
			return

		if self.n == self.capacity:
			self._resize(2 * self.capacity)

		for i in range(self.n-1, index-1, -1):
			self.A[i+1] = self.A[i]

		self.A[index] = item
		self.n+=1

	def delete(self):
		'''
		This function deletes item from the end of the array
		'''
		if self.n == 0:
			print("Array is empty deletion is not possible")
			return

		self.A[self.n-1] = 0
		self.n-=1

	def remoteAt(self, index):
		'''
		This function deletes the item from the specified index..
		'''
		if self.n == 0:
			print("Array is empty deletion not possible")
			return

		if index < 0 or index >= self.n:
			return IndexError("Index out of bound...Deletion not possible")

		if index == self.n-1:
			self.A[index] = 0
			self.n-=1
			return

		for i in range(index, self.n-1):
			self.A[i] = self.A[i+1]

		self.A[self.n-1] = 0
		self.n-=1

	def _resize(self, new_cap):
		'''
		Resize internal array to capacity new_cap
		'''

		B = self.make_array(new_cap) # New Bigger Array

		for k in range(self.n): # Reference all existing values
			B[k] = self.A[k]

		self.A = B # Call A the new bigger array
		self.capacity = new_cap # reset the capacity

	def make_array(self, new_cap):
		'''
		returns a new array with new_cap capacity
		'''
		return (new_cap * ctypes.py_object) ()


# Instantiate
arr = DynamicArray()
# Append new element
arr.append(1)
len(arr)

# output ---> 1

# Append new element
arr.append(2)
# check length
len(arr)

# output ---> 2

# Index
arr[0]

# output ---> 0

arr[1]

# output ---> 2