import java.util.List;
import java.util.ArrayList;

public class adj_flowerpots {
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;

        // fill out bed with empty spots at beginning and end of flowerbed
        List<Integer> largerBed = new ArrayList<Integer>();
        largerBed.add(0);
        for (int i = 0; i < flowerbed.length; i++) {
            largerBed.add(flowerbed[i]);
        }
        largerBed.add(0);

        for (int j = 1; j < largerBed.size() - 1; j++) {
            if (largerBed.get(j) == 0 && largerBed.get(j - 1) == 0 && largerBed.get(j + 1) == 0) {
                largerBed.set(j, 1);
                count++;
            }
        }

        return (count >= n);
    }

    public static void main(String[] args) {
        int[] flowerbed = new int[] { 1, 0, 0, 0, 1 };
        int newFlowers = 1;
        System.out.println(canPlaceFlowers(flowerbed, newFlowers));

    }

}

/*
 * Calculate how many open spots are valid in the flowerbed
 * Compare the num of open spots to num newFlowers
 * In order to get num open spots:
 * - create a list with 0's at front and end of given array to simulate open
 * spots
 * - iterate over list starting at 1 and ending at second to last
 * - if == 0, plant flower and incrememnt count
 * - if count >= n then return true
 * 
 * Test cases:
 * flowerbed = [0]
 * flowerbed = [0,0]
 * flowerbed = [1,0]
 * flowerbed = [0,0,1,0,0]
 * flowerbed = [1,0,0,0,1]
 */
