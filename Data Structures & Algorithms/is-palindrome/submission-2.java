class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        char[] chArray = s.toCharArray();

        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(chArray[left])) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(chArray[right])) {
                right--;
            }

            if (chArray[left] != chArray[right]) {
                return false;
            }

            left++;
            right--;
        }
        return true;
    }
}
