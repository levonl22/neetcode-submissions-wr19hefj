class Solution {

    public String encode(List<String> strs) {
        String res = "";
        for (String s : strs) {
            res += s.length() + "#" + s;
        }
        return res;
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();

        //5#Hello5#World
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + length;
            res.add(str.substring(i, j));
            i = j;
        }
        return res;
    }
}
