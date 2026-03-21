// 오븐 시계
// bronze 3

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    int A = Integer.parseInt(st.nextToken());
    int B = Integer.parseInt(st.nextToken());
    
    int C = Integer.parseInt(br.readLine());

    int M = A * 60 + B + C;

    int hour = (M / 60) % 24;
    int minute = M % 60;

    System.out.println(hour + " " + minute);
  }
}
