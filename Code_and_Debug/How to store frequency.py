nums = [5,6,7,7,1,9,111,1,1,5,1,1]

##### Method 1 #####
# using Dict

freq_map = {} # creating new empty freq map dict
freq_map

for i in range(0,len(nums)):
    if nums[i] in freq_map:
        # freq_map[nums[i]] += 1
        freq_map[nums[i]] = freq_map[nums[i]] + 1
    else:
        freq_map[nums[i]] = 1

# freq_map
print(freq_map[1])

# finding a key in dict takes O(1) as TC
# updating value of any key in dict is also O(1)
# adding new key to dict is also O(1)
# and running a for loop on dict is O(n)
# if in worst case all elements on nums are unique then freq_dict will also have same number of n elements, each having a value of 1
# so SC = O(n)



# METHOD 2
freq_map2 = {}

n = len(nums)

for i in range(0,n):
    freq_map[nums[i]] = freq_map.get(nums[i],0)+1           
    # if a key is present then get its value and add 1 to it and update or give 0 value and add it as new element

# For loop for n items has O(n)
# .get also has a O(1) as TC
# on an average case , access, update , delete and add all has O(1) TC


