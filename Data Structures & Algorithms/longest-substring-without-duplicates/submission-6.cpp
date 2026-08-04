#include <unordered_set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_set<char> unique_char;

        int left = 0;
        int max_len = 0;

        for (int right = 0; right < s.size(); right++) {

            while (unique_char.count(s[right])) {
                unique_char.erase(s[left]);
                left++;
            }


            unique_char.insert(s[right]);

            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};