import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class App {
	public static void main(String[] args) {
		String salida = "/home/angel/Documentos/Distribuidos/Proyecto/ZippingOut/Myzip.zip";
		String entrada = "/home/angel/Documentos/Distribuidos/Proyecto/comprimeme.py";
		
		byte[] buffer = new byte[1024];

    	try{

    		FileOutputStream fos = new FileOutputStream(salida);
    		ZipOutputStream zos = new ZipOutputStream(fos);
    		ZipEntry ze= new ZipEntry("comprimeme.py");
    		zos.putNextEntry(ze);
    		FileInputStream in = new FileInputStream(entrada);

    		int len;
    		while ((len = in.read(buffer)) > 0) {
    			zos.write(buffer, 0, len);
    		}

    		in.close();
    		zos.closeEntry();

    		//remember close it
    		zos.close();

    		System.out.println("Done");

    	}catch(IOException ex){
    	   ex.printStackTrace();
    	}
    }
	
}
