import schedule
import time


def func_1():
    print("Go to the shop")


def func_2():
    print("Study Czech")


def func_3():
    print("Do homework")


def func_4():
    print("Play basketball")


def func_5():
    print("Prepare for the final exam at school")


def func_6():
    print("Study English")


schedule.every(1).minutes.do(func_1)
schedule.every().day.at("10:30").do(func_2)
schedule.every().monday.do(func_5)
schedule.every().friday.do(func_4)
schedule.every().wednesday.at("13:15").do(func_3)
schedule.every().hour.at(":35").do(func_2)
schedule.every().tuesday.at("17:10").do(func_6)
schedule.every().thursday.at("19:10").do(func_6)

while True:
    schedule.run_pending()
    time.sleep(1)
