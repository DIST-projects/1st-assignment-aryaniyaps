
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RmiServer {

    public static void main(String[] args) {
        try {
            CalculatorImpl obj = new CalculatorImpl();
            // create registry on 1099
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("CalculatorService", obj);
            System.out.println("RMI server bound CalculatorService on port 1099");
        } catch (Exception e) {
            System.err.println("RMI server exception:");
            e.printStackTrace();
        }
    }
}
