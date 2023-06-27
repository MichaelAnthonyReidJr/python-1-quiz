def max_values(nums):
  maxNumber = 0
  indicesOfMaxNumber = []
  i = 0
  for eachNumber in nums:
    if eachNumber > maxNumber:
      maxNumber = eachNumber
      maxIndices = i
      i += 1
      indicesOfMaxNumber.append(maxIndices)
      nums.pop(maxNumber)
  for eachNumber in nums:
    if eachNumber > maxNumber:
      maxNumber = eachNumber
      maxIndices = i
      i += 1
      indicesOfMaxNumber.append(maxIndices)
      nums.pop(maxNumber)
      return indicesOfMaxNumber
     
      
  
    
    
    maxNumber = max(nums)
  
  
    
     
    
  pass #TODO:



# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]