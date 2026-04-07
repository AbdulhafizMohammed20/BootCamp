def find_largest_number(nums) : # accepts an array of integers
    largest = float("-inf") 

    for num in nums:

        largest = max(largest , num) # always takes the maximum of the current and previous largest number

    return largest

while True :
    print("Insert an array of integers :" )

    nums = list(map(int, input().split()))
    print(f"The largest number i s = {find_largest_number(nums)}")
          