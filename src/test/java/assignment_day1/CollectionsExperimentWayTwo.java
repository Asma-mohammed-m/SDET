package assignment_day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;

public class CollectionsExperimentWayTwo {

	/*
	 * Collections Framework (List, Set, Map) Write a program to: • Create an
	 * ArrayList of integers, add some elements, and print the list. • Sort the list
	 * in ascending order and print the sorted list. • Create a HashSet to store
	 * unique names and display them. • Create a HashMap to store student names as
	 * keys and their scores as values. Then, print the map.
	 */
	
	public static void main(String[] args) {
		// 1. Create an ArrayList, add elements, and print the list
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(42, 7, 15, 89, 23, 56));
        System.out.println("Original List: " + numbers);

        // Sort the list in ascending order
        Collections.sort(numbers);
        System.out.println("Sorted List: " + numbers);

        // 2. Create a HashSet to store unique names and display them
        HashSet<String> names = new HashSet<>(Arrays.asList("Alice", "Bob", "Charlie", "Alice", "Eve", "Bob"));
        System.out.println("Unique Names: " + names);

        // 3. Create a HashMap to store student names and scores
        HashMap<String, Integer> studentScores = new HashMap<>();
        studentScores.put("John", 85);
        studentScores.put("Emma", 92);
        studentScores.put("Lucas", 78);
        studentScores.put("Sophia", 88);
        studentScores.put("Emma", 95); // Updating Emma's score

        // Print the HashMap
        System.out.println("Student Scores: " + studentScores);

	}

}
