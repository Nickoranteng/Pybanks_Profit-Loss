    # %%
    # import the os and CSV file reading module
import os
import csv
    
    # location of files to be analysed and the Destination to write output
Source_csvpath = os.path.join("Resources", "budget_data.csv")
Dest_csvpath = os.path.join("Analysis", "budget_analysis.txt")
   
    #  Improved Reading using CSV module
with open(Source_csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first. Read each row of data after the header
  
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Declare your variables for the various parameters to analyse
    
    changelist = []   
    Totalprofit= 0
    count  = 0 
    firstRow = next(csvreader)
    count += 1
    Totalprofit += int(firstRow[1])
    previousPL = int(firstRow[1]) 
    greatest_Increase = ["",0]
    greatest_Decrease = ["",9999999999999999999]
    for row in csvreader:
        print(row)
        count += 1
        Totalprofit +=  int(row[1])
        change = int(row[1])-previousPL
        previousPL = int(row[1])
        changelist += [change]
    # calculate the greatest increae in profits    
        if change > greatest_Increase[1]:
            greatest_Increase[0] = row[0]
            greatest_Increase[1] = change
    # calculate the greatest decrease in profits
        if change < greatest_Decrease[1]:
            greatest_Decrease[0] = row[0]
            greatest_Decrease[1] = change
        
    # calculate  Average change in profit/losses over entire period using function
monthlyaverage = sum(changelist)/len(changelist)
    # calculate the greatest increase

 
    # Results
results=(        
    f"Financial Analysis\n" 
    f"------------------\n"     
    f"Total Months: {count}\n"
    f"Total: {Totalprofit}\n"
    f"Average Change: {monthlyaverage:.2f}\n"
    f"Greatest Increase in Profits: {greatest_Increase[0]} (${greatest_Increase[1]})\n"  
    f"Greatest Decrease in Profits: {greatest_Decrease[0]} (${greatest_Decrease[1]})\n")
   

print(results)
       
with open(Dest_csvpath, "w") as Py_Bank_file:
    Py_Bank_file.write(str(results)) 
 
