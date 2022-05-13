# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:26:51 2022

@author: Parths
"""

#User function Template for python3

class Solution:
    def countWays(self, N):
        # code here
        counter = ((N+1)*(N+2))//2
        return counter

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input("Number: "))
    for _ in range(t):
        N = int(input("no> "))
        
        ob = Solution()
        print(ob.countWays(N))
# } Driver Code Ends