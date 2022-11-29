#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                    
                    
                    
#java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i,j;
        for(i=0; i<nums.length; i++){
            for(j=i+1; j<nums.length; j++){
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
        return nums;
    }
}
