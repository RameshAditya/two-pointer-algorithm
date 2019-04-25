'''
code for the first algo challenge on my blog post -
number of elements A[j], such that A[i]<=A[j]<=2*A[i]

Algo: Described in blog post.
'''
def first(A):
    n = len(A)
    assert A == sorted(A)
    i = 0
    j = 0
    ans = [0 for i in range(n)]
    for i in range(n):
        while j+1<n and A[j+1]>=A[i] and A[j+1]<=2*A[i]:
            j+=1
        ans[i] = j-i
    return ans

'''
code for the second algo challenge on my blog post -
number of substrings of string S with <= K unique alphabets

Algo: Described in blog post.
'''
def second(s, k):
    n = len(s)
    ans = 0
    hsh = [0 for i in range(26)]
    ct = 0
    i = 0
    j = 0
    for i in range(n):
        while j < n and ct<=k:
            if hsh[ord(s[j]) - ord('a')] == 0 and ct==k:
                break
            else:
                hsh[ord(s[j]) - ord('a')] += 1
                if hsh[ord(s[j]) - ord('a')] == 1:
                    ct += 1
            j+=1
        ans += j-i
        hsh[ord(s[i]) - ord('a')] -= 1
        if hsh[ord(s[i]) - ord('a')] == 0:
            ct -= 1
    return ans
            
'''
code for the third algo challenge on my blog post - 
number of pairs A[i] and B[j] such that A[i] * B[j] <= k

Algo:
- Find the largest element in B (call it B[j]) such that A[0]*B[j] <= k
- All indices less than j therefore will also be valid pairs
- As i increases, j will decrease
- Profit
'''
def third(A, B, k):
    A.sort()
    B.sort()
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    ans = 0

    while j<m:
        if A[0]*B[j] <= k:
            j+=1
        else:
            break
    j-=1
    for i in range(n):
        while j>=0 and A[i]*B[j] > k:
            j-=1
        ans += j+1
    return ans

'''
code for the fourth algo challenge
number of substrings of less than K unique alphabets that each index is part of

Algo:
- Same as second, find the largest substring from each index
- Now each of these elements must be included in each others answers
- Equivalent to multiple range sum updates
- Use difference arrays
- Profit
'''
def fourth(s, k):
    n = len(s)
    ans = [0 for i in range(n)]
    hsh = [0 for i in range(26)]
    ct = 0
    i = 0
    j = 0
    for i in range(n):
        while j < n and ct<=k:
            if hsh[ord(s[j]) - ord('a')] == 0 and ct==k:
                break
            else:
                hsh[ord(s[j]) - ord('a')] += 1
                if hsh[ord(s[j]) - ord('a')] == 1:
                    ct += 1
            j+=1
        ans[i] = j-i
        hsh[ord(s[i]) - ord('a')] -= 1
        if hsh[ord(s[i]) - ord('a')] == 0:
            ct -= 1

    diff = [0 for i in range(n+1)]
    for i in range(n):
        diff[i] += 1
        diff[i+ans[i]]-=1
    for i in range(1, n+1):
        diff[i] += diff[i-1]
    return diff[:-1]
    # diff[i] now stores how many substrings of <= k unique chars
    # that s[i] is a part of


        
