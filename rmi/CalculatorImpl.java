
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalculatorImpl extends UnicastRemoteObject implements Calculator {

    protected CalculatorImpl() throws RemoteException {
        super();
    }

    public int add(int a, int b) throws RemoteException {
        return a + b;
    }

    public double multiply(double a, double b) throws RemoteException {
        return a * b;
    }

    public String echo(String msg) throws RemoteException {
        return "ECHO: " + msg;
    }
}
