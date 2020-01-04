def insertionSort(l):
  for i in range(1, len(l)):
      val = l[i]

      j = i - 1
      while j >= 0 and l[j] > val:
        l[j + 1] = l[j]
        j -= 1
      l[j + 1] = val

  return l;

l = [2, 4, 3, 1, 5]
print(l)
print(insertionSort(l));
