import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.MessageProperties;
import java.util.Scanner;

public class jobJavaClient {

  private static final String TASK_QUEUE_NAME = "task_queue";

  public static void main(String[] argv) throws Exception {
    ConnectionFactory factory = new ConnectionFactory();
    factory.setHost("192.168.184.221");                       //Direccion IP del servidor de cola
    Connection connection = factory.newConnection();
    Channel channel = connection.createChannel();

    channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);

    Scanner keyboard = new Scanner(System.in);
    System.out.println("Ingrese el nombre del archivo ");
    String message = keyboard.next();
    System.out.println(message);

    channel.basicPublish("", TASK_QUEUE_NAME,
        MessageProperties.PERSISTENT_TEXT_PLAIN,
        message.getBytes("UTF-8"));
    System.out.println("Usted envió el archivo '" + message + "'");

    channel.close();
    connection.close();
  }


}
