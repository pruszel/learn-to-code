import javax.swing.*;
import java.awt.event.*;

// setBounds(x axis, y axis, width, height)

public class Main
{
  public static String encrypt(String text, boolean encrypt) {
    StringBuffer result = new StringBuffer();

    for (int i=0; i < text.length(); i++) {
      char c = text.charAt(i);
      int n = (int) c;
      if (encrypt) {
        n += 1;
      } else {
        n -= 1;
      }
      c = (char) n;

      result.append(c);
    }

    return result.toString();
  }

  public static void main(String[] args) {
    // creating instance of JFrame
    JFrame f = new JFrame();


    // Create text fields and buttons

    JTextField decrypt = new JTextField();
    decrypt.setBounds(80, 60, 250, 30);

    JTextField encrypt = new JTextField();
    encrypt.setBounds(80, 200, 250, 30);

    JButton b1 = new JButton("Encrypt");
    b1.setBounds(80, 100, 250, 40);

    JButton b2 = new JButton("Decrypt");
    b2.setBounds(80, 150, 250, 40);




    // Encrypt button event listener
    b1.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        String text = decrypt.getText();
        String secret = encrypt(text, true);
        encrypt.setText(secret);
      }
    });


    // Decrypt button event listener
    b2.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        String text = encrypt.getText();
        String secret = encrypt(text, false);
        decrypt.setText(secret);
      }
    });


    // add elements to JFrame
    f.add(b1);
    f.add(b2);
    f.add(encrypt);
    f.add(decrypt);
    
    f.setSize(400, 500);
    f.setLayout(null);
    // make the frame visible
    f.setVisible(true);
  }
}