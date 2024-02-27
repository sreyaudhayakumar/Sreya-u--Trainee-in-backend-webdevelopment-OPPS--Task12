# Create a class called Add , it must have __call__ defined. Create an object of that class.
# When the object is directly called with a list of integers - like - obj([1,2,3,4,5]) It must return the sum
# of elements in the list.
# Eg:
# add = Add()
# total = add([1,2,3,4,5,6])

class Add:
    def __call__(self, nums):
        return sum(nums)

add = Add()

nums = list(map(int, input("Enter a list of integers separated by space: ").split()))

total = add(nums)
print("The sum of the numbers is:", total)