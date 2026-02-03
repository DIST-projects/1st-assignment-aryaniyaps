
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RmiClient {

    public static void main(String[] args) {
        String host = (args.length < 1) ? "localhost" : args[0];
        try {
            Registry registry = LocateRegistry.getRegistry(host);
            Calculator stub = (Calculator) registry.lookup("CalculatorService");
            System.out.println("add(5,7) -> " + stub.add(5, 7));
            System.out.println("multiply(2.5,4) -> " + stub.multiply(2.5, 4));
            System.out.println("echo('hi') -> " + stub.echo("hi"));
        } catch (Exception e) {
            System.err.println("RMI client exception:");
            e.printStackTrace();
        }
    }
}
