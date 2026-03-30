class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        for (int i = 0; i < heights.length; i++ ){

            for (int j = i + 1; j < heights.length; j++ ){
                int width = j - i;
                int height = 0;
                if (heights[j] < heights[i]) height = heights[j];
                else height = heights[i];

                int area = width * height;
                if (area > maxArea) maxArea = area;
            }
        }
        return maxArea;
    }
}
