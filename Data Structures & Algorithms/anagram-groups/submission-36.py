class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through list of strs
        # get the count of chars in each str
        # use the count of char as key to organize into res arr

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())