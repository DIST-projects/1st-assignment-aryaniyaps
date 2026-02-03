
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {

    int add(int a, int b) throws RemoteException;

    double multiply(double a, double b) throws RemoteException;

    String echo(String msg) throws RemoteException;
}
