import java.util.*;  

class Table
{
    public static void main (String args[]){
    System.out.println("tables");
      System.out.println("ENTER A NUMBER ");
        Scanner sc= new Scanner(System.in);

        int num =sc.nextInt();
      
        for (int i=1; i<11; i++){
            System.out.println(""+num+"*"+i+"="+num*i);
        }
    }

}