package Sort;
import java.io.*;
import java.text.FieldPosition;
import java.text.SimpleDateFormat;
import java.util.Date;


public class readFile {
    public static void main(String[] args) throws Exception{
        fileWriter("Hello.txt");

    }
    public static void fileWriter(String filename) throws Exception{
        File file = new File(filename);
        FileWriter fw = new FileWriter(file,true);
        fw.write("I have a Dream"+'\n');
        fw.close();

    }
}