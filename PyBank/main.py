import os
import csv

def main():
    #find csv file path
    #code for finding file path from class 3.2 activity Stu_ReadComicBooksCSV
    csvpath = os.path.join("..","PyBank" ,"Resources", "budget_data.csv")
    print(csvpath)
    #Create list to store dates and profit/losses
    date_list = []
    profit_loss_list = []
    change_list = []
    
    #read csv
    #code for reading csv from class 3.2 activity Stu_ReadComicBooksCSV
    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        #Get header so it's not added to list elements
        csv_header = next(csvreader) 
        
        #read rows and add values to lists
        for row in csvreader:
            date_list.append(row[0])
            profit_loss_list.append(row[1])

    #Get the monthly change in profit/loss for average, greatest increase and greatest decrease
    change_list = GetMonthlyChangeList(profit_loss_list)

    total_months = GetMonths(date_list)
    total_profit = GetTotalProfit(profit_loss_list)
    average_change = GetAverageChange(change_list)
    greatest_increase = GetGreatestIncrease(date_list, change_list)
    greatest_decrease = GetGreatestDecrease(date_list, change_list)
    WriteAndPrintAnalysis(total_months,total_profit,average_change,greatest_increase,greatest_decrease)

def GetMonths(date_values):
    #loop over list and count the number of elements in it for total number of months
    date_counter = 0
    for date in date_values:
        date_counter += 1
    return date_counter

def GetTotalProfit(profit_values):
    #Add each value in profit loss list to get total profits/losses
    total = 0
    for value in range(0, len(profit_values)):
        total += int(profit_values[value])
    return total

def GetAverageChange(change_values):
    average_change = 0
    #add up the total of the change values
    for change in range(0, len(change_values)):
        average_change += int(change_values[change])
    #Get the average of the changes and round to 2 decimal places to match the output
    #Round function from class work 3.2 Stu_CensusZip
    average_change = round(average_change / len(change_values),2)
    return average_change

def GetGreatestIncrease(date_values, change_values):
    #loop over the monthly change list and return the date of the greatest change along with
    #the value of the change
    greatest_value_increase = 0
    date_of_greatest_increase = ""
    for value in range(len(change_values)):
        if int(change_values[value]) >= greatest_value_increase:
            greatest_value_increase = int(change_values[value])
            #change starts at the 2nd month in the profit/loss list so so we add 1 to
            #the date index to find the correct date
            date_of_greatest_increase = str(date_values[value+1])
    #return a list to have access to the date and value of greatest increase
    return [date_of_greatest_increase, greatest_value_increase]

def GetGreatestDecrease(date_values, change_values):
    #Copied GetGreatestIncrease function and changed >= to <=
    #loop over the monthly change list and return the date of the greatest change along with
    #the value of the change
    greatest_value_decrease = 0
    date_of_greatest_decrease = ""
    for value in range(len(change_values)):
        if int(change_values[value]) <= greatest_value_decrease:
            greatest_value_decrease = int(change_values[value])
            #change starts at the 2nd month in the profit/loss list so so we add 1 to
            #the date index to find the correct date
            date_of_greatest_decrease = str(date_values[value+1])
    #return a list to have access to the date and value of greatest increase
    return [date_of_greatest_decrease, greatest_value_decrease]

def GetMonthlyChangeList(profit_values):
    change_list = []
    for value in range(1, len(profit_values)):
        change_list.append(int(profit_values[value])-int(profit_values[value-1]))
    return change_list

def WriteAndPrintAnalysis(months,total,average,increase,decrease):
    #create list of values for output to terminal and txt file
    output_list = ["Financial Analysis",
                   "----------------------------",
                   f"Total Months: {str(months)}",
                   f"Total: {str(total)}", f"Average Change: {str(average)}", 
                   f"Greatest Increase in Profits: {str(increase[0])} (${str(increase[1])})",
                   f"Greatest Decrease in Profits: {str(decrease[0])} (${str(decrease[1])})"]
    #print statements to match output in example
    for line in output_list:
        print(str(line))

    #write results to text file
    #code from https://www.pythontutorial.net/python-basics/python-write-text-file/
    with open('Analysis.txt','w') as f:
        for line in output_list:
            f.write(line)
            #\n to output to next line
            f.write("\n")

main()