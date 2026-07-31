
#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        std::unordered_map<int,int> num; 

        int lent = nums.size();

        for(int i=0; i<lent;i++)
        {
            if(num.contains(nums[i])){
                return true;
            }
            else{
                num[nums[i]]=0;
            }
        }

        return false;
        
    }
};