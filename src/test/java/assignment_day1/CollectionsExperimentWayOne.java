package assignment_day1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;

public class CollectionsExperimentWayOne {
	/*
	 * Collections Framework (List, Set, Map) Write a program to: • Create an
	 * ArrayList of integers, add some elements, and print the list. • Sort the list
	 * in ascending order and print the sorted list. • Create a HashSet to store
	 * unique names and display them. • Create a HashMap to store student names as
	 * keys and their scores as values. Then, print the map.
	 */

	public static void main(String[] args) {
		// 1. Create an ArrayList of integers, add elements, and print the list
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        numbers.add(25);
        numbers.add(10);
        numbers.add(5);
        numbers.add(30);
        numbers.add(15);

        System.out.println("Original List: " + numbers);

        // 2. Sort the list in ascending order and print the sorted list
        Collections.sort(numbers);
        System.out.println("Sorted List: " + numbers);

        // 3. Create a HashSet to store unique names and display them
        HashSet<String> names = new HashSet<String>();
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        names.add("Alice"); // Duplicate will be ignored
        names.add("David");

        System.out.println("Unique Names (HashSet): " + names);

        // 4. Create a HashMap to store student names as keys and their scores as values
        HashMap<String, Integer> studentScores = new HashMap<String, Integer>();
        studentScores.put("John", 85);
        studentScores.put("Emma", 92);
        studentScores.put("Liam", 78);
        studentScores.put("Sophia", 95);
        studentScores.put("Oliver", 88);

        // Print the HashMap
        System.out.println("Student Scores (HashMap): " + studentScores);
    }

}
