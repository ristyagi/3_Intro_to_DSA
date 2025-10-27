# HASHING

# Hashing is pre-storing values into some datastructure like List/Dictionary/Set and then fetching it 
# https://www.youtube.com/watch?v=0IE5T63qEHg&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=11



# Q1 - print how many times each item of m is present in n?
# Two list are there n and m
# constraints are -> 
    # 1 <= n[i] <= 10
    # n can have 10^8 elements
    # m can have 10^8 elements

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2] 


##### Brute Force Solution #####
for num in m:                               # iterating over list m
    count = 0
    # print(f'm -> {num}')
    for item in n:                          # iterating over list n
        # print(f'n is -> {item}')
        if item == num:                     # check if item in m is equal to each item in n
            count = count + 1
    print(f'count for {num} is -> {count}\n')

# Time complexity of this solution will be TC = O(m x n) 
# as there are m items and to check those we have to iterate over n items.
# Space complexity SC = O(1), as both lists are provided to us and we are only using one count variable
# worst case Time taken will be 10^8 x 10^8 = 10^16 which is greater than 10^8 and hence TLE error will occur.
# error will be thrown not because of code but because number of operations will be too high.



##### Hash List Solution #####
# Since value of elements in n can range from 1 to 10 only, we can think of using hashing.

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2,11]

hash_list = [0]* (len(n)+1)     # creating a hash list with 0 value on each element and its of length one more than n
hash_list
print(len(hash_list))

for num in n:                   # taking each number of n and setting count of that num to the same index of hash_list
    hash_list[num] += 1


for t in m:
    if t > len(hash_list)-1:
        print(f'count for {t} is -> 0')
    else:
        print(f'count for {t} is -> {hash_list[t]}')

# total TimeComplexity= O(n+m) - as there are two for loops and they are not inside each other, they are one after other
# SpaceComplexity -> only hash_list is created as new, which will have a fixed number of items, is 1<=n<=10, that means hash_list will always be of static length 11
# hence O(11) which is same as O(1)

# in worst case with 10^8 elements on both lists
# TC = O(10^8 + 10^8) = O(2 x 10^8) ~ O(10^8) and hence TLE error will not come



##### Hash Map Solution #####

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2,11]

freq_map = {}

nums = len(n)

for i in range(0,nums):
    freq_map[n[i]] = freq_map.get(n[i],0)+1 # if key with same element as m present in hash_dict then increase freq by 1 or add new key to it

freq_map[5]
