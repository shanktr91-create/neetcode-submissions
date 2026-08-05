class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Frequency of characters we need
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        # Frequency inside current window
        window = {}

        have = 0                  # Number of characters whose required frequency is satisfied
        need_count = len(need)    # Number of distinct characters we need

        left = 0

        ans = [-1, -1]
        ans_len = float("inf")

        for right in range(len(s)):

            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Did this character just become satisfied?
            if c in need and window[c] == need[c]:
                have += 1

            # Current window contains every required character
            while have == need_count:

                # Update answer
                if (right - left + 1) < ans_len:
                    ans = [left, right]
                    ans_len = right - left + 1

                # Remove left character
                window[s[left]] -= 1

                # Did removing it break the requirement?
                if s[left] in need and window[s[left]] <need[s[left]]:
                    have -= 1

                left += 1

        l, r = ans

        return "" if ans_len == float("inf") else s[l:r+1]