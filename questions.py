QUESTIONS = [
        {
                'title': 'Trapping Rain Water',
                'difficulty': 'Easy',
                'text': 'Given n non-negative integers representing an elevation map where the width of each bar is 1, compute volume of '
                        'water it is able to trap after raining.',
                'input': """The first line of input contains the size of the array, n
The following line of input contains n space-separated integers

Constraints:-
1 <= n <= 50000
0<=A[i]<=10<sup>10</sup>""",
                'output': 'The first and only line of output contains integer, in accordance to the task.',
                'example': """Sample Input:
6
3 0 0 2 0 4
Sample Output:
10"""
        },
        {
                'title': 'Merge Overlapping Intervals',
                'difficulty': 'Medium',
                'text': 'Given two integer arrays X and Y of size N each. For each i, (X[i], Y[i]) represents a interval. Merge all the '
                        'overlapping intervals and print mutually exclusive intervals in increasing order. Two intervals [XA, '
                        'YA] and [XB, YB] are overlapping if XA <= XB <= YA and the merged interval is [ XA , max(YA, YB)].',
                'input': """First line contains an integer N
Next line contains N space separated integers denoting the contents of array X.
Next line contains N space separated integers denoting the contents of array Y.

Constraints:
1 <= N <= 10^4
0 <= X[i] <= Y[i]<= 10^5""",
                'output': 'Print the merged intervals in increasing order. So each line contains two space separated integers X and Y.',
                'example': """Sample Input 1:
4
6 1 2 4
8 9 4 7

Output 
1 9

Explanation:
All the intervals are overlapping so all can be merged together and we get [1, 9]

Sample Input 2:
2
2 4
3 5

Output
2 3
4 5

Explanation
Both the intervals don't overlap. So, print it as it is."""
        },
        {
                'title': 'Combination Sum',
                'difficulty': 'Medium',
                'text': """<p>Given an array of&nbsp;<strong>distinct</strong>&nbsp;integers&nbsp;<code>arr</code>&nbsp;and a target 
                integer&nbsp;<code>target</code>, return count<em>&nbsp;of all&nbsp;<strong>unique 
                combinations</strong>&nbsp;of&nbsp;</em><code>arr</code><em>&nbsp;where the chosen numbers sum 
                to&nbsp;</em><code>target</code><em>.</em></p>

<p>The&nbsp;<strong>same</strong>&nbsp;number may be chosen from&nbsp;<code>arr</code>&nbsp;an&nbsp;<strong>unlimited number of 
times</strong>. Two combinations are unique if the frequency of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to&nbsp;<code>target</code>&nbsp;is less 
than&nbsp;<code>150</code>&nbsp;combinations for the given input.</p>
""",
                'input': """First line contains a single integer n- length of nums.
Second line contains elements of nums. 
Third line contains a single integer- target.

Constraints:
1 <= nums. length <= 40
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000""",
                'output': 'Print the number of possible combinations that add up to target.',
                'example': """Input:
3
1 2 3
3
Output:
3
"""
        },
        {
                'title': 'Min Cut Tree',
                'difficulty': 'Medium',
                'text': 'Given an integer K and an array height[] of size N, where height[i] denotes the height of the ith tree in a '
                        'forest. The task is to make a cut of height X from the ground such that at max K units wood is collected. Find '
                        'the minimum value of X <b>If you make a cut of height X from the ground then every tree with a height greater '
                        'than X will be reduced to X and the remaining part of the wood can be collected</b>',
                'input': """The first line contains two integers N and K.
The next line contains N integers denoting the elements of the array height[]

<b>Constraints</b>
1 &le; N &le; 10<sup>5</sup>
1 &le; arr[i] &le; 10<sup>5</sup>
1 &le; K &le; 10<sup>7</sup>""",
                'output': 'Print a single integer with the value of X.',
                'example': """Sample Input:
4 2
1 2 1 2

Sample Output:
1

<b>Explanation:</b>
Make a cut at height 1, the updated array will be {1, 1, 1, 1} and
the collected wood will be {0, 1, 0, 1} i. e. 0 + 1 + 0 + 1 = 2."""
        },
        {
                'title': 'Minimum Swaps',
                'difficulty': 'Hard',
                'text': 'Given two arrays of size N which have the same values but in different orders, we need to make a second array '
                        'the same as a first array using a minimum number of swaps. Note:- It is guaranteed that the elements of the '
                        'array are unique',
                'input': """First line of input contains the size of array N, second line of input contains N space separated integers 
                depicting values of first array, third line of input contains N space separated integers depicting values of second array.

Constraints:-
1 < = N < = 10000
1 < = Arr[i] < = 1000000000""",
                'output': 'Print the minimum number of swaps required to make the second array equal to first.',
                'example': """Sample Input:-
5
1 2 3 4 5
3 1 2 5 4

Sample Output:-
3

Sample Input:-
4
3 6 4 8
4 6 8 3

Sample Output:-
2"""
        }
]
