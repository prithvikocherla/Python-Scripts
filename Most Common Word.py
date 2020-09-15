import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(word for word in paragraph.lower().split())
        print(count)
        
        ans = []
        for i in sorted(set(count.values()),reverse=True):
            for key, value in filter(lambda x :x[1]==i,count.items()):
                if count[key] == i and key not in banset:
                    ans.append(key)
            if(ans):
                break               

        return ans

if __name__ == '__main__':
    x= Solution()
    q= x.mostCommonWord("Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
                        ,["and","he","the","to","is","jack","jill"])
    print(q)