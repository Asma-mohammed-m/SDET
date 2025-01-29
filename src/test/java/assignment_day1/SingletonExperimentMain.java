package assignment_day1;

public class SingletonExperimentMain {
	
	
	

	public static void main(String[] args) {
		// Get the single instance of Logger
		SingletonExperimentSub_Logger logger1 = SingletonExperimentSub_Logger.getInstance();
        logger1.log("This is the first log message.");
        System.out.println(logger1);

        // Try to get another instance
        SingletonExperimentSub_Logger logger2 = SingletonExperimentSub_Logger.getInstance();
        logger2.log("This is the second log message.");
        System.out.println(logger2);

        // Verify that logger1 and logger2 are the same instance
        if (logger1 == logger2) {
            System.out.println("Both logger1 and logger2 are the same instance.");
            System.out.println(logger1);
            System.out.println(logger2);
            
        }

	}

}
