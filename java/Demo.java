import java.util.Scanner;

class Demo {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.println("enter amount");
      int amount = sc.nextInt();
      if (amount > 60) {
         System.out.println("butter fruit tisko");
      } else if (amount > 50) {
         System.out.println("apple tisko");
      } else if (amount > 40) {
         System.out.println("pine apple tiso");
      } else if (amount > 30) {
         System.out.println("orange tisko");
      } else if (amount <= 30) {
         System.out.println("waterbottle tisko");
      }

   }
}