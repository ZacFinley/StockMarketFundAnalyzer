import java.sql.*;

public class DatabaseConnection{  
	static String url = "jdbc:mysql://localhost:3306/USA_Funds?serverTimezone=UTC";
	static String username = "root";
	static String password = "police7000122";
	
//	public static int getRecipeId(String recipeName) {
//		int resultId = -1;
//		try {
//			Connection connection = DriverManager.getConnection(url, username, password);
//			String sql = "SELECT recipe_id FROM recipes WHERE recipe_name = '" + recipeName + "'";
//			Statement statement = connection.createStatement();
//			ResultSet result = statement.executeQuery(sql);
//			while (result.next()) {
//				String id = result.getString(1);
//				resultId = Integer.parseInt(id);
//			}
//			
//			connection.close();
//		} catch (SQLException e) {
//			System.out.println("Oops, error!");
//			e.printStackTrace();
//		}
//		return resultId;
//	};
	
	public static void addFund(String ticker, String name, double price, double expenceRatio, String category,
			int morningStar, String netAssets, double holdingsTurnover, String inceptionDate, String fundFamily, double portCompCash,
			double portCompStocks, double portCompBonds, double portCompOthers, double portCompPreferred, double portCompConvertable,
			double secWeightBasicMat, double secWeightConCyc, double secWeightFinSer, double secWeightRealestate, double secWeightConDef,
			double secWeightHealth, double secWeightUtil, double secWeightComSer, double secWeightEnergy, double secWeightIndus,
			double secWeightTech, int numYrsUp, int numYrsDown, double ytd, double oneMon, double threeMon, double oneYr,
			double threeYr, double fiveYr, double tenYr, double inception, int initInv, int subInv, boolean isMutualFund, boolean isEtf, String captureDate) {
		try {
			Connection connection = DriverManager.getConnection(url, username, password);
			String sql = "INSERT INTO funds VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
			PreparedStatement statement = connection.prepareStatement(sql);
			statement.setString(1, ticker);
			statement.setString(2, name);
			statement.setDouble(3, price);
			statement.setDouble(4, expenceRatio);
			statement.setString(5, category);
			statement.setInt(6, morningStar);
			statement.setString(7, netAssets);
			statement.setDouble(8, holdingsTurnover);
			// Fix this with date
			statement.setString(9, inceptionDate);
			statement.setString(10, fundFamily);
			statement.setDouble(11, portCompCash);
			statement.setDouble(12, portCompStocks);
			statement.setDouble(13, portCompBonds);
			statement.setDouble(14, portCompOthers);
			statement.setDouble(15, portCompPreferred);
			statement.setDouble(16, portCompConvertable);
			statement.setDouble(17, secWeightBasicMat);
			statement.setDouble(18, secWeightConCyc);
			statement.setDouble(19, secWeightFinSer);
			statement.setDouble(20, secWeightRealestate);
			statement.setDouble(21, secWeightConDef);
			statement.setDouble(22, secWeightHealth);
			statement.setDouble(23, secWeightUtil);
			statement.setDouble(24, secWeightComSer);
			statement.setDouble(25, secWeightEnergy);
			statement.setDouble(26, secWeightIndus);
			statement.setDouble(27, secWeightTech);
			statement.setInt(28, numYrsUp);
			statement.setInt(29, numYrsDown);
			statement.setDouble(30, ytd);
			statement.setDouble(31, oneMon);
			statement.setDouble(32, threeMon);
			statement.setDouble(33, oneYr);
			statement.setDouble(34, threeYr);
			statement.setDouble(35, fiveYr);
			statement.setDouble(36, tenYr);
			statement.setDouble(37, inception);
			statement.setInt(38, initInv);
			statement.setInt(39, subInv);
			statement.setBoolean(40, isMutualFund);
			statement.setBoolean(41, isEtf);
			// Fix this with date
			statement.setString(42, captureDate);
			statement.executeUpdate();
			statement.close();
			connection.close();
		} catch (SQLException e) {
			System.out.println("Oops, error!");
			e.printStackTrace();
		}
	};
	
//	public static void deleteRecipe(int recipeId) {
//		try {
//			Connection connection = DriverManager.getConnection(url, username, password);
//			String sql = "DELETE FROM recipes WHERE recipe_id = ?";
//			PreparedStatement statement = connection.prepareStatement(sql);
//			statement.setInt(1, recipeId);
//			statement.executeUpdate();
//			statement.close();
//			connection.close();
//		} catch (SQLException e) {
//			System.out.println("Oops, error!");
//			e.printStackTrace();
//		}
//	};
	
//	public static void addIngredient(int recipeId, String measurementQty, int measurementUnitId, String ingredientName) {
//		try {
//			Connection connection = DriverManager.getConnection(url, username, password);
//			String sql = "INSERT INTO recipe_ingredients (recipe_id, measurement_qty, measurement_unit_id, ingredient_name) VALUES (?, ?, ?, ?)";
//			PreparedStatement statement = connection.prepareStatement(sql);
//			statement.setInt(1, recipeId);
//			statement.setString(2, measurementQty);
//			statement.setInt(3, measurementUnitId);
//			statement.setString(4, ingredientName);
//			statement.executeUpdate();
//			statement.close();
//			connection.close();
//		} catch (SQLException e) {
//			System.out.println("Oops, error!");
//			e.printStackTrace();
//		}
//	};

	public static void main(String args[]){  
		DatabaseConnection dbConnect = new DatabaseConnection();
		dbConnect.addFund("CHCLX",
				"AB Discovery Growth Fund Class A",
				14.54,
				96.00,
				"Mid-Cap Growth",
				4,
				"2.92B",
				80.00,
				"1938-07-06",
				"AllianceBernstein",
				1.32,
				98.63,
				0.00,
				0.05,
				0.00,
				0.00,
				1.15,
				11.38,
				5.97,
				0.75,
				5.85,
				26.54,
				0.02,
				0.03,
				0.00,
				14.76,
				33.53,
				57,24,
				26.65,
				1.43,
				5.57,
				36.99,
				18.78,
				16.73,
				15.26,
				0,
				2500,
				50,
				true,
				false,
				"2020-11-13");
//		DatabaseConnection.getRecipeId("CHCLX");


	}  
}  