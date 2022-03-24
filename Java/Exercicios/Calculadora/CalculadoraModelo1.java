import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Objects;

public class CalculadoraModelo1 extends JFrame implements ActionListener{
    public static void main(String[] args) {
        new CalculadoraModelo1();
    }

    JTextField displayCalc;
    String valorTxt;
    ArrayList<Double> listNum;
    ArrayList<Character> listOp;
    double result;

    public CalculadoraModelo1(){

        super("Calculadora");

        listNum = new ArrayList<Double>();
        listOp = new ArrayList<Character>();

        result = 0.00;

        valorTxt = "";
        Container n = new JPanel();

        n.setLayout(new GridLayout(4,4));

        JButton btn7 = new JButton("7");
        btn7.addActionListener(this);
        n.add(btn7);

        JButton btn8 = new JButton("8");
        btn8.addActionListener(this);
        n.add(btn8);

        JButton btn9 = new JButton("9");
        btn9.addActionListener(this);
        n.add(btn9);

        JButton btnBar = new JButton("/");
        btnBar.addActionListener(this);
        n.add(btnBar);

        JButton btn4 = new JButton("4");
        btn4.addActionListener(this);
        n.add(btn4);

        JButton btn5 = new JButton("5");
        btn5.addActionListener(this);
        n.add(btn5);

        JButton btn6 = new JButton("6");
        btn6.addActionListener(this);
        n.add(btn6);

        JButton btnAster = new JButton("*");
        btnAster.addActionListener(this);
        n.add(btnAster);

        JButton btn1 = new JButton("1");
        btn1.addActionListener(this);
        n.add(btn1);

        JButton btn2 = new JButton("2");
        btn2.addActionListener(this);
        n.add(btn2);

        JButton btn3 = new JButton("3");
        btn3.addActionListener(this);
        n.add(btn3);

        JButton btnMinus = new JButton("-");
        btnMinus.addActionListener(this);
        n.add(btnMinus);

        JButton btn0 = new JButton("0");
        btn0.addActionListener(this);
        n.add(btn0);

        JButton btnDot = new JButton(".");
        btnDot.addActionListener(this);
        n.add(btnDot);

        JButton btnEqual = new JButton("=");
        btnEqual.addActionListener(this);
        n.add(btnEqual);

        JButton btnPlus = new JButton("+");
        btnPlus.addActionListener(this);
        n.add(btnPlus);

        Container c = getContentPane();

        displayCalc = new JTextField();
        displayCalc.setEditable(false);;

        c.add(BorderLayout.NORTH, displayCalc);
        c.add(BorderLayout.CENTER, n);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 300);
        setVisible(true);
    }

    public boolean testNum(String textDig){
        try {
            Double numTrue = Double.parseDouble(textDig);
            return true;
        }
        catch (NumberFormatException exception){
            return false;
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String textButton = e.getActionCommand();
        valorTxt += textButton;

        double numConv = 0.0;

        if (testNum(textButton)){
            numConv = Double.parseDouble(textButton);
            displayCalc.setText(valorTxt);
            listNum.add(numConv);
            System.out.println(listNum);
        }else{          
            listOp.add(textButton.charAt(0));
            displayCalc.setText(displayCalc.getText() + textButton);
            System.out.println(listOp);
            if(Objects.equals(textButton, "=")){
                calc();
            }
        }

    }

    public double calc(){
        double num1, num2;
        char operador;

        for (int i = 0; i < listNum.size() - 1; i++) {
            num1 = listNum.get(i);
            num2 = listNum.get(i + 1);

            operador = listOp.get(i);

            System.out.println("Volor 1" + num1 + "Valor 2" + num2 + "Operador: " + operador);
        }

        return 0.00;
    }

}
