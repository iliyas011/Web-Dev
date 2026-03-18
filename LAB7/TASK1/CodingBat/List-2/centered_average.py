def centered_average(nums):
  
  
  total_sum = sum(nums)
  largest = max(nums)
  smallest = min(nums)
  return (total_sum - largest - smallest) // (len(nums) - 2)