public class merge_strings_alt {

    public static String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        String merged = null;
        int idx = 0;
        String longest, shortest = null;
        if (word1.length() > word2.length()) {
            longest = word1;
            shortest = word2;
        } else {
            longest = word2;
            shortest = word1;
        }

        for (int i = 0; i < shortest.length(); i++) {
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
            idx = i;
        }

        if (idx < longest.length()) {
            for (int j = idx + 1; j < longest.length(); j++) {
                sb.append(longest.charAt(j));
            }
        }

        merged = sb.toString();

        return merged;
    }

    public static void main(String[] args) {
        String word1 = "a";
        String word2 = "p";
        String result = mergeAlternately(word1, word2);
        System.out.println(result);
    }

}
