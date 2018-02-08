"""
Problem Statement
    	The holidays are near. Hero would like to buy some candies, so he went to the store. In the store he found some boxes. Each box has a label with three positive integers a[i], b[i], and cost[i]. Their meaning is as follows: Obviously, cost[i] is the amount Hero has to pay to buy this box. The other two numbers promise that the box will contain exactly a[i] red candies and exactly b[i] blue candies (and nothing else). Hero knows that the total number of candies always matches the label, but the colors sometimes don't. Sometimes, exactly one candy in the box has the opposite color. Thus, for each box we have three possibilities: instead of (a[i] red, b[i] blue) we can also get (a[i]+1 red, b[i]-1 blue) or (a[i]-1 red, b[i]+1 blue). Hero is going to buy some of the boxes. Then, he will bring them home, he will unpack all boxes and pool all candies together. Hero will be happy if the final pile of candies will contain at least K candies of the same color. Find the cheapest set of boxes such that it is guaranteed that Hero will be happy if he buys these boxes. Return the cost of that set of boxes. If it is impossible to guarantee Hero's happiness, return -1 instead.
 
Definition
    	
Class:	Unpacking
Method:	getcost
Parameters:	int[], int[], int[], int
Returns:	int
Method signature:	int getcost(int[] a, int[] b, int[] cost, int K)
(be sure your method is public)
    
 
Constraints
-	a, b and cost will contain the same number of elements.
-	a will contain between 1 and 50 elements, inclusive.
-	Each element in a, b and cost will be between 1 and 10,000, inclusive.
-	K will be between 1 and 10,000, inclusive.
 
Examples
0)	
    	
{6,5}
{4,4}
{1,1}
10
Returns: 2
There are two boxes, each with cost 1. One box promises to hold 6 red + 4 blue candies, the other promises to hold 5 red + 4 blue ones. Hero will be happy if he opens 10 candies of the same color. Clearly, buying just one box is not enough. Is Hero guaranteed to be happy if he buys both of them? As it turns out, yes. In most cases, he will open at least 10 red candies and he will be happy. The only case in which that won't happen is the case when the first box actually contains 5 red + 5 blue and the second box contains 4 red + 5 blue candies. However, in this case Hero will also be happy, because he will open 10 blue candies.
1)	
    	
{5,5}
{4,4}
{1,1}
10
Returns: -1
Even if Hero buys both boxes, it is possible that he will only open 9 red + 9 blue candies in total.
2)	
    	
{10}
{5}
{13}
9
Returns: 13
3)	
    	
{1,2,3,4,5}
{1,2,3,4,5}
{1,2,3,4,5}
10
Returns: 10
4)	
    	
{1,2,3,4,15}
{1,2,3,4,5}
{1,2,3,4,5}
17
Returns: 9
"""


