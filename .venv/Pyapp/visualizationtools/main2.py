def tailRecursion_renderer(n, accumulator=0):
    # base case: stop when n reaches 0
    if n == 0:
        return accumulator
    # recursive case: last action is the recursive call
    return tailRecursion_renderer(n - 1, accumulator + 1)


# test call
print(tailRecursion_renderer(5))  # Output: 5