package pkg03des;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

public class Main extends JFrame {
    
    private JButton btnCargar, btnCifrar, btnDescifrar;
    private JTextArea areaTexto;
    private File archivoSeleccionado;
    private SecretKey clave;

    public Main() {
        super("Cifrado DES con Interfaz");

        // Crear interfaz
        setLayout(new BorderLayout());

        areaTexto = new JTextArea();
        areaTexto.setLineWrap(true);
        areaTexto.setWrapStyleWord(true);
        JScrollPane scroll = new JScrollPane(areaTexto);

        JPanel panelBotones = new JPanel();
        btnCargar = new JButton("Cargar archivo");
        btnCifrar = new JButton("Cifrar");
        btnDescifrar = new JButton("Descifrar");

        panelBotones.add(btnCargar);
        panelBotones.add(btnCifrar);
        panelBotones.add(btnDescifrar);

        add(scroll, BorderLayout.CENTER);
        add(panelBotones, BorderLayout.SOUTH);

        // Eventos
        btnCargar.addActionListener(e -> cargarArchivo());
        btnCifrar.addActionListener(e -> cifrarArchivo());
        btnDescifrar.addActionListener(e -> descifrarArchivo());

        setSize(500, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void cargarArchivo() {
        JFileChooser selector = new JFileChooser();
        int resultado = selector.showOpenDialog(this);
        if (resultado == JFileChooser.APPROVE_OPTION) {
            archivoSeleccionado = selector.getSelectedFile();
            try {
                String contenido = new String(java.nio.file.Files.readAllBytes(archivoSeleccionado.toPath()));
                areaTexto.setText(contenido);
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, "Error al leer el archivo.");
            }
        }
    }

    private void cifrarArchivo() {
        if (archivoSeleccionado == null) {
            JOptionPane.showMessageDialog(this, "Primero carga un archivo.");
            return;
        }

        try {
            KeyGenerator generadorDES = KeyGenerator.getInstance("DES");
            generadorDES.init(56);
            clave = generadorDES.generateKey();

            Cipher cifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cifrador.init(Cipher.ENCRYPT_MODE, clave);

            FileInputStream entrada = new FileInputStream(archivoSeleccionado);
            FileOutputStream salida = new FileOutputStream(archivoSeleccionado.getAbsolutePath() + ".cifrado");

            byte[] buffer = new byte[1000];
            int bytesleidos;

            while ((bytesleidos = entrada.read(buffer)) != -1) {
                byte[] cifrado = cifrador.update(buffer, 0, bytesleidos);
                if (cifrado != null) salida.write(cifrado);
            }

            byte[] cifradoFinal = cifrador.doFinal();
            if (cifradoFinal != null) salida.write(cifradoFinal);

            entrada.close();
            salida.close();

            JOptionPane.showMessageDialog(this, "Archivo cifrado correctamente.");
        } catch (Exception ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error al cifrar.");
        }
    }

    private void descifrarArchivo() {
        if (archivoSeleccionado == null || clave == null) {
            JOptionPane.showMessageDialog(this, "Primero carga y cifra un archivo.");
            return;
        }

        try {
            Cipher descifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
            descifrador.init(Cipher.DECRYPT_MODE, clave);

            FileInputStream entrada = new FileInputStream(archivoSeleccionado.getAbsolutePath() + ".cifrado");
            ByteArrayOutputStream salidaBytes = new ByteArrayOutputStream();

            byte[] buffer = new byte[1000];
            int bytesleidos;

            while ((bytesleidos = entrada.read(buffer)) != -1) {
                byte[] descifrado = descifrador.update(buffer, 0, bytesleidos);
                if (descifrado != null) salidaBytes.write(descifrado);
            }

            byte[] descifradoFinal = descifrador.doFinal();
            if (descifradoFinal != null) salidaBytes.write(descifradoFinal);

            entrada.close();

            String texto = new String(salidaBytes.toByteArray());
            areaTexto.setText(texto);
            JOptionPane.showMessageDialog(this, "Texto descifrado mostrado.");
        } catch (Exception ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error al descifrar.");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Main());
    }
}
