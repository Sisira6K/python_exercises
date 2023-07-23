"""Your are given the following list containing stock symbols, their current price as well as the absolute price
change of the previous day:
stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]
As you plan to take some of the profits, write a program that creates a list of all the stock symbols with a change     
of more than +5 percent. The list should be named sell_list. The list should only contain the stock symbol, not the price 
or the absolute change. Print the resulting list."""

stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]
sell_list=[]
for number in stocks:
    previousPrice = number[-2]- number[-1]
    absolutePrice = abs(number[-1])
    changePercent =(absolutePrice/previousPrice)*100
    if changePercent > 5 :
       sell_list.append(number[-3])
print(sell_list)