nums=[1,2,3,4,5,6]
#x=nums[0]+ nums[4]
#y=nums[5]-nums[2]
#print(x+y)
#nums[-1]
counter=len(nums)-1
for item in nums:
    nums[counter]=nums[counter]+5
    counter=counter-1
print(nums)