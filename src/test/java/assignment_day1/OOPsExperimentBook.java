package assignment_day1;

public class OOPsExperimentBook {
	
	/*
	 * Object-Oriented Programming (OOP) Concepts • Create a class Book with the
	 * following attributes: • Title (String) • Author (String) • Price (double) •
	 * Include constructors, getters, and setters for each attribute. • Implement a
	 * method displayDetails() to print the book details. • Create an instance of
	 * the class and display the details.
	 */
	
	private String title;
    private String author;
    private double price;

    // Constructor
    public OOPsExperimentBook(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    // Getters
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public double getPrice() {
        return price;
    }

    // Setters
    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    // Method to display book details
    public void displayDetails() {
        System.out.println("Book Details:");
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: $" + price);
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		OOPsExperimentBook myBook = new OOPsExperimentBook("The Alchemist", "Paulo Coelho", 19.99);

        // Displaying book details
        myBook.displayDetails();

	}

}
