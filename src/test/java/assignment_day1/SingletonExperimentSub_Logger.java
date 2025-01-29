package assignment_day1;

public class SingletonExperimentSub_Logger {
	
	// Static variable to hold the single instance of the class
    private static SingletonExperimentSub_Logger instance;

    // Private constructor to prevent instantiation from outside
    private SingletonExperimentSub_Logger() {
        System.out.println("Logger initialized.");
    }

    // Public method to provide access to the single instance
    public static SingletonExperimentSub_Logger getInstance() {
        if (instance == null) {
            // Create the instance only when needed (lazy initialization)
            instance = new SingletonExperimentSub_Logger();
        }
        return instance;
    }

    // A sample method to log messages
    public void log(String message) {
        System.out.println("Log: " + message);
    }

}
