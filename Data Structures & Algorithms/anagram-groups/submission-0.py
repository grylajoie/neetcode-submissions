class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = []
        dict = {}

        for str in strs:
            sortedString = ''.join(sorted(str))
            if sortedString in dict:
                dict[sortedString].append(str)
            else:
                dict[sortedString] = [str]

        for key in dict:
            group.append(dict[key])
            print(group)
       
        return group
