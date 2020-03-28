#Import os module
import os

#Import system module
import sys 

#Import module for reading CSV files
import csv

csvpath=os.path.join('..','PyBank','budget_data.csv')

#Read CSV module
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
    #Read the header row first
    headerrow=next(csvreader,None)
   
    #Set variables and take into account first row (Jan 2010)
    total_months_count=1
    firstrow=next(csvreader)
    net_total=0
    net_total=net_total+int(firstrow[1])
    previous=int(firstrow[1])
    changein_profit=0
    net_change=[] 
    max_increase={"date":firstrow[0],"value": 0}
    min_decrease={"date":firstrow[0],"value":0}
            
    for row in csvreader:
        total_months_count=total_months_count+1 
        net_total=net_total+int(row[1])
        changein_profit=int(row[1])-previous 
        previous=int(row[1])
        
        #Min/Max if statement for change in profit
        if len(net_change)>0 and changein_profit>max(net_change):
            max_increase["date"]=row[0]
            max_increase["value"]=changein_profit
        elif len(net_change)>0 and changein_profit<min(net_change):
            min_decrease["date"]=row[0]
            min_decrease["value"]=changein_profit
 
        net_change.append(changein_profit)

    #Average of net change calculation
    average_netchange=sum(net_change)/len(net_change)

    
    #Print out Financial summary results
    print(f"Total Months: {total_months_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: $ {average_netchange:.2f}")
    print("Greatest Increase in Profits:",max_increase["date"] , "$", max_increase["value"])
    print("Greatest Decrease in Profits",min_decrease["date"], "$", min_decrease["value"])
   
    #Set variable for text file
    text_file=os.path.join("budget_final.txt")

    #Open text file
    sys.stdout=open(text_file,"w")

    #Output financial summary 
    print(f"Total Months: {total_months_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: $ {average_netchange:.2f}")
    print("Greatest Increase in Profits:",max_increase["date"] , max_increase["value"])
    print("Greatest Decrease in Profits",min_decrease["date"], min_decrease["value"])
   
    sys.stdout.close()