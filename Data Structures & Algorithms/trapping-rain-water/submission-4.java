class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int area = 0;
        int maxLeft = 0;
        int maxRight = 0;
        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] >= maxLeft) maxLeft = height[left];
                else area = area + (maxLeft - height[left]);
                left++;
            }
            else {
                if (height[right] >= maxRight) maxRight = height[right];
                else area = area + (maxRight - height[right]);
                right--;
            }
        }
        return area;
    }
}
