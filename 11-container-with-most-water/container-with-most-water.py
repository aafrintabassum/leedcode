class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        mx=0
        
        while l<r:
            a=(r-l)*min(height[l],height[r])
            mx=max(mx,a)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return mx