def longestIncreasingSequence(l):
  result, seq = 0, 0
  for i in range(len(l)-1):
    if (l[i] > l[i-1]):
      seq += 1
    else:
      if (seq > result):
        result = seq
      seq = 0
  print(l)
  print("longest increasing sequence is: " + str(result))

longestIncreasingSequence([1,6,9,1,3,2,7,9])
