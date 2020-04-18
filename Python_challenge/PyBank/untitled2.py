# -*- coding: utf-8 -*-

import os
import csv


PyBankcsv = os.path.join("Resources","budget_data.csv")


profit = []
monthly_changes = []
date = []
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0




with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    
    first_row = next (csvreader)
    initial_profit = int (first_row[1])
    
    count = count + 1 
    
    total_profit = total_profit + int(first_row[1])
    
    for row in csvreader:    
      count = count + 1 
      date.append(row[0])

     
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

    
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit


      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit


     
     
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
      
     
    
    average_change_profits = sum (monthly_changes)/ len (monthly_changes)
    
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str((average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as report:
    report.write("----------------------------------------------------------\n")
    report.write("  Financial Analysis"+ "\n")
    report.write("----------------------------------------------------------\n\n")
    report.write("    Total Months: " + str(count) + "\n")
    report.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    report.write("    Average Change: " + '$' + str((average_change_profits)) + "\n")
    report.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    report.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    report.write("----------------------------------------------------------\n")