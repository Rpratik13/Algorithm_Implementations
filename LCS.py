string1 = input('Enter first string: ')
string2 = input('Enter second string: ')
memo = [[-1 for i in range(len(string2))] for j in range(len(string1))]

def lcs(X, Y, m, n):
    if m == len(X) or n == len(Y):
        return 0
    if memo[m][n] != -1:
        return memo[m][n]
    elif X[m] == Y[n]:
        ans = 1 + lcs(X, Y, m+1, n+1)
    else:
        ans = max(lcs(X, Y, m, n+1), lcs(X, Y, m+1, n))
    memo[m][n] = ans
    return ans

print(lcs(string1, string2, 0, 0))
for x in memo:
    print(x)
