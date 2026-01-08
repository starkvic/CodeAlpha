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
print(type(stocks_list))
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
print(f"There stocks present are{len(stocks_list)}")
stock_row = []
price_row = []
for stock,price in stocks_list.items():
    #print(f"The {stock} is valued at {price}") ##For testing the display of the stocks
    stock_row.append(str(stock))
    price_row.append(price)
print(stock_row)
print(price_row)
trading_choice = True
while trading_choice==True:
    print("try")
    break