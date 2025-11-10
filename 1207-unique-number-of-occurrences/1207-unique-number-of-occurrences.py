class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #Dictionary to store instances
        count_map = {}

        #Iterate through array
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1

        seen_counts = set()

        for count in count_map.values():
            if count in seen_counts:
                return False

            seen_counts.add(count)

        return True
