class Solution {
    public boolean isPalindrome(String s) {
        
        s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        
        char[] chArray = new char[s.length()];
        String reversed = new StringBuilder(s).reverse().toString();
        
        return s.equals(reversed);
    }
}