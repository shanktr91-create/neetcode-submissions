class Solution {
public:
    int maxProfit(vector<int>& prices) {

        //std::vector<int> minarr(prices.size()); 
        
        int max_profit = 0;
        int min = prices[0];
        int idx = 0;
        for(int i: prices){
            if(i<min){
                min = i;
            }
            
            int profit = prices[idx] - min;
            if(profit > max_profit){
                max_profit = profit;
            }
            idx++;
        
        }

    return max_profit; 
    }
};
