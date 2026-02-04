cd ~/rmi# RMI (Java) Assignment

This folder contains a small Java RMI example used for Assignment 1.

Files:

- `Calculator.java` — remote interface.
- `CalculatorImpl.java` — implementation of the interface.
- `RmiServer.java` — starts the RMI registry and binds the implementation.
- `RmiClient.java` — looks up the remote object and invokes methods.

How to compile and run (local):

```
javac *.java
rmiregistry 1099 &
java RmiServer
java RmiClient
```

AWS notes:

- On EC2 open `1099` (RMI registry) and any other ports you use.
- Copy `rmi/` folder and run the same commands on the instance.
