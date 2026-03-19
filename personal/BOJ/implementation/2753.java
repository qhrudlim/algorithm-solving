// 윤년
// bronze 5

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int A = Integer.parseInt(br.readLine());

    System.out.print( (A%4 == 0) ? ((A%400 == 0) ? "1" : (A%100 == 0) ? "0" : "1") : "0" );
  }
}
