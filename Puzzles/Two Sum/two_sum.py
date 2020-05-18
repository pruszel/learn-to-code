def twoSum(ar, s):
    sums = []
    m = {}
    for i in range(len(ar)):
        diff = s - ar[i]
        if diff in m:
            print("found one!", ar[i], "+", m[diff]);
        m[ar[i]] = ar[i]


twoSum([3, 5, 2, -4, 8, 11], 7);

