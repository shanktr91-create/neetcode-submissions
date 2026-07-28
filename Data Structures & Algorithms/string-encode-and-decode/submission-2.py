class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ''
        for i in strs:
            newstr+=i+"~"
        return newstr

    def decode(self, s: str) -> List[str]:

        list1 = s.split("~")
        list1.pop()
        return list1
    
