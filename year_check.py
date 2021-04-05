from colorama import init, deinit, Fore, Back, Style
init(autoreset=True)
""" for colored output run from command prompt from output"""

banner = """╦ ╦┌─┐┌─┐┬─┐  ┌─┐┬ ┬┌─┐┌─┐┬┌─
╚╦╝├┤ ├─┤├┬┘  │  ├─┤├┤ │  ├┴┐
 ╩ └─┘┴ ┴┴└─  └─┘┴ ┴└─┘└─┘┴ ┴"""
            
print(Fore.RED+banner)
try:
    b=Fore.YELLOW+"This Programe Tells You Leap year or NOT and Gives The Days From Same year"
    print(b,"\n")
    play_again = True
    def leap_year(year,month,day):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    total_days = 0
                    dit = {1:31,2:29,3:31,4:30,5:31,6:31,7:30,8:31,9:30,10:31,11:30,12:31}
                    for i in range(1,month):
                        total_days += dit[i]
                    total_days += day
                    print(str(year)+" is leap year and "+str(month)+" month has "+str(dit[month])+" days.","days are",total_days,".\n")
                else:
                    total_days = 0
                    dit = {1:31,2:28,3:31,4:30,5:31,6:31,7:30,8:31,9:30,10:31,11:30,12:31}
                    for i in range(1,month):
                        total_days += dit[i]
                    total_days += day
                    print(str(year)+" is not leap year and "+str(month)+" month has "+str(dit[month])+" days.","days are",total_days,".\n")
            else:
                    total_days = 0
                    dit = {1:31,2:28,3:31,4:30,5:31,6:31,7:30,8:31,9:30,10:31,11:30,12:31}
                    for i in range(1,month):
                        total_days += dit[i]
                    total_days += day
                    print(str(year)+" is leap year and "+str(month)+" month has "+str(dit[month])+" days.","days are",total_days,".\n")
        else :
            total_days = 0
            dit = {1:31,2:28,3:31,4:30,5:31,6:31,7:30,8:31,9:30,10:31,11:30,12:31}
            for i in range(1,month):
                total_days += dit[i]
            total_days += day
            print(str(year)+" is not leap year and "+str(month)+" month has "+str(dit[month])+" days.","days are",total_days,".\n")


    yr = int(input("Enter year : "))
    mn = int(input("Enter month : "))
    dy = int(input("Enter day : "))

    leap_year(yr,mn,dy)

    while play_again:
        ask = input("\nwould you liketo play again if yes press 1 or press \"q\" to quit :) ")
        if ask == "1":
            play_again = True
            b_yr = int(input("Enter year : "))
            b_mn = int(input("Enter month : "))
            b_dy = int(input("Enter day : "))
            leap_year(b_yr,b_mn,b_dy)
        elif ask == 'q':
            play_again = False

    """creatd by Atul"""
    """run from cmd for colors"""
except:
 print("you may have entered wron input try again")
