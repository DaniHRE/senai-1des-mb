import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.security.DigestException;

public class Lista extends JFrame{

    public Lista() {
        super("Lista de Linguagens");

        Container painel = new JPanel();

        Container botoes = new JPanel();
        botoes.setLayout(new GridLayout(2,1));

        Container resetar = new JPanel();
        resetar.setLayout(new GridLayout(1,1));

        Container container = getContentPane();
        container.setLayout(new GridLayout(3,1));

        JLabel header = new JLabel("Selecione as Linguagens");

        DefaultListModel<String> listaUm = new DefaultListModel<>();
        listaUm.addElement("Primeiro");
        listaUm.addElement("Segundo");
        listaUm.addElement("Terceiro");
        JList<String> listaEsquerda = new JList<>(listaUm);
        listaEsquerda.setPreferredSize(new Dimension(200, 200));

        DefaultListModel<String> listaDois = new DefaultListModel<>();
        JList<String> listaDireita = new JList<>(listaDois);
        listaDireita.setPreferredSize(new Dimension(200, 200));

        JButton passarDireita = new JButton(">>");
        passarDireita.setSize(20,20);
        passarDireita.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Passa pra direita, acionado.");
            }
        });
        botoes.add(passarDireita);

        JButton passarEsquerda = new JButton("<<");
        passarEsquerda.setSize(20,20);
        passarEsquerda.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Passa pra esquerda, acionado");
            }
        });
        botoes.add(passarEsquerda);

        painel.add(listaEsquerda);
        painel.add(botoes);
        painel.add(listaDireita);

        JButton resetButton = new JButton("Resetar");
        resetButton.setSize(20,20);
        resetButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Botão Selecionado.");
            }
        });
        resetar.add(resetButton);

        container.add(header);
        container.add(painel);
        container.add(resetar);

        setVisible(true);
        setSize(600, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public static void main(String[] args) {
        new Lista();
    }

}
