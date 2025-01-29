package assignment_day1;

import java.util.Arrays;

public class ArrayExperiment {
	
	/*
	 * Arrays and Array Manipulation • Write a Java program to: • Create an array of
	 * integers with 10 elements. • Find the largest and smallest element in the
	 * array. • Reverse the array and print it. • Find the sum and average of all
	 * elements in the array.
	 */

	public static void main(String[] args) {
        // Create an array of integers with 10 elements
        int[] arr = {12, 45, 7, 89, 34, 23, 67, 90, 5, 11};

        // Find the largest and smallest element in the array
        int largest = arr[0];
        int smallest = arr[0];
        int sum = 0;

        for (int num : arr) {
            if (num > largest) {
                largest = num;
            }
            if (num < smallest) {
                smallest = num;
            }
            sum += num;
        }

        // Reverse the array
        int[] reversedArray = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            reversedArray[i] = arr[arr.length - 1 - i];
        }

        // Calculate average
        double average = (double) sum / arr.length;

        // Print results
        System.out.println("Original Array: " + Arrays.toString(arr));
        System.out.println("Largest Element: " + largest);
        System.out.println("Smallest Element: " + smallest);
        System.out.println("Reversed Array: " + Arrays.toString(reversedArray));
        System.out.println("Sum of Elements: " + sum);
        System.out.println("Average of Elements: " + average);
    }

}
