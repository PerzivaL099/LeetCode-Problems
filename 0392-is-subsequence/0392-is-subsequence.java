class Solution {
    public boolean isSubsequence(String s, String t) {
        //Define pointers and length of strings
        int pointerS = 0;
        int pointerT = 0;

        int lengthS = s.length();
        int lengthT = t.length();

        while(pointerS < lengthS && pointerT < lengthT){
            if(s.charAt(pointerS) == t.charAt(pointerT)){
                pointerS++;
            }
            pointerT++;
        }

        return pointerS == lengthS;
    }
}