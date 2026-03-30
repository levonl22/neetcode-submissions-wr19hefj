class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> nums2 = new ArrayList<>();
        
        boolean result = false;

        for (int i = 0; i < nums.length; i++) {
            if (nums2.contains(nums[i])) {
                result = true;
                break;
            }
            else {
                nums2.add(nums[i]);
            }

        }
        return result;
    }
}