from typing import List

def two_sum(input_list: List[int], target: int) -> List[int]:
  prev_map = {}
  for i, val in enumerate(input_list):
    diff_val = target - val
    if diff_val in prev_map:
      return [prev_map[diff_val], i]
    
    prev_map[val] = i

arr = [2, 5, 7, 11, 9, 15]
target = 26

print(two_sum(arr, target))
