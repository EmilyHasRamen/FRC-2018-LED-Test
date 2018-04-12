import java.util.Scanner;
import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;

import java.text.*;  // for SimpleDateFormat()

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
        System.out.println( "10 = RAINBOW" );
        System.out.println( "11 = RAINBOWCYCLE" );
        System.out.println( "12 = RAINBOWTHEATERCHASE" );
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
            case 10: LEDmode = "RAINBOW";
                     break;
            case 11: LEDmode = "RAINBOWCYCLE";
                     break;
            case 12: LEDmode = "RAINBOWTHEATERCHASE";
                     break;
            default: LEDmode = "BLACK";
                     break;
        }
        System.out.println("LEDmode = '" + LEDmode + "'");


        BufferedWriter writer = null;
        try {
            //create a temporary file
//            String timeLog = new SimpleDateFormat("yyyyMMdd_HHmmss").format(Calendar.getInstance().getTime());
            String timeLog = "LEDstrip.txt";
            File logFile = new File(timeLog);

            // This will output the full path where the file will be written to...
            System.out.println(logFile.getCanonicalPath());

            writer = new BufferedWriter(new FileWriter(logFile));
            writer.write(LEDmode);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                // Close the writer regardless of what happens...
                writer.close();
            } catch (Exception e) {
            }
        }
        // writer = new BufferedWriter(new FileWriter(logFile, true));  // to append the text to the file 

    }
}
