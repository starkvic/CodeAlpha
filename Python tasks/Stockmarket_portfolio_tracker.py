import os
stocks_list = {
    "AAPL": 260.33,   # Apple
    "MSFT": 483.47,   # Microsoft
    "GOOGL": 321.98,  # Alphabet
    "AMZN": 241.56,   # Amazon
    "TSLA": 431.41,   # Tesla
    "META": 515.20,   # Meta Platforms
    "NVDA": 650.75,   # NVIDIA
    "NFLX": 610.40,   # Netflix
    "AMD": 185.30,    # AMD
    "INTC": 52.80,    # Intel
    "ORCL": 128.90,   # Oracle
    "IBM": 195.60,    # IBM
    "JPM": 178.45,    # JPMorgan Chase
    "V": 290.10,      # Visa
    "WMT": 168.25,    # Walmart
    "DIS": 112.40,    # Disney
    "BA": 225.60,     # Boeing
    "KO": 61.85,      # Coca-Cola
    "PEP": 170.20,    # PepsiCo
    "NKE": 104.75     # Nike
}
#print(type(stocks_list)) Displays the type of container storing the stocks
"""
file_path = "stocks.txt" #This is the storage of the file that is used to store the list of stocks
with open(file_path,'r') as data:
#the with statement allows the execution and assigning of variables in a special way
#print(type(stocks)) #confirming that the type is dictionary
    line = data.readlines()
    print(len(line))
    print(line)
"""
print("Welcome to the text based Stock Market Exchange TBSME")
print(f"There stocks present are {len(stocks_list)}")
stock_row = []
price_row = []
for stock,price in stocks_list.items():
    #print(f"The {stock} is valued at {price}") ##For testing the display of the stocks
    stock_row.append(str(stock))
    price_row.append(price)

for i in range(0,len(stocks_list),4):
    print(stock_row[i],":",price_row[i],"    ",stock_row[i+1],":",price_row[i+1],"    ",stock_row[i+2],":",price_row[i+2],"    ",stock_row[i+3],":",price_row[i+3])
trading_choice = True
while trading_choice==True:
    user_select = input("First time user?Y/N - ")
    current_user = ""
    if(user_select.lower()=="y"):
        new_user = input("Kindly Enter your first name")
        current_user = new_user
    else:
        files = os.listdir(".")
        extension =".txt"
        users = [file for file in files if extension in file]
        print("Welcome back. Kindly select your account from the list of the below:")
        for user in users:
            print(user[0:-4])
        current_user = input("My name is - ")
    #_=os.system("cls") #can be used to clear the screen if it is too cluttered.
    if(user_select=="n"):
        print("Here are the list of your stocks")
        with open(f"{current_user}.txt","r+") as current_file:
            current_stocks = current_file.readlines()
            #print(current_file) to display the selected file and mode
        
        #displaying current stocks
        #print(current_stocks) #shows the structure of the list holding the users stocks
        mystock_row = current_stocks[0].split(",")
        myqty_row = current_stocks[1].split(",")
        #removing trailing new line marker
        mystock_row[len(mystock_row)-1] = mystock_row[len(mystock_row)-1][0:-1]
        myqty_row[len(myqty_row)-1] = myqty_row[len(myqty_row)-1][0:-1]
        total_investment = 0
        for i in range(len(mystock_row)):
            print(f"{i+1}.{mystock_row[i]}:{myqty_row[i]}")
            total_investment += int(stocks_list[mystock_row[i]])*int(myqty_row[i])
        print(f"Your total investment is {total_investment}$")
        new_stock = input("Add a new stock? Y/N")
        while new_stock.lower()=="y":
            stock_name = input("Stock name:")
            stock_qty = input("Quantity:")
            mystock_row.append(stock_name)
            myqty_row.append(stock_qty)
            new_stock = input("Add a new stock? Y/N")
        print("Thank you for trading...\nYour current balance is")
        for i in range(len(mystock_row)):
            print(f"{i+1}.{mystock_row[i]}:{myqty_row[i]}")
            total_investment += int(stocks_list[mystock_row[i]])*int(myqty_row[i])
        print(f"Your total investment is {total_investment}$")
        mystock_row[len(mystock_row)-1] = str(mystock_row[len(mystock_row)-1])+"\n"
        myqty_row[len(myqty_row)-1] = str(myqty_row[len(myqty_row)-1])+"\n"
        #print(mystock_row) #Printing the output string
        #print(myqty_row) #Printing the output string
        with open(f"{current_user}.txt","w") as current_file:    
            current_file.write(",".join(mystock_row))
            current_file.write(",".join(myqty_row))



        """
        name_stock = current_stocks[0].split(",")
        qty_stock = current_stocks[1].split(",") 
        for i in range(len(name_stock)):
            print(f"{name_stock[i]}:    {qty_stock[i]}") """
    else:
        current_file = open(f"{current_user}.txts","a+")
        
    
    break