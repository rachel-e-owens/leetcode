import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Map;
import java.util.List;

public class group_anagraphs {

    public static List<List<String>> groupAnagrams(String[] strs) {
        // HashMap to store key=sorted String, and value=List of matching Strings
        HashMap<String, ArrayList<String>> groupAn = new HashMap<>();
        // List of lists of sorted strings to return
        List<List<String>> sortedList = new ArrayList<List<String>>();

        for (int i = 0; i < strs.length; i++) {
            char[] chars = strs[i].toCharArray(); // convert string to a char array
            Arrays.sort(chars); // sort the char array
            String sorted = String.valueOf(chars); // convert sorted char array back to string

            if (groupAn.get(sorted) == null) {
                ArrayList<String> mapStrings = new ArrayList<String>();
                mapStrings.add(strs[i]);
                groupAn.put(sorted, mapStrings);
            } else {
                ArrayList<String> mapStrings = groupAn.get(sorted); // get the arraylist of strings to add to
                mapStrings.add(strs[i]);
                groupAn.put(sorted, mapStrings); // put updated list in hashmap
            }
        }

        for (Map.Entry<String, ArrayList<String>> entry : groupAn.entrySet()) {
            sortedList.add(entry.getValue());
        }

        return sortedList;
    }

    public static void main(String[] args) {
        String[] strings = new String[] { "eat", "tea", "tan", "ate", "nat", "bat" };
        List<List<String>> anagramStrings = groupAnagrams(strings);
        System.out.println(anagramStrings);
    }
}

/*
 * TEST CASES
 * 1. 1 word - bat
 * 2. 2 words - cat, tac
 * 3. No words - ""
 * 4. No anagrams - bed, cat, group
 * 5. All for one - cat, tac, act
 */

/*
 * 1. go through String array
 * 2. For each string, convert to char array
 * 3. convert back to string
 * 4. add sorted string to hashmap
 * 5. iterate through hashmap and print out each group
 */
