import javax.swing.*;
import java.awt.*;

public class Ball implements Runnable {
  int x=0;
  int y=0;
  int dx=1;
  int dy=0;
  int width = 15;
  int height = 15;

  public Ball(int x, int y) {
    this.x = x;
    this.y = y;
  }
  
  public void draw(Graphics g) {
    g.setColor(Color.BLACK);
    g.fillOval(x, y, 50, 50);
  }
  
  public void run() {
    try {
      while(true) {
        x = x + dx;
        y = y + dy;
        //System.out.println("Ball x: "+x+" y: "+y);
        Thread.sleep(20);
      }
    } catch(Exception e) {

    }
  }
}
