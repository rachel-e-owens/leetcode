import java.util.Arrays;

class product_array_except_self {
    public static int[] productExceptSelf(int[] nums) {
        int[] products = new int[nums.length]; // array to hold products
        /*
         * Too slow
         * for (int i = 0; i < nums.length; i++) {
         * int product = 1;
         * int j = 0;
         * while (j < nums.length) {
         * if (j != i) {
         * product = product * nums[j];
         * }
         * j++;
         * }
         * products[i] = product;
         * }
         */
        int prefix = 1;
        int postfix = 1;

        // iterate prefix
        for (int i = 0; i < nums.length; i++) {
            products[i] = prefix;
            prefix = prefix * (nums[i]);
            System.out.println(Arrays.toString(products));
        }

        // iterate postfix
        for (int j = nums.length - 1; j >= 0; j--) {
            products[j] = postfix * products[j];
            postfix = postfix * (nums[j]);
            System.out.println(Arrays.toString(products));
        }
        return products;
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 2, 3, 4 };
        System.out.println(Arrays.toString(productExceptSelf(nums)));

    }
}