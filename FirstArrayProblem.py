'''Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
'''


a = [10, 20, 4]
largest_num = 0
for num in a :
  if largest_num < num:
      largest_num = num

print(largest_num)

    
  