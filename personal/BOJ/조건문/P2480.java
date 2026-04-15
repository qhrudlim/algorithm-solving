// 주사위 세 개
// bronze 4

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2480 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    int a = Integer.parseInt(st.nextToken());
    int b = Integer.parseInt(st.nextToken());
    int c = Integer.parseInt(st.nextToken());

    // 세 수가 모두 다른 경우
    if (a != b && b != c && a != c) {
      int max;

      // a > b 일 경우
      if (a > b) {
        // c > a > b 인 경우
        if (c > a) {
          max = c;
        }

        // a > (b, c) 인 경우
        else {
          max = a;
        }
      }

      // a < b 일 경우
      else {
        // c > b > a 인 경우
        if (c > b) {
          max = c;
        }

        // b > (a, c) 인 경우
        else {
          max = b;
        }
      }
      System.out.println(max * 100);
    }

    // 두개 이상의 수가 같을 경우
    else {
      // 3개 모두 같은 경우
      if (a == b && a == c) {
        System.out.println(10000 + a * 1000);
      }

      // 2개가 같은 경우
      else {
        // a와 b 혹은 a와 c 가 같은 경우
        if (a == b || a == c) {
          System.out.println(1000 + a * 100);
        }

        // b와 c 가 같은 경우
        else {
          System.out.println(1000 + b * 100);
        }
      }
    }
  }
}
