import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;
import java.util.Scanner;

public class FileReader {
	
	public FileReader(String filename) {
		try {
			File myObj = new File(filename);
			Scanner myReader = new Scanner(myObj);
			myReader.nextLine();
			while (myReader.hasNextLine()) {
				String[] data = myReader.nextLine().split(",");
				DatabaseConnection.addFund(
						data[0], 
						data[1], 
						Double.parseDouble(data[2]), 
						Double.parseDouble(data[3]), 
						data[4], 
						Integer.parseInt(data[5]), 
						data[6], 
						Double.parseDouble(data[7]), 
						data[8], 
						data[9], 
						Double.parseDouble(data[10]), 
						Double.parseDouble(data[11]), 
						Double.parseDouble(data[12]), 
						Double.parseDouble(data[13]), 
						Double.parseDouble(data[14]), 
						Double.parseDouble(data[15]), 
						Double.parseDouble(data[16]), 
						Double.parseDouble(data[17]), 
						Double.parseDouble(data[18]),
						Double.parseDouble(data[19]), 
						Double.parseDouble(data[20]), 
						Double.parseDouble(data[21]), 
						Double.parseDouble(data[22]), 
						Double.parseDouble(data[23]), 
						Double.parseDouble(data[24]), 
						Double.parseDouble(data[25]), 
						Double.parseDouble(data[26]), 
						Integer.parseInt(data[27]), 
						Integer.parseInt(data[28]), 
						Double.parseDouble(data[29]), 
						Double.parseDouble(data[30]), 
						Double.parseDouble(data[31]), 
						Double.parseDouble(data[32]), 
						Double.parseDouble(data[33]), 
						Double.parseDouble(data[34]), 
						Double.parseDouble(data[35]), 
						0, 
						Integer.parseInt(data[37]), 
						Integer.parseInt(data[38]), 
						Boolean.parseBoolean(data[39]), 
						Boolean.parseBoolean(data[40]), 
						data[41]);
			}
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("File Reader Error!!");
			e.printStackTrace();
		}
	}
	
	public void addNewFund() {
		
	}
	
	public void updateExistingFund() {
		
	}

	public static void main(String[] args) {
//		FileReader fr = new FileReader("40-49yrFunds.csv");
//		FileReader fr = new FileReader("50-59yrFunds.csv");
		FileReader fr = new FileReader("60yrPlusFunds.csv");

	}

}
