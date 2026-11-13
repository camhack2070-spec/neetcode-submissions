class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> twosum;
        for(int i = 0;i < nums.size();++i)
        {
            for(int j = i + 1;j < nums.size();++j)
            {
                if((nums[i] + nums[j]) == target)
                {
                    twosum.push_back(i);
                    twosum.push_back(j);
                }
            }
        }
        return twosum;
    }
};
