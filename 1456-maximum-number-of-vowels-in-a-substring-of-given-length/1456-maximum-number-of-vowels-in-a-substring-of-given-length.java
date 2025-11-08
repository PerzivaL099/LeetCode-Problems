class Solution {
    public int maxVowels(String s, int k) {
        //Vowel List
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        int currentVowels = 0;
        //Fill window
        for(int i= 0; i < k; i++){
            if(vowels.contains(s.charAt(i))){
                currentVowels++;
            }
        }

        int maxVowels = currentVowels;
        //Slide Window
        for(int i = k; i < s.length(); i++){

      

            char charIn = s.charAt(i);
            char charOut = s.charAt(i - k);

            if(vowels.contains(charIn)){
                currentVowels++;
            }
            
            if(vowels.contains(charOut)){
                currentVowels--;
            }

            maxVowels = Math.max(maxVowels, currentVowels);
        }
        return maxVowels;
    }
}
    
