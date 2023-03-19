def palindrome(lst):
    n = len(lst)
    for i in range(n // 2):
        if lst[i] != lst[n - i - 1]:
            return False
    return True

