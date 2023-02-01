from sys import argv, exit 
import os
from datetime import date
import pandas as pd

def main():
    sales_csv = get_sales_csv()
    orders_dir = create_orders_dir(sales_csv)
    process_sales_data(sales_csv, orders_dir)
    return
# Get path of sales data CSV file from the command line
def get_sales_csv():
    
 # Check whether command line parameter provided
    num_params= len(argv) -1
    if num_params >=1:
        sales_csv = argv[1]
        # Check whether provide parameter is valid path of file
        if os.path.isfile(sales_csv):
            return sales_csv
        else:
            print('Error: Invaild path to sales data csv file')
            exit(1)
    
    else:
        print('Error: Misssing CSV files path to sales data CSV files')
        exit(1)
    
   
# Create the directory to hold the individual order Excel sheets
def create_orders_dir(sales_csv):

  # Get directory in which sales data CSV file resides
  sales_dir = os.path.dirname(os.path.abspath(sales_csv))
  
  # Determine the path of the directory to hold the order data files
  todays_date = date.today().isofromat()
  orders_dir = os.path.join(sales_dir, f'Orders_{todays_date}')
  
  # Create the order directory if it does not already exist
  if not os.path.isdir(orders_dir):
      os.makedirs(orders_dir)
      
  return orders_dir

#Split the sales data into individual orders and save to Excel sheets
def process_sales_data(sales_csv):
    
# Import the sales data from the CSV file into a DataFrame
  sales_df = pd.read_csv(sales_csv)
  
# Insert a new "TOTAL PRICE" column into the DataFrame
  sales_df.insert (7, 'comment' , sales_df['ITEM QUANTITY'] * sales_df['ITEM PRICE'])
# Remove columns from the DataFrame that are not needed

# Group sales data by order ID and save to Excel sheets

    
    
    
if __name__ == '__main__':
     main()