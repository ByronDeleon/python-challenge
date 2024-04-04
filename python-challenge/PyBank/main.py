#Great thanks to my tech friends who patiently took the time to help me through his challenge amd pffer tips and tricks
# with internet resources such as w3 schools and stack overflow and for taking time to, as I am sure was painful, dragging me through this)
#it works but I am exhausted!!


import os
import csv

# Set up the lists and variablews
date =[]
months =[]
profit = []
changes = []
count = 0
initial_profit = 0
total_profit = 0
total_change_profits = 0
average_net_change = 0

# Set csv file path 
budget_csv = os.path.join("Resources","budget_data.csv")
output_txt_file = os.path.join("Analysis","Financial_Analysis.txt")

# Read csv file 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read csv
    cvsreader = next(csvfile)
    for row in csvreader:    
      month = row[0]
      
      # Creat the variables 
      date.append(row[0])
      months.append(month)
      values =int(row[1])

      # Calculate the profits 
      profit.append(values)
      total_profit = total_profit + int(row[1])

      # Discover monthly profit changes and averages
      count =len(months)
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit
      
      # Read the data 
      changes.append(monthly_change_profits)
      net_total = sum(profit) 
      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit
      net_total_months =len(months) - 1
      budget_change =[]  

      # Do the math on change
    for i in range(len(profit) - 1):
      
      budget_change.append((profit[i + 1]) - (profit[i]))
      new_net_total = sum(budget_change)

    # Changes in the average profits
    average_net_change = new_net_total/net_total_months
    
    #Greatest Increase /Decrease in profits ( min & max)
    greatest_increase_profits = max(changes)
    greatest_decrease_profits = min(changes)

    increase_date = date[changes.index(greatest_increase_profits)]
    decrease_date = date[changes.index(greatest_decrease_profits)]
    
#Print the output to terminal
output=f"""
  ----------------------------------------------------------
  Financial Analysis
  ----------------------------------------------------------

   Total Months: {str(count)}
  Total Profits: ${str(total_profit)}
  Average Change: ${round(average_net_change, 2)}
  Greatest Increase in Profits: {str(increase_date)}, ${str(greatest_increase_profits)}
  Greatest Decrease in Profits: {str(decrease_date)}, ${str(greatest_decrease_profits)}
 
  
    ----------------------------------------------------------
  """
print(output)

# Open/Print to "Financial_analysis.txt"  file to Analysis folder
with open(output_txt_file, "w") as output_txt:
 output_txt.write(output)
  
