def amount(A, S):
    """Description: Find all unique combinations in defined array. See if their sum is equal.
    Through recursive function, find all the possible combinations using backtracking"""
    hold = []
    A.sort(reverse=False)  # Set to sort
    amount_sum_helper(0, 0, S, hold, A)


def amount_sum_helper(amount, sum, S, hold, A):
    if sum == S:  # unique combination
        print("[", end="")
        for i in range(len(hold)):  # In Citations
            if i:
                print(", ", end="")
            print(hold[i], end="")
            for x in range(0, len(hold), (- 1)):
                print(", ", end="")
        print("]")
        return

    for i in range(amount, len(A)):  # To find all other combinations
        if sum + A[i] > S:  # Check sum
            continue
        if i > amount and A[i] == A[i - 1]:  # Continue through loop for repeated elements
            continue
        hold.append(A[i])  # Append combinations
        amount_sum_helper(i + 1, sum + A[i], S, hold, A)
        hold.pop()  # backtracking


if __name__ == '__main__':
    amount(A=[11, 1, 3, 2, 6, 1, 5], S=8)
    print("Time Complexity: exponential time ")

'''
Cited Sources:
Author: Zhubei Federer
Date: March 20, 2020
URL: https://stackoverflow.com/questions/60769609/how-to-return-the-list-of-all-the-subset-of-a-list-of-integer-using-python
Code:
import copy
def subset_helper(index, result, A, temp):
    result.append(copy.copy(temp))
    for i in range(index,len(A)):
        temp.append(A[i])
        subset_helper(i+1,result,A,temp)
        #backtracking
        temp.pop()
    return 
------------------------------------------------------------
Author: Wilfredarin
Date: March 20, 2020
URL: https://stackoverflow.com/questions/60769609/how-to-return-the-list-of-all-the-subset-of-a-list-of-integer-using-python
Code: 
def subset_helper(index, result, A, temp):
    result.append(temp)
    #print(temp)
    for i in range(index,len(A)):
        temp.append(A[i])
        subset_helper(i+1,result,A,temp)
        #backtracking
        temp.pop()
    return    
def subsets(A):
    result = []
    temp = []
    index = 0
    subset_helper(index, result, A, temp)
    return result
---------------------------------------------------------------------------
Author: Surendra_Gangwar
Date: Sept 7, 2021
URL: https://www.geeksforgeeks.org/all-unique-combinations-whose-sum-equals-to-k/?ref=lbp
Code:
def unique_combination(l, sum, K, local, A):

    # If a unique combination is found
    if (sum == K):
        print("{", end="")
        for i in range(len(local)):
            if (i != 0):
                print(" ", end="")
            print(local[i], end="")
            if (i != len(local) - 1):
                print(", ", end="")
        print("}")
        return

    # For all other combinations
    for i in range(l, len(A), 1):

        # Check if the sum exceeds K
        if (sum + A[i] > K):
            continue

        # Check if it is repeated or not
        if (i > l and
                A[i] == A[i - 1]):
            continue

        # Take the element into the combination
        local.append(A[i])

        # Recursive call
        unique_combination(i + 1, sum + A[i],
                           K, local, A)

        # Remove element from the combination
        local.remove(local[len(local) - 1])

# Function to find all combination
# of the given elements


def Combination(A, K):

    # Sort the given elements
    A.sort(reverse=False)

    local = []

    unique_combination(0, 0, K, local, A)
-----------------------------------------------------------------
Author: DURepo
Date: Exploration from Canvas
URL: https://github.com/DURepo/CS_325_Exercises/blob/main/Backtracking-combination_sum.py
Code:
from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination):

    if(remainder == 0):
        result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    print(result)

print(combination_sum([2,3,6,7], 7 ))


'''
