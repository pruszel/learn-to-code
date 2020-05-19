import javax.swing.*;
import java.awt.*;

public class Paddle {
  public int x=0;
  public int y=0;

  public Paddle(int x, int y) {
    this.x = x;
    this.y = y;
  }
  
  public void draw(Graphics g) {
    g.setColor(Color.BLACK);
    g.drawRect(x, y, 30, 100);
  }
}