def feedDog(hunger_level, biscuit_size):
    '''Description: The arrays are being sorted in descending order. I want to see which dog would like
    the bigger biscuit first then iterating through till each dog has been feed while incrementing
    by 1'''
    hunger_level.sort(reverse=True)  # Set to sort
    biscuit_size.sort(reverse=True)
    level = len(hunger_level)  # Array lengths of both hunger_level and biscuit_size
    size = len(biscuit_size)
    food_gone = 0  # Initialize food counter
    hunger = 0  # Initialize indexes for hunger and biscuit
    biscuit = 0
    while hunger != level and biscuit != size:  # While loop
        if hunger_level[hunger] <= biscuit_size[biscuit]:  # Set to increment
            hunger += 1
            biscuit += 1
            food_gone += 1
        else:  # Set to check if dog has been given biscuit and keep going
            hunger += 1
    return food_gone  # Return once all dogs have been given biscuit


print(feedDog([1, 2, 3], [1, 1]))
print(feedDog([2, 1], [1, 2, 3]))
print(feedDog([2, 1, 3, 4], [1, 2]))
print(feedDog([1, 1, 3, 4], [4, 4, 4]))
print(feedDog([1, 2, 3, 4], [5, 4, 6, 7]))
print("Time Complexity is O(n logn)")

'''
Cited Sources:
Author: DURepo
Date: Exploration from Canvas
URL: https://github.com/DURepo/CS_325_Exercises/blob/main/Greedy-activity_selection.py
Code: 
def activity_selection(activities, start_times,end_times):
    result = []
    blocked_time = 0
    count = len(activities)
    for i in range(count):
        if(start_times[i] >= blocked_time):
            result.append(activities[i])
            blocked_time = end_times[i]

    return result

result=activity_selection(["Play Golf", "Paint", "Cook", "Sleep", "Jog", "Code", "Eat"],  [1, 3, 1, 3, 4, 6, 8], [3, 4, 4, 6, 6, 9, 9])
print(result)
-------------------------------------------------------------------------
Author: Techie Delight
URL: https://www.techiedelight.com/activity-selection-problem-using-dynamic-programming/
Code: 
# Returns the maximum count of non-conflicting jobs that can be performed
# by a single person
def findNonConflictingJobsLength(jobs):

    # Sort the jobs according to increasing order of their start time
    jobs.sort(key=lambda x: x[0])

    # L[i] stores the maximum count of non-conflicting jobs ending at i'th job
    L = [0] * len(jobs)

    for i in range(len(jobs)):
        # consider each `j` less than `i`
        for j in range(i):
            # L[i] = max(L[j]), where `jobs[j].finish` is less than `jobs[i].start`
            if jobs[j][1] < jobs[i][0] and L[i] < L[j]:
                L[i] = L[j]

        # increment L[i] since it ends at the i'th job
        L[i] = L[i] + 1

    # return the maximum job length in the list
    return max(L)


if __name__ == '__main__':

    # Each pair stores the start and the finish time of a job
    jobs = [
        (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
        (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)
    ]
--------------------------------------------------------------------
Author: Nikhil Kumar Singh
URL: https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
Code:
"""The following implementation assumes that the activities
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

def printMaxActivities(s , f ):
    n = len(f)
    print ("The following activities are selected")

    # The first activity is always selected
    i = 0
    print (i,end=' ')

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print (j,end=' ')
            i = j

# Driver program to test above function
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)
------------------------------------------------------------------------
Author: Data Structures and Algorithms
URL: https://algodaily.com/lessons/getting-to-know-greedy-algorithms-through-examples
Code:
routine greedyNavigate
Input: Matrix w of dimensions m * n containing reward for each cell,
Start cell coordinates: (0, 0)
Goal cell coordinates: (m-1, n-1)
Output: Path found and the accumulated reward on that path

// (r, c) denotes (row, column) coordinates
1. total = 0
2. (r, c) = (0,0)
3. while (r, c) != goal
    a. total = total + w[r, c]
    b. print (r, c)           // print coordinates of the cell
    // check if we are in top row
    c. if (r == m-1)
        c = c+1             // go right. no other choice
    // check if we are in rightmost col
    d. if (c == n-1 )
        r = r+1             // go up, no other choice
    // greedily select either up or right move
    e. if w[r+1, c] > w[r, c+1]
            r = r+1                 // move up
        else
            c = c+1                 // move right
4. Print goal
5. return total                     // return accumulated reward

Code:
Routine selectActivity
Input: Finish time array f
Output: Selected activity array S and total activities in S

1. count = 0
2. S[count] = 0
3. lastInd = 0                  // index of last activity added to S
4. for i = 1..(n-1)
    a. if s[i] >= f[lastInd]    // add i to selected activity set S
        then
        {
            i. count = count + 1
            ii. S[count] = i
            iii. lastInd = i
        }
5. return (count + 1) and S

Code: 
Routine: solveKnapsack
Input: Weight array w, value array v of size n,
        X = capacity of knapsack
Output: Array R containing indices of items in the sack and
        array Rwt that has the corresponding weight of
        each item in the sack,
        val: total value of items in sack,
        RInd: total items added in sack

1. Initialize array R to -1 and array Rval to zero
2. Create an array Y containing value of each item per unit of weight
   Y[i] = v[i]/w[i] for i = 0..(n-1)
3. Create an array Z, which has indices of the sorted values of Y in descending order.
4. remaining = X
5. i = 0
6. val = 0
7. RInd = 0
8. while (i < n and remaining < X)
    a. toadd = min(remaining, w[Z[i]])
    b. R[RInd] = Z[i]
    c. Rwt[RInd] = toadd
    d. val = val + val[Z[i]] * toadd
    e. remaining = remaining - toadd
    f. i = i+1
    g. RInd = RInd + 1
9. return R, Rwt, val, RInd
-----------------------------------------------------------------------------
Concept of Greedy Algorithms: https://www.guru99.com/greedy-algorithm.html

--------------------------------------------------------------------------
Concept of Greedy Algorithms: https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

----------------------------------------------------------------------
Concept of Greedy Algorithms: https://www.geeksforgeeks.org/check-if-two-arrays-can-be-made-equal-by-reversing-any-
subarray-once/
--------------------------------------------------------------------

'''
