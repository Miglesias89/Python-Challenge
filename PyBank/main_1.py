#Import os module
import os

#Import module for reading CSV files
import csv

csvpath=os.path.join('..','PyBank','budget_data.csv')

#Read CSV module
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    headerrow=next(csvreader,None)
   
    total_months_count=1
    firstrow=next(csvreader)
    net_total=0
    net_total=net_total+int(firstrow[1])
    previous=int(firstrow[1])
    changein_profit=0
    net_change=[]
    max_increase={"date":" ","value": 0}
    min_decrease={"date":" ","value":0}
            
    for row in csvreader:
        total_months_count=total_months_count+1 
        net_total=net_total+int(row[1])
        changein_profit=int(row[1])-previous
        previous=int(row[1])
        if len(net_change)>0 and changein_profit>max(net_change):
            max_increase["date"]=row[0]
            max_increase["value"]=changein_profit
        elif len(net_change)>0 and changein_profit<min(net_change):
            min_decrease["date"]=row[0]
            min_decrease["value"]=changein_profit
 
        net_change.append(changein_profit)

    average_netchange=sum(net_change)/len(net_change)
        
    print(f"Total Months: {total_months_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: $ {average_netchange:.2f}")
    print("Greatest Increase in Profits:",max_increase["date"] , max_increase["value"])
    print("Greatest Decrease in Profits",min_decrease["date"], min_decrease["value"])
   
   