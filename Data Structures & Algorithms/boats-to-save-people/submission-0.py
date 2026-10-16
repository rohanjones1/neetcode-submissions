class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people)-1
        total = 0
        while (l<=r):
            curr = 0
            total += 1
            curr += people[r]
            r -= 1
            if curr + people[r] <= limit:
                r -= 1
            elif curr + people[l] <= limit:
                    l += 1
        return total
