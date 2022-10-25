# program to find the duplicate number in array and it's time complexity
 
numbers = [3, 6, 2, 4, 3, 6, 8, 9]

for i in range(len(numbers)):
	for j in range(i + 1, len(numbers)):
		if numbers[i] == numbers[j]:
			print(f"{numbers[i]} is a duplicate numbers.")
			break

## time = a * n^2 + b ---> O(n^2)

# A quick note on public vs private methods, we can use an underscore before the method to keep it non-public

class M(objects):
	def public(self):
		print('use tab to see me.')

	def _private(self):
		print('you won\'t be able to see me.')

m = M()
m.public()

## output ---> use tab to see me.

m._private()

## output ---> you won't be able to see me