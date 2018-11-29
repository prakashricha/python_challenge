import os
import csv

totalmonth=0.0
totalprofitloss=0
profitloss =[]
month=[]
valuechange=0
Val=[]
i=0
list=[]
totalvaluechange=0.0
bankdata = os.path.join('..','..','..','..', 'Resources', 'budget_data.csv')
with open(bankdata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  # read header
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
#       print(row)
        totalmonth += 1
# calculating total profit and loss
        totalprofitloss = float(totalprofitloss + (int(row[1])))
        month.append(row[0])
        profitloss.append(row[1])
    def changevalue(startpoint,currentpoint):
        return(float(int(currentpoint)-int(startpoint)))

#    print(f"total month : {totalmonth}")
 #   print(f"total profit and loss : {totalprofitloss}")
for eachn in profitloss:
    val = float(changevalue(profitloss[i - 1], eachn))
    Val.append(val)
    i = i + 1
Val[0]=0
#print(f"total value change :{Val}")
#calculation Average change Value
for i in range(len(Val)):
    totalvaluechange = totalvaluechange+Val[i]
Averagevaluechange=round(totalvaluechange/i,2)

# finding greatest increase and Decrease
maxval=max(Val)
minval=min(Val)
x=Val.index(maxval)
y=Val.index(minval)


#val_zip=zip(month,profitloss,Val)

#printing final output

print(f"Total Months: {totalmonth}")
print(f"Total:  {totalprofitloss}")
print(f"Average  Change: {Averagevaluechange}")
print(f"Greatest Increase in Profits: {month[x]} (${maxval})")
print(f"Greatest Decrease in Profits: {month[y]} (${minval})")

