package pkg03des;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.crypto.*;
import java.security.*;
import java.util.Base64;

public class Main extends JFrame {

    private JButton btnCargar, btnCifrar, btnDescifrar;
    private JTextArea areaTexto;
    private File archivoSeleccionado;
    private SecretKey clave;

    public Main() {
        super("Cifrado y Descifrado DES");

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

        // Eventos de los botones
        btnCargar.addActionListener(e -> cargarArchivo());
        btnCifrar.addActionListener(e -> cifrarArchivo());
        btnDescifrar.addActionListener(e -> descifrarArchivo());

        // Configurar la ventana
        setSize(600, 500);
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
                areaTexto.setText(contenido); // Mostrar contenido del archivo en el JTextArea
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
            // Generar una clave DES
            KeyGenerator generadorDES = KeyGenerator.getInstance("DES");
            generadorDES.init(56);
            clave = generadorDES.generateKey();

            // Crear un cifrador con DES en modo ECB y PKCS5Padding
            Cipher cifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cifrador.init(Cipher.ENCRYPT_MODE, clave);

            FileInputStream entrada = new FileInputStream(archivoSeleccionado);
            ByteArrayOutputStream salida = new ByteArrayOutputStream();

            byte[] buffer = new byte[1024];
            int bytesleidos;

            while ((bytesleidos = entrada.read(buffer)) != -1) {
                byte[] cifrado = cifrador.update(buffer, 0, bytesleidos);
                if (cifrado != null) salida.write(cifrado);
            }

            byte[] cifradoFinal = cifrador.doFinal();
            if (cifradoFinal != null) salida.write(cifradoFinal);

            entrada.close();

            // Convertir los datos cifrados a Base64 para mostrar
            byte[] textoCifrado = salida.toByteArray();
            String textoCifradoBase64 = Base64.getEncoder().encodeToString(textoCifrado);
            areaTexto.setText(textoCifradoBase64); // Mostrar texto cifrado

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
            // Convertir el texto cifrado de Base64 a bytes
            byte[] bytesCifrados = Base64.getDecoder().decode(areaTexto.getText());

            // Crear un descifrador con DES en modo ECB y PKCS5Padding
            Cipher descifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
            descifrador.init(Cipher.DECRYPT_MODE, clave);

            ByteArrayInputStream entrada = new ByteArrayInputStream(bytesCifrados);
            ByteArrayOutputStream salidaBytes = new ByteArrayOutputStream();

            byte[] buffer = new byte[1024];
            int bytesleidos;

            while ((bytesleidos = entrada.read(buffer)) != -1) {
                byte[] descifrado = descifrador.update(buffer, 0, bytesleidos);
                if (descifrado != null) salidaBytes.write(descifrado);
            }

            byte[] descifradoFinal = descifrador.doFinal();
            if (descifradoFinal != null) salidaBytes.write(descifradoFinal);

            entrada.close();

            // Mostrar el texto descifrado en el JTextArea
            String textoDescifrado = new String(salidaBytes.toByteArray());
            areaTexto.setText(textoDescifrado); // Mostrar texto descifrado
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
