// 1998년생인 내가 태국에서는 2541년생?!
// bronze 5

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P18108{
  public static void main(String[] arg) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String yearStr = br.readLine();
    int yearInt = Integer.parseInt(yearStr);

    System.out.println(yearInt - 543);
  }
}
