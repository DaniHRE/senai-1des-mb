import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TabelaAlunos extends JFrame{

    public static void main(String[] args) {
        new TabelaAlunos();
    }

    public TabelaAlunos(){
        super("Lista de Alunos");

        Container painel = new JPanel();

        String headerTabela[] = {"ID", "Nome", "Nota", "Faltas"};

        String dadosTabela[][] = { {"1", "Luciano", "8", "0"}, {"2", "Daniel", "10", "2"}, {"3", "João", "5", "5"}};

        DefaultTableModel dTabela = new DefaultTableModel();

        dTabela.addColumn("ID");
        dTabela.addColumn("Nome");
        dTabela.addColumn("Nota");
        dTabela.addColumn("Faltas");

        dTabela.addRow(new Object[]{"1", "Luciano", "8", "0"});

        JTable tabela = new JTable(dTabela);

        JScrollPane scrollPane = new JScrollPane(tabela);

        JButton botaoAdd = new JButton("Adicionar");

        botaoAdd.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dTabela.addRow(new Object[]{"1", "Luciano", "8", "0"});
            }
        });

        painel.add(scrollPane);
        painel.add(botaoAdd);

        setVisible(true);
        setSize(500, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        Container conteudo = getContentPane();
        conteudo.add(painel);

        getContentPane();
    }

}
