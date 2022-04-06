import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class DesafioJList1 extends JFrame implements ActionListener {

    public static void main(String[] args) { new DesafioJList1();}

    JList<String> contentList;
    JList<String> knowList;
    DefaultListModel<String> firstList;
    DefaultListModel<String> chosenList;

    public DesafioJList1(){
        super("list1:");
        //create jpanel
        Container panel = new JPanel();
        Container listPanel = new JPanel();
        Container buttons = new JPanel();
        Container conteudo = getContentPane();

        //Layout
        panel.setLayout(new FlowLayout());
        listPanel.setLayout(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.insets = new Insets(10, 15, 10, 15);
        buttons.setLayout(new GridLayout(2, 1, 1, 5));

        JLabel description = new JLabel("choose fafers", SwingConstants.CENTER);
        description.setPreferredSize(new Dimension(400, 50));

        JButton reset = new JButton("Reset");
        reset.setPreferredSize(new Dimension(100, 50));
        reset.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(e.getActionCommand().equals("Reset")){
                    loadList();
                }
            }
        });

        JButton buttonAdd = new JButton(">>");
        buttonAdd.setPreferredSize(new Dimension(100, 20));
        buttonAdd.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent f) {
                if(f.getActionCommand().equals(">>")){
                    String value = contentList.getSelectedValue();
                    System.out.println(value);

                    chosenList.addElement(value);
                    firstList.removeElement(value);
                }
            }
        });

        JButton removeButton = new JButton("<<");
        removeButton.setPreferredSize(new Dimension(100, 20));
        removeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent g) {
                if(g.getActionCommand().equals("<<")){
                    String value = knowList.getSelectedValue();
                    System.out.println(value);

                    firstList.addElement(value);
                    chosenList.removeElement(value);
                }
            }
        });

        buttons.add(buttonAdd, BorderLayout.SOUTH);
        buttons.add(removeButton, BorderLayout.NORTH);

        firstList = new DefaultListModel<>();
        chosenList = new DefaultListModel<>();

        contentList = new JList<>(firstList);
        contentList.setBackground(Color.gray);

        knowList = new JList<>(chosenList);
        knowList.setBackground(Color.green);

        loadList();

        contentList.setBounds(250, 100, 75, 75 );
        contentList.setPreferredSize(new Dimension (200,200));
        knowList.setBounds(250, 100, 75, 75);
        knowList.setPreferredSize(new Dimension (200,200));

        panel.add(description);
        listPanel.add(contentList, constraints);
        listPanel.add(buttons, constraints);
        listPanel.add(knowList, constraints);
        panel.add(listPanel);
        panel.add(reset);

        conteudo.add(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 600);
        setVisible(true);
    }

    private void loadList() {
        chosenList.removeAllElements();
        firstList.removeAllElements();
        firstList.addElement("C#");
        firstList.addElement("Python");
        firstList.addElement("Java");
        firstList.addElement("Javascript");

    }

    @Override
    public void actionPerformed(ActionEvent evento) {

    }
}
