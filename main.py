import time,sys,os
from dataclasses import dataclass

@dataclass
class Stock:
  TSLA: int
  TSLA_shares: int
  TSLA_before: int
  AMZN: int
  AMZN_shares: int
  AMZN_before: int
  NKE: int
  NKE_shares: int
  NKE_before: int
  MSFT: int
  MSFT_shares: int
  MSFT_before: int
  NFLX: int
  NFLX_shares: int
  NFLX_before: int
  AAPL: int
  AAPL_shares: int
  AAPL_before: int
  total_money: int
  day: int
  choice_of_stock_or_end: str
  switch: str
  good_event_or_bad: bool
#^^^^^dataclass for stocks

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
    
def typingPrin(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.09)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0)
  value = input() 
  return value  

def clearScreen():
  os.system("clear")

import random
def random_stock():
  Stock.TSLA = random.randint(800, 1000)
  Stock.MSFT = random.randint(240, 350)
  Stock.NFLX = random.randint(160, 625)
  Stock.AAPL = random.randint(100, 210)
  Stock.AMZN = random.randint(120, 280)
  Stock.NKE = random.randint(100, 190)
  
#^^^^^^^^^^random number generator for stocks

def assign_arrows():
  if Stock.day != 1:
    Stock.TSLA_before = Stock.TSLA
    Stock.MSFT_before = Stock.MSFT
    Stock.NFLX_before = Stock.NFLX
    Stock.AAPL_before = Stock.AAPL
    Stock.AMZN_before = Stock.AMZN
    Stock.NKE_before = Stock.NKE
  
def random_bad_events():
  if Stock.day != 1:
    bad_events = random.randint(0, 3)
    if bad_events == 0:
      return "Will Smith rocks Chris Rock, certain stocks decrease in value."
    elif bad_events == 1:
      return "Kanye West wins presidency, certain stocks decrease in value."
    elif bad_events == 2:
      return "A billionaire sells all their stocks and live in nature, certain stocks decrease in value."
    elif bad_events == 3:
      return "Competitor company stocks increase, certain stocks decrease in value."
  else:
    return ""
#^^^^^^^^^^^^assigns a number to every bad event that can potentially happend and make it print randomly
  
def random_good_events():
  if Stock.day != 1:
    good_events = random.randint(0, 3)
    if good_events == 0:
      return "The hole in the ozone layer expands 2%, certain stocks increase in value."
    elif good_events == 1:
      return "Three nations declare war over lithium, certain stocks increase in value."
    elif good_events == 2:
      return "Competitor company stocks decrease, certain stocks increase in value."
    elif good_events == 3:
      return "It is holiday season, certain stocks increase in value."
  else:
    return ""
#^^^^^^^^^^^^assigns a number to every good event that can potentially happend and make it print randomly
  
def explain_stock():
  typingPrint("Follow the directions of the program as they are loaded.\nStarting Day 1 you will have $10000.\n")
  time.sleep(1)
#^^^^^^^^^^explains each stock individually

def up_or_down(joe10): 
  if Stock.day != 1:
    if Stock.TSLA == joe10:
      if Stock.TSLA > Stock.TSLA_before:
        return "↑"
      elif Stock.TSLA < Stock.TSLA_before:
        return "↓"
      elif Stock.TSLA == Stock.TSLA_before:
        return "-"
    if Stock.MSFT == joe10:
      if Stock.MSFT > Stock.MSFT_before:
        return "↑"
      elif Stock.MSFT < Stock.MSFT_before:
        return "↓"
      elif Stock.MSFT == Stock.MSFT_before:
        return "-"
    if Stock.NFLX == joe10:
      if Stock.NFLX > Stock.NFLX_before:
        return "↑"
      elif Stock.NFLX < Stock.NFLX_before:
        return "↓"
      elif Stock.NFLX == Stock.NFLX_before:
        return "-"
    if Stock.AAPL == joe10:
      if Stock.AAPL > Stock.AAPL_before:
        
        return "↑"
      elif Stock.AAPL < Stock.AAPL_before:
        return "↓"
      elif Stock.AAPL == Stock.AAPL_before:
        return "-"
    if Stock.AMZN == joe10:
      if Stock.AMZN > Stock.AMZN_before:
        return "↑"
      elif Stock.AMZN < Stock.AMZN_before:
        return "↓"
      elif Stock.AMZN == Stock.AMZN_before:
        return "-"
    if Stock.NKE == joe10:
      if Stock.NKE > Stock.NKE_before:
        return "↑"
      elif Stock.NKE < Stock.NKE_before:
        return "↓"
      elif Stock.NKE == Stock.NKE_before:
        return "-"
  else:
    return ""
  
def affected(joe10):
  if Stock.day != 1:
    if Stock.TSLA == joe10:
      if Stock.good_event_or_bad == True:
        if Stock.TSLA > Stock.TSLA_before:
          return "Affected"
        elif Stock.TSLA < Stock.TSLA_before:
          return "Unaffected"
        elif Stock.TSLA == Stock.TSLA_before:
          return "Neutral"
      else:
        if Stock.TSLA < Stock.TSLA_before:
          return "Affected"
        elif Stock.TSLA > Stock.TSLA_before:
          return "Unaffected"
        elif Stock.TSLA == Stock.TSLA_before:
          return "Neutral"
    if Stock.MSFT == joe10:
      if Stock.good_event_or_bad == True:
        if Stock.MSFT > Stock.MSFT_before:
          return "Affected"
        elif Stock.MSFT < Stock.MSFT_before:
          return "Unaffected"
        elif Stock.MSFT == Stock.MSFT_before:
          return "Neutral"
      else:
        if Stock.MSFT < Stock.MSFT_before:
          return "Affected"
        elif Stock.MSFT > Stock.MSFT_before:
          return "Unaffected"
        elif Stock.MSFT == Stock.MSFT_before:
          return "Neutral"
    if Stock.NFLX == joe10:
      if Stock.good_event_or_bad == True:
        if Stock.NFLX > Stock.NFLX_before:
          return "Affected"
        elif Stock.NFLX < Stock.NFLX_before:
          return "Unaffected"
        elif Stock.NFLX == Stock.NFLX_before:
          return "Neutral"
      else:
        if Stock.NFLX < Stock.NFLX_before:
          return "Affected"
        elif Stock.NFLX > Stock.NFLX_before:
          return "Unaffected"
        elif Stock.NFLX == Stock.NFLX_before:
          return "Neutral"
    if Stock.AAPL == joe10:
      if Stock.good_event_or_bad == True:
        if Stock.AAPL > Stock.AAPL_before:        
          return "Affected"
        elif Stock.AAPL < Stock.AAPL_before:
          return "Unaffected"
        elif Stock.AAPL == Stock.AAPL_before:
          return "Neutral"
      else:
        if Stock.AAPL < Stock.AAPL_before:        
          return "Affected"
        elif Stock.AAPL > Stock.AAPL_before:
          return "Unaffected"
        elif Stock.AAPL == Stock.AAPL_before:
          return "Neutral"
    if Stock.AMZN == joe10:
      if Stock.good_event_or_bad == True:
        if Stock.AMZN > Stock.AMZN_before:
          return "Affected"
        elif Stock.AMZN < Stock.AMZN_before:
          return "Unaffected"
        elif Stock.AMZN == Stock.AMZN_before:
          return "Neutral"
      else:
        if Stock.AMZN < Stock.AMZN_before:
          return "Affected"
        elif Stock.AMZN > Stock.AMZN_before:
          return "Unaffected"
        elif Stock.AMZN == Stock.AMZN_before:
          return "Neutral"
    if Stock.NKE == joe10:
      if Stock.good_event_or_bad == True:
        if Stock.NKE > Stock.NKE_before:
          return "Affected"
        elif Stock.NKE < Stock.NKE_before:
          return "Unaffected"
        elif Stock.NKE == Stock.NKE_before:
          return "Neutral"
      else:
        if Stock.NKE < Stock.NKE_before:
          return "Affected"
        elif Stock.NKE > Stock.NKE_before:
          return "Unaffected"
        elif Stock.NKE == Stock.NKE_before:
          return "Neutral"
  else:
    return "Neutral"

def good_or_bad():
  goodbad = random.randint(0,1)
  if goodbad == 0:
    Stock.good_event_or_bad = True
    return random_good_events()
  elif goodbad == 1:
    Stock.good_event_or_bad = False
    return random_bad_events()
    
def display_day():
  print(f'''
{good_or_bad()}
        
This is your current stocks and how the news affected it. 
TSLA: {Stock.TSLA_shares}, {affected(Stock.TSLA)}
MSFT: {Stock.MSFT_shares}, {affected(Stock.MSFT)}
NFLX: {Stock.NFLX_shares}, {affected(Stock.NFLX)}
AAPL: {Stock.AAPL_shares}, {affected(Stock.AAPL)}
AMZN: {Stock.AMZN_shares}, {affected(Stock.AMZN)}
NKE:  {Stock.NKE_shares}, {affected(Stock.NKE)}
        
TSLA(Tesla): ${Stock.TSLA} {up_or_down(Stock.TSLA)}
MSFT(Microsoft): ${Stock.MSFT} {up_or_down(Stock.MSFT)}
NFLX(Netflix): ${Stock.NFLX} {up_or_down(Stock.NFLX)}
AAPL(Apple): ${Stock.AAPL} {up_or_down(Stock.AAPL)}
AMZN(Amazon): ${Stock.AMZN} {up_or_down(Stock.AMZN)}
NKE(Nike): ${Stock.NKE} {up_or_down(Stock.NKE)}''')
#displays the amount of each stock for the current day they are in

def valid_choice():
  if Stock.choice_of_stock_or_end == "TSLA":
    return "TSLA"
  elif Stock.choice_of_stock_or_end == "MSFT":
    return "MSFT"
  elif Stock.choice_of_stock_or_end == "NFLX":
    return "NFLX"
  elif Stock.choice_of_stock_or_end == "AAPL":
    return "AAPL"
  elif Stock.choice_of_stock_or_end == "AMZN":
    return "AMZN"
  elif Stock.choice_of_stock_or_end == "NKE":
    return "NKE"
#this def functions makes sure that only valid choices of stocks are being chosen
    
def valid_amount_of_shares_buy(amount_to_invest):
  if Stock.choice_of_stock_or_end == "TSLA" and (Stock.TSLA * amount_to_invest) <= Stock.total_money:
    return True
  elif Stock.choice_of_stock_or_end == "MSFT" and (Stock.MSFT * amount_to_invest) <= Stock.total_money:
    return True
  elif Stock.choice_of_stock_or_end == "NFLX" and (Stock.NFLX * amount_to_invest) <= Stock.total_money:
    return True
  elif Stock.choice_of_stock_or_end == "AAPL" and (Stock.AAPL * amount_to_invest) <= Stock.total_money:
    return True
  elif Stock.choice_of_stock_or_end == "AMZN" and (Stock.AMZN * amount_to_invest) <= Stock.total_money:
    return True
  elif Stock.choice_of_stock_or_end == "NKE" and (Stock.NKE * amount_to_invest) <= Stock.total_money:
    return True
  
  else:
    return False
#this def function checks that the Stock inputed is one that is stated and if they have enough money to buy the certain amount of stock they want to buy

def buying_shares(joe2):
  if Stock.choice_of_stock_or_end == "TSLA":
    subtract = Stock.total_money - (Stock.TSLA * joe2)
    Stock.total_money = subtract
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.TSLA_shares += joe2
    return True
  elif Stock.choice_of_stock_or_end == "MSFT":
    subtract = Stock.total_money - (Stock.MSFT * joe2)
    Stock.total_money = subtract
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.MSFT_shares += joe2
    return True
  elif Stock.choice_of_stock_or_end == "NFLX":
    subtract = Stock.total_money - (Stock.NFLX * joe2)
    Stock.total_money = subtract
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.NFLX_shares += joe2
    return True
  elif Stock.choice_of_stock_or_end == "AAPL":
    subtract = Stock.total_money - (Stock.AAPL * joe2)
    Stock.total_money = subtract
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.AAPL_shares += joe2
    return True
  elif Stock.choice_of_stock_or_end == "AMZN":
    subtract = Stock.total_money - (Stock.AMZN * joe2)
    Stock.total_money = subtract
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.AMZN_shares += joe2
    return True
  elif Stock.choice_of_stock_or_end == "NKE":
    subtract = Stock.total_money - (Stock.NKE * joe2)
    Stock.total_money = subtract
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.NKE_shares += joe2
    return True

def valid_amount_of_shares_sell(amount_to_sell):
  if Stock.choice_of_stock_or_end == "TSLA" and Stock.TSLA_shares >= amount_to_sell:
    return True
  elif Stock.choice_of_stock_or_end == "MSFT" and Stock.MSFT_shares >= amount_to_sell:
    return True
  elif Stock.choice_of_stock_or_end == "NFLX" and Stock.NFLX_shares >= amount_to_sell:
    return True
  elif Stock.choice_of_stock_or_end == "AAPL" and Stock.AAPL_shares >= amount_to_sell:
    return True
  elif Stock.choice_of_stock_or_end == "AMZN" and Stock.AMZN_shares >= amount_to_sell:
    return True
  elif Stock.choice_of_stock_or_end == "NKE" and Stock.NKE_shares >= amount_to_sell:
    return True
  
  else:
    return False

def selling_shares(amount_to_sell):
  if Stock.choice_of_stock_or_end == "TSLA":
    add = Stock.total_money + (Stock.TSLA * Stock.TSLA_shares)
    Stock.total_money = add
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.TSLA_shares -= amount_to_sell
    return True
  elif Stock.choice_of_stock_or_end == "MSFT":
    add = Stock.total_money + (Stock.MSFT * Stock.MSFT_shares)
    Stock.total_money = add
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.MSFT_shares -= amount_to_sell
    return True
  elif Stock.choice_of_stock_or_end == "NFLX":
    add = Stock.total_money + (Stock.NFLX * Stock.NFLX_shares)
    Stock.total_money = add
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.NFLX_shares -= amount_to_sell
    return True
  elif Stock.choice_of_stock_or_end == "AAPL":
    add = Stock.total_money + (Stock.AAPL * Stock.AAPL_shares)
    Stock.total_money = add
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.AAPL_shares -= amount_to_sell
    return True
  elif Stock.choice_of_stock_or_end == "AMZN":
    add = Stock.total_money + (Stock.AMZN * Stock.AMZN_shares)
    Stock.total_money = add
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.AMZN_shares -= amount_to_sell
    return True
  elif Stock.choice_of_stock_or_end == "NKE":
    add = Stock.total_money + (Stock.NKE * Stock.NKE_shares)
    Stock.total_money = add
    typingPrint(f"You now have ${Stock.total_money}\n")
    time.sleep(1)
    Stock.NKE_shares -= amount_to_sell
    return True   
  
Stock.day = 1
Stock.total_money = 10000
Stock.TSLA_shares = 0
Stock.AMZN_shares = 0
Stock.NKE_shares = 0
Stock.MSFT_shares = 0
Stock.NFLX_shares = 0
Stock.AAPL_shares = 0

#this sets the day to Day 1 and gives a starting money value to Stock.total_money and it starts you off with 0 shares
def intro():
     #^^ can be day or year or month or anything
  typingPrint("Welcome to BCCSE, The Base Camp Coding Stock Exchange!\nHere, people make millions or go into debt completely.\nYou have four work weeks, or 20 days to make $100,000!\n")


i = 0
intro()
time.sleep(1)
explain_stock()

typingPrin("\nloading . . . . . ")
time.sleep(1.5)
clearScreen()


while Stock.day <= 20: 
  if i > 0:
    typingPrin("\nloading . . . . . ")
    time.sleep(1)
  assign_arrows()
  print(f'''
        
Day {Stock.day} 
In the stock market
You have ${Stock.total_money}''')
  random_stock()
  display_day()
  Stock.switch = "on"
  while Stock.switch == "on":
    choice_to_buy_or_sell = typingInput("Would you like to buy, sell, or end: ").upper()
    time.sleep(1)
    while choice_to_buy_or_sell == "BUY":
      Stock.choice_of_stock_or_end = input("\nWhat stock do you want to invest in or input 'back' to go back: ").upper()
      if Stock.choice_of_stock_or_end == "BACK":
        break
      elif Stock.choice_of_stock_or_end != valid_choice():
        typingPrint("Invalid Stock\n")
        time.sleep(1)
      else:
        amount_to_invest = input("\nHow many shares do you want to buy: ")
        joe = amount_to_invest.isdigit()
        if joe:
          joe2 = int(amount_to_invest)
          if valid_amount_of_shares_buy(joe2):
            if buying_shares(joe2):
              break
          else:
            print("\n Get your money up not your funny up *growl*.\n (You do not have enough money for that)")
        else:
          print("Enter a number.")
    while choice_to_buy_or_sell == "SELL":
      Stock.choice_of_stock_or_end = input("\nWhat stock do you want to sell or input 'back' to go back: ").upper()
      if Stock.choice_of_stock_or_end == "BACK":
        break
      elif Stock.choice_of_stock_or_end != valid_choice():
        print("Invalid Stock.")
      else:
        amount_to_sell = input("\nHow many shares do you want to sell: ")
        joe3 = amount_to_sell.isdigit()
        if joe3:
          joe4 = int(amount_to_sell)
          if valid_amount_of_shares_sell(joe4):
            if selling_shares(joe4):
              break
          else:
            print("\n No shares? Couldn't be me.\n(You don't own that many shares)")
        else:
          typingPrint("Enter a number.")
          time.sleep(1)          
    if choice_to_buy_or_sell == "END":
      Stock.day += 1
      Stock.switch = "off"
      print("")
    if choice_to_buy_or_sell != "BUY" and choice_to_buy_or_sell != "SELL" and choice_to_buy_or_sell != "END":
      print("Invalid Input\n")
    i += 1

if Stock.total_money >= 100000:
  print("YOU WIN!!!")
else:
  print("YOU failed. . . . .")