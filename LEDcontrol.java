import java.util.Scanner;
import java.io.PrintWriter;
import java.io.File;

public class LEDcontrol {
    public static void main( String[] args ) {
        Scanner reader = new Scanner(System.in);  // Reading from System.in
        String LEDmode = new String("BLACK");

        System.out.println( "1 = RED" );
        System.out.println( "2 = BLUE" );
        System.out.println( "3 = GREEN" );
        System.out.println( "4 = WHITE" );
        System.out.println( "5 = FLASHRED" );
        System.out.println( "6 = FLASHBLUE" );
        System.out.println( "7 = FLASHGREEN" );
        System.out.println( "8 = FLASHWHITE" );
        System.out.println( "9 = BLACK" );
        System.out.println( "0 = Exit Program" );

        System.out.println("Enter a number: ");
        int option = reader.nextInt(); // Scans the next token of the input as an int.
        switch (option) {
            case 1:  LEDmode = "RED";
                     break;
            case 2:  LEDmode = "BLUE";
                     break;
            case 3:  LEDmode = "GREEN";
                     break;
            case 4:  LEDmode = "WHITE";
                     break;
            case 5:  LEDmode = "FLASHRED";
                     break;
            case 6:  LEDmode = "FLASHBLUE";
                     break;
            case 7:  LEDmode = "FLASHGREEN";
                     break;
            case 8:  LEDmode = "FLASHWHITE";
                     break;
            case 9:  LEDmode = "BLACK";
                     break;
            case 0:  LEDmode = "BLACK";
                     reader.close();
                     System.exit( 0 );
                     break;
            default: LEDmode = "BLACK";
                     break;
        }
        System.out.println("LEDmode = '" + LEDmode + "'");

//        PrintWriter pw = null;
//        try {
//             File file = new File("LEDstrip.txt");
////             FileWriter fw = new FileWriter(file, true);
//             FileWriter fw = new FileWriter(file, false);
//             pw = new PrintWriter(fw);
//             pw.print(LEDmode);
//        } catch (IOException e) {
//             e.printStackTrace();
//        } finally {
//             if (pw != null) {
//                 pw.close();
//             }
 //       }

//         File fileLocation = new File("./LEDstrip.txt");
//         File file = new File("LEDstrip.txt");
 //        fileLocation.getParentFile().mkdirs();
//         PrintWriter outFile = new PrintWriter(file);
//         PrintWriter outFile = new PrintWriter("LEDstrip.txt");
//         BufferedWriter outFile = null;
//         outFile = new BufferedWriter( new FileWriter("LEDstrip.txt"));
//         outFile.print(LEDmode);
//         outFile.close();
    }
}
