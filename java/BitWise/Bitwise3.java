public class Bitwise3 {
    public static void main(String[] args) {
        int a = 22;
        int b = 44;
        int c = 55;
        // String result =a>b && a>c? a+"is greatest":(b>c? b+ "is greatest":c+ "is
        // greatest");
        int result = a > b && a > c ? a : (b > c ? b : c);
        System.out.println(result + " is greatest");
        // System.out.println(result);
    }
}
