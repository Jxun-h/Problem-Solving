import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        String temp = Integer.toString(n, m);
        System.out.println(temp.toUpperCase());
    }
}