class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        res=int("".join(reversed(str(x))))
        res=res*sign
        if res<-2**31 or res>2**31 -1:
            return 0
        return res