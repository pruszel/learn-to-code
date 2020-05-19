import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Main extends JFrame implements KeyListener
{
  static int width = 600;
  static int height = 500;

  static Ball ball = new Ball(width/2, height/2);
  static Paddle p1 = new Paddle(0, (height/2)-50);
  static Paddle p2 = new Paddle(width-30, (height/2)-50);

  @Override
  public void paint(Graphics g) {
    super.paint(g);
    // g.clearRect(0,0,width, height);

    ball.draw(g);
    p1.draw(g);
    p2.draw(g);

    // draw(g);
  }
  public void draw(Graphics g) {
		// repaint();
	}

  public Main() {
		this.setTitle("Pong");
		this.setSize(width, height);
		this.setResizable(false);
		this.setVisible(true);
  }

  public static void main(String[] args) {
    Main game = new Main();

    Thread b = new Thread(ball);
    b.start();

    try {
      while(true) {
        game.repaint();
        Thread.sleep(50);
      }
    } catch(Exception e) {

    }
  }

  @Override
  public void keyTyped(KeyEvent e) {

      if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
          System.out.println("Right key typed");
      }
      if (e.getKeyCode() == KeyEvent.VK_LEFT) {
          System.out.println("Left key typed");
      }
  }
  @Override
  public void keyReleased(KeyEvent e) {
      if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
          System.out.println("Right key Released");
      }
      if (e.getKeyCode() == KeyEvent.VK_LEFT) {
          System.out.println("Left key Released");
      }
  }
  @Override
  public void keyPressed(KeyEvent e) {
      if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
          System.out.println("Right key pressed");
      }
      if (e.getKeyCode() == KeyEvent.VK_LEFT) {
          System.out.println("Left key pressed");
      }
  }

}
