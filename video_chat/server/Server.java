package server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
  public static void main(String[] args) throws IOException {
    ServerSocket ss = new ServerSocket(8000);
    Socket s = ss.accept();
    System.out.println(s);
  }
}
