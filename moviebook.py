import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Nikita')
mycur=conn.cursor()
mycur.execute('create database MUMBAI_MOVIETICKETBOOKING_SYSTEM')
conn.close()

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Nikita',database='MUMBAI_MOVIETICKETBOOKING_SYSTEM')
mycur=conn.cursor()
mycur.execute('create table MOVIES_STREAMING(MOVIENAME VARCHAR(60),GENRE VARCHAR(60),LANGUAGE VARCHAR(60),PRODUCED_BY VARCHAR(60),DIRECTED_BY VARCHAR(60),STARRING VARCHAR(60),RELEASE_DATE VARCHAR(50))')
qry1="insert into MOVIES_STREAMING values(%s,%s,%s,%s,%s,%s,%s)"
data1=[("CHAPPAK","BIOGRAPHY","HINDI","MEGHNA GULZAR,DEEPIKA PADUKONE","MEGHNA GULZAR","DEEPIKA PADUKONE","13thJUNE2020"),("BAAGHI3","ACTION THRILLER","HINDI","SAJID NADIADWALA","AHMED KHAN","TIGER SHROFF,RITESH DESHMUKH,SHRADDHA KAPOOR","13thJUNE2020"),("GUNJAN SAXENA:THE KARGIL GIRL","BIOGRAPHY","HINDI","KARAN JOHAR,HIROO JOHAR,APPORVA MEHTA","SHARAN SHARMA","JANHVI KAPOOR,PANKAJ TRIPATHI,ANGAD BEDI","12thJUNE2020"),("TANHAJI","HISTORICAL,BIOGRAPHICAL PERIOD ACTION FILM","HINDI","BHUSHAN KUMAR,KRISHAN KUMAR,AJAY DEVGN","OM RAUT","AJAY DEVGN,KAJOL,SAIF ALI KHAN","12thJUNE2020")]
mycur.executemany(qry1,data1)
mycur.execute('create table THEATRES_MUMBAI(SLNO int,THEATRENAME VARCHAR(60),LOCATION VARCHAR(60),CAPACITY INT,FACILITY VARCHAR(20))')
qry2="insert into THEATRES_MUMBAI values(%s,%s,%s,%s,%s)"
data2=[(1,"MARATHA MANDIR THEATRE","MARATHA MANDIR MARG,MUMBAI,INDIA",1000,"AC"),
      (2,"THE ROYAL OPERA HOUSE","CHARNI ROAD,MUMBAI,INDIA",1000,"AC"),
      (3,"PRITHVI THEATRE","JUHU,MUMBAI,INDIA",1000,"AC"),
      (4,"TATA THEATRE","NCPA COMPLEX,MUMBAI,INDIA",1010,"NON AC"),
      (5,"JAMSHED BHABHA THEATRE","NCPA COMPLEX,MUMBAI,INDIA",1109,"NON AC"),
      (6,"REGAL CINEMA","COLABA CAUSEWAY,MUMBAI,INDIA",1000,"AC")]
mycur.executemany(qry2,data2)
mycur.execute('create table MARATHA_MANDIR_THEATRE(SLNO INT,MOVIE_STREAMING VARCHAR(60),SHOW_TIME VARCHAR(60),RUNNING_TIME VARCHAR(60),PAY_PER_TICKET VARCHAR(70))')
mycur.execute('create table THE_ROYAL_OPERA_HOUSE(SLNO INT,MOVIE_STREAMING VARCHAR(60),SHOW_TIME VARCHAR(60),RUNNING_TIME VARCHAR(60),PAY_PER_TICKET VARCHAR(70))')
mycur.execute('create table PRITHVI_THEATRE(SLNO INT,MOVIE_STREAMING VARCHAR(60),SHOW_TIME VARCHAR(60),RUNNING_TIME VARCHAR(60),PAY_PER_TICKET VARCHAR(70))')
mycur.execute('create table TATA_THEATRE(SLNO INT,MOVIE_STREAMING VARCHAR(60),SHOW_TIME VARCHAR(60),RUNNING_TIME VARCHAR(60),PAY_PER_TICKET VARCHAR(70))')
mycur.execute('create table JAMSHED_BHABHA_THEATRE(SLNO INT,MOVIE_STREAMING VARCHAR(60),SHOW_TIME VARCHAR(60),RUNNING_TIME VARCHAR(60),PAY_PER_TICKET VARCHAR(70))')
mycur.execute('create table REGAL_CINEMA(SLNO INT,MOVIE_STREAMING VARCHAR(60),SHOW_TIME VARCHAR(60),RUNNING_TIME VARCHAR(60),PAY_PER_TICKET VARCHAR(70))')
qry3="insert into MARATHA_MANDIR_THEATRE values(%s,%s,%s,%s,%s)"
data3=[(1,"CHAPPAK","11:30AM -2:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (2,"CHAPPAK","2:30PM-5:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
     (3,"TANHAJI","5:30PM-8:00PM","135 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
  (4,"CHAPPAK","9:00PM-11:30PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES")]
mycur.executemany(qry3,data3)
qry4="insert into REGAL_CINEMA values(%s,%s,%s,%s,%s)"
data4=[(1,"CHAPPAK","11:30AM -2:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (2,"CHAPPAK","2:30PM-5:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
     (3,"TANHAJI","5:30PM-8:00PM","135 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (4,"CHAPPAK","9:00PM-11:30PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES")]
mycur.executemany(qry4,data4)
qry5="insert into PRITHVI_THEATRE values(%s,%s,%s,%s,%s)"
data5=[(1,"CHAPPAK","11:30AM -2:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (2,"CHAPPAK","2:30PM-5:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
     (3,"GUNJAN SAXENA:THE KARGIL GIRL","5:30PM-8:00PM","112 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (4,"CHAPPAK","9:00PM-11:30PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES")]
mycur.executemany(qry5,data5)
qry6="insert into JAMSHED_BHABHA_THEATRE values(%s,%s,%s,%s,%s)"
data6=[(1,"CHAPPAK","11:30AM -2:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (2,"CHAPPAK","2:30PM-5:00PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
     (3,"GUNJAN SAXENA:THE KARGIL GIRL","5:30PM-8:00PM","112 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (4,"CHAPPAK","9:00PM-11:30PM","141 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES")]
mycur.executemany(qry6,data6)
qry7="insert into THE_ROYAL_OPERA_HOUSE values(%s,%s,%s,%s,%s)"
data7=[(1,"BAAGHI3","11:30AM -2:00PM","143 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (2,"BAAGHI3","2:30PM-5:00PM","143 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
     (3,"GUNJAN SAXENA:THE KARGIL GIRL","5:30PM-8:00PM","112 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (4,"BAAGHI3","9:00PM-11:30PM","143 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES")]
mycur.executemany(qry7,data7)
qry8="insert into TATA_THEATRE values(%s,%s,%s,%s,%s)"
data8=[(1,"BAAGHI3","11:30AM -2:00PM","143 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (2,"BAAGHI3","2:30PM-5:00PM","143 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
     (3,"TANHAJI","5:30PM-8:00PM","135 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES"),
    (4,"BAAGHI3","9:00PM-11:30PM","143 MINUTES","BALCONY-110 RUPEES,1ST CLASS-80 RUPEES,2ND CLASS-60 RUPEES")]
mycur.execute('create table customer_details(EMAIL_ADDRESS VARCHAR(100),CONTACTNO bigint,CODE int,THEATRE int,MOVIE int,NO_OF_TICKETS int,SEATING varchar(60),TOTAL_AMOUNT int)')
mycur.executemany(qry8,data8)
conn.commit()
conn.close()

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Nikita',database='MUMBAI_MOVIETICKETBOOKING_SYSTEM')
mycur=conn.cursor()
def movies_streamingnow():
    qry9=("select * from MOVIES_STREAMING")
    mycur.execute(qry9)
    print("MOVIES STREAMING DETAILS")
    print("________________________")
    for(MOVIENAME,GENRE,LANGUAGE,PRODUCED_BY,DIRECTED_BY,STARRING,RELEASE_DATE) in mycur:
        print("MOVIENAME  :",MOVIENAME)
        print("GENRE      :",GENRE)
        print("LANGUAGE   :",LANGUAGE)
        print("PRODUCED BY:",PRODUCED_BY)
        print("DIRECTED BY:",DIRECTED_BY)
        print("STARRING   :",STARRING)
        print("RELEASE    :",RELEASE_DATE)
        print()
    conn.commit()        
def mumbai_theatres():
    comm=("select * from THEATRES_MUMBAI")
    mycur.execute(comm)
    print("THEATRES IN MUMBAI DETAILS ")
    print("__________________________")
    for (SLNO,THEATRENAME,LOCATION,CAPACITY,FACILITY) in mycur:
        print("SLNO:",SLNO)
        print("THEATRE NAME:",THEATRENAME)
        print("LOCATION    :",LOCATION)
        print("CAPACITY    :",CAPACITY)
        print("FACILITY    :",FACILITY)
        print()
    conn.commit()
def customer_service():
    while True:
        print("\n")
        print("__________________________________________________________________________")
        print("\n")
        print("1.BOOKING MOVIE TICKETS")
        print("2.SHOW CUSTOMER DETAILS")
        print("3.UPDATE CUSTOMER DETAILS")
        print("4.CANCEL BOOKING")
        print("5.RETURN TO MAIN MENU")
        print("\n")
        print("__________________________________________________________________________")
        print("\n")
        choice=input("ENTER YOUR CHOICE(SLNO):")
        
        if (choice=="1"):
            z="y"
            while (z.lower()=="y"):
                inputdata()
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
            if (z.lower()=="n"):
                return customer_service()
            else:
                print("INVALID INPUT!!")
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
        elif (choice=="2"):
            z="y"
            while (z.lower()=="y"):
                display()
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
            if (z.lower()=='n'):
                return customer_service()
            else:
                print("INVALID INPUT!!")
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
        elif (choice=="3"):
           z="y"
           while (z.lower()=="y"):
                update()
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
           if (z.lower()=='n'):
                return customer_service()
           else:
                print("INVALID INPUT!!")
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
        elif (choice=="4"):
          z="y"
          while (z.lower()=="y"):
                cancel()
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
          if (z.lower()=='n'):
                return customer_service()
          else:
                print("INVALID INPUT!!")
                z=input("\n DO YOU WANT TO CONTINUE...(y/n):")
        elif (choice=="5"):
          return mainmenu()
        else:
         print("INVALID INPUT!!")
                
                
def maratha_mandir_theatre():
    comm1='select * from MARATHA_MANDIR_THEATRE'
    mycur.execute(comm1)
    print("MARATHA MANDIR THEATRE DETAILS")
    print("_____________________________")
    for (slno,movie_streaming,show_time,running_time,pay_per_ticket) in mycur:
        print("\n")
        print("SLNO:",slno)
        print("MOVIE STREAMING:",movie_streaming)
        print("SHOW TIME      :",show_time)
        print("RUNNING TIME   :",running_time)
        print("PAY PER TICKET :",pay_per_ticket)
        print("\n")
    conn.commit()    
      
def the_royal_opera_house():
    comm2='select * from THE_ROYAL_OPERA_HOUSE'
    mycur.execute(comm2)
    print("THE ROYAL OPERA HOUSE DETAILS")
    print("_____________________________")
    for (slno,movie_streaming,show_time,running_time,pay_per_ticket) in mycur:
        print("\n")
        print("SLNO:",slno)
        print("MOVIE STREAMING:",movie_streaming)
        print("SHOW TIME      :",show_time)
        print("RUNNING TIME   :",running_time)
        print("PAY PER TICKET :",pay_per_ticket)
        print("\n")
    conn.commit()    
def prithvi_theatre():
    comm3='select * from PRITHVI_THEATRE'
    mycur.execute(comm3)
    print("PRITHVI_THEATRE DETAILS")
    print("_____________________________")
    for (slno,movie_streaming,show_time,running_time,pay_per_ticket) in mycur:
        print("\n")
        print("SLNO:",slno)
        print("MOVIE STREAMING:",movie_streaming)
        print("SHOW TIME      :",show_time)
        print("RUNNING TIME   :",running_time)
        print("PAY PER TICKET :",pay_per_ticket)
        print("\n")
    conn.commit()    
def tata_theatre():
    mycursor=conn.cursor()
    comm4='select * from TATA_THEATRE'
    mycur.execute(comm4)
    print("TATA_THEATRE DETAILS")
    print("_____________________________")
    for (slno,movie_streaming,show_time,running_time,pay_per_ticket) in mycur:
        print("\n")
        print("SLNO:",slno)
        print("MOVIE STREAMING:",movie_streaming)
        print("SHOW TIME      :",show_time)
        print("RUNNING TIME   :",running_time)
        print("PAY PER TICKET :",pay_per_ticket)
        print("\n")
    conn.commit()    
def jamshed_bhabha_theatre():
    comm5='select * from JAMSHED_BHABHA_THEATRE'
    mycur.execute(comm5)
    print("JAMSHED_BHABHA_THEATRE DETAILS")
    print("_____________________________")
    for (slno,movie_streaming,show_time,running_time,pay_per_ticket) in mycur:
        print("\n")
        print("SLNO:",slno)
        print("MOVIE STREAMING:",movie_streaming)
        print("SHOW TIME      :",show_time)
        print("RUNNING TIME   :",running_time)
        print("PAY PER TICKET :",pay_per_ticket)
        print("\n")
    conn.commit() 
def regal_cinema():
    comm6='select * from REGAL_CINEMA'
    mycur.execute(comm6)
    print("REGAL CINEMA DETAILS")
    print("_____________________________")
    for (slno,movie_streaming,show_time,running_time,pay_per_ticket) in mycur:
        print("\n")
        print("SLNO:",slno)   
        print("MOVIE STREAMING:",movie_streaming)
        print("SHOW TIME      :",show_time)
        print("RUNNING TIME   :",running_time)
        print("PAY PER TICKET :",pay_per_ticket)
        print("\n")
    conn.commit()
conn.close()    
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Nikita',database='MUMBAI_MOVIETICKETBOOKING_SYSTEM')
mycur=conn.cursor()
def inputdata():
    email_address=input("\n ENTER EMAIL ADDRESS:")
    contact_no=int(input("\n ENTER CONTACT NO:"))
    code=int(input("CREATE AND ENTER A PASSWORD THAT CONTAINS ONLY NUMBERS:"))
    print(" NOTE: DO NOT FORGET THIS PASSWORD...THIS PASSWORD MAY BE REQUIRED LATER")
    print()
    mumbai_theatres()
    theatre=input("ENTER YOUR CHOICE(SLNO):")   
    if theatre=="1":
        maratha_mandir_theatre()
    elif theatre=="2":
        the_royal_opera_house()
    elif theatre=="3":
        prithvi_theatre()
    elif theatre=="4":
        tata_theatre()
    elif theatre=="5":
        jamshed_bhabha_theatre
    elif theatre=="6":
        regal_cinema()
    else:
        print("INVALID INPUT!!")
        return inputdata() 
    print("IN THE NEXT LINE ENTER THE SLNO CORRESPONDING TO THE MOVIE YOU WANT TO WATCH AT THE SPECIFIED TIME")
    movie=input("ENTER THE SLNO:")
    no_of_tickets=int(input("ENTER THE NO OF TICKETS"))
    seating=input("enter BALCONY/FIRST CLASS/SECOND CLASS IN CAPITAL LETTERS")
    if seating=="BALCONY":
        TOTAL_PAY=no_of_tickets*110
        print("TOTAL AMOUNT :",TOTAL_PAY)
    elif seating=="FIRST CLASS":
        TOTAL_PAY=no_of_tickets*80
        print("TOTAL AMOUNT :",TOTAL_PAY)
    elif seating=="SECOND CLASS":
        TOTAL_PAY=no_of_tickets*60
        print("TOTAL AMOUNT :",TOTAL_PAY)
    else:
        print("INVALID INPUT!!")
        return customer_service()

    print("YOU HAVE COMPLETED THE BOOKING PROCESS SUCCESSFULLY")
    print("A MESSAGE WILL BE SEND TO YOUR CONTACT_NO OR EMAIL ADDRESS WHICH HAS TO BE SHOWN ON REACHING THE THEATRE AND THE PAYMENT SHOULD BE MADE THERE")
    
    data=(email_address,contact_no,code, theatre,movie,no_of_tickets,seating,TOTAL_PAY)
    mycur.execute('insert into customer_details(EMAIL_ADDRESS,CONTACTNO,CODE,THEATRE,MOVIE,NO_OF_TICKETS,SEATING,TOTAL_AMOUNT) values(%s,%s,%s,%s,%s,%s,%s,%s)',data)
    conn.commit()
    return customer_service()
def display():
            ans=input("HAVE YOU BOOKED FOR WATCHING ANY MOVIE(y/n):")  
            if ans.lower()=="n":
               return customer_service()
            elif ans.lower()=="y":
                ccode=input("ENTER THE PASSWORD THAT YOU PREVIOUSLY ENTERED")
                email_address=input("\nENTER THE EMAIL ID THAT YOU PREVIOUSLY ENTERED:")
                ch='y'
                while(ch=='y'):
                     mycur.execute("select * from customer_details where code='{}'and email_address='{}'".format(ccode,email_address))  
                                                              
                     rs="y"  
                     while (rs.lower()=="y"):
                        res=mycur.fetchall()
                        if not res:
                            print("YOU HAVE ENTERED THE WRONG PASSWORD OR EMAIL ADDRESS")
                            return customer_service()
                        for row in res:
                            print("\n EMAIL ADDRESS:",row[0])           
                            print("\n CONTACT NO   :",row[1])
                            print("\n CODE         :",row[2])
                            print("\n THEATRENO    :",row[3])
                            print("\n MOVIENO      :",row[4])
                            print("\n NO_OF_TICKETS:",row[5]) 
                            print("\n SEATING      :",row[6])
                            print("\n TOTAL AMOUNT :",row[7])
                        return customer_service()
            else:
                  print("INVALID INPUT")
                  return customer_service()     

            conn.commit()       
              
def update():
     ans=input("HAVE YOU BOOKED FOR WATCHING ANY MOVIE(y/n):")
     if ans.lower()=="n":
        return customer_service()
     elif ans.lower()=="y":
        ccode=input("ENTER THE PASSWORD THAT YOU PREVIOUSLY ENTERED")
        email_address=input("\nENTER THE EMAIL ID THAT YOU PREVIOUSLY ENTERED:")
        print("1.UPDATE EMAIL ADDRESS 2.UPDATE CONTACT NO")
        updation=input("ENTER 1 OR 2")
        if updation=="1":
              email_address=input("ENTER NEW EMAIL ADDRESS")
              mycur.execute("update customer_details set email_address='{}' where code='{}'".format(email_address,ccode))
              print("YOUR EMAIL ADDRESS HAS BEEN UPDATED")
        elif updation=="2":
             contact_no=int(input("ENTER NEW CONTACT NO"))
             mycur.execute("update customer_details set contactno={} where code='{}'".format(contact_no,ccode))
             print("YOUR CONTACT NO HAS BEEN UPDATED")
        else:
            print("INVALID UPDATION!!PLEASE TRY AGAIN")
            return update()
        
     else:
         print("INVALID INPUT")
         return customer_service()
     conn.commit()
def cancel():
    ans=input("HAVE YOU BOOKED FOR WATCHING ANY MOVIE(y/n):")
    if ans.lower()=="n":
        return customer_service()
    elif ans.lower()=="y":
        ccode=input("ENTER THE PASSWORD THAT YOU PREVIOUSLY ENTERED")    
        email_address=input("\nENTER THE EMAIL ID THAT YOU PREVIOUSLY ENTERED:")
        mycur.execute("select * from customer_details where code='{}'".format(ccode))
        print("YOUR BOOKING IS CANCELLED")
        return customer_service()
    else:
        print("INVALID INPUT")
        return customer_service()     

    conn.commit()
def feedback():
    import csv
    with open('myfeedback.csv',mode='w',newline='') as csvfile:
        mywriter=csv.writer(csvfile,delimiter=',')
        ans='y'
        while ans.lower()=='y':
            feedback=input("PLEASE ENTER YOUR VALUABLE FEEDBACKS ON OUR SERVICE")
            print("5-excellent 4-good 3-average 2-below average 1-bad")
            star_rating=input("HOW DO YOU RATE US OUT OF 5?")
            improvements=input("PLEASE ADD YOUR VALUABLE SUGGESTIONS TO IMPROVE OUR SERVICE")
            mywriter.writerow([feedback,star_rating,improvements])
           
            ans=input("add more?(y/n)")
    csvfile.close()
    with open('myfeedback.csv',mode='r') as csvfile:
         myreader=csv.reader(csvfile)
         for row in myreader:
              print("YOUR FEEDBACK IS:")
              print(row[0])
              print("STAR RATING",row[1])
              print(row[2])
    csvfile.close()
def carparking():
     import csv
     with open('carparking.csv',mode='w',newline='') as csvfile:
        mywriter=csv.writer(csvfile,delimiter=',')
        mycur.execute('create table carparking(EMAILADDRESS varchar(60),SELECTION varchar(60),SPACE varchar(60))')
        ans='y'
        while ans.lower()=='y':
            print("WE HAVE INTRODUCED A NEW SERVICE WHERE YOU CAN BOOK CARPARKING BEFOREHAND FOR YOUR CONVINENCE")
            print("THE SPACE YOU HAVE BOOKED WILL NOT BE ALLOTED TO ANYONE ELSE")
            print("PARKING BLOCKS ARE CP1,CP2,CP3,CP4")
            emailaddress=input("ENTER YOUR EMAILADRESS")
            selection=input("ENTER CP1/CP2/CP3/CP4")
            space=input("how many space do you need? NOTE:ONE SPACE FOR ONE CAR AND FOR EACH SPACE PAY IS 30 RS")
            mywriter.writerow([selection,space])
            ans='n'
            
     csvfile.close()
     with open('carparking.csv',mode='r') as csvfile:
         myreader=csv.reader(csvfile)
         for row in myreader:
              print(row[1],"SPACE IN",row[0],"HAS BEEN BOOKED FOR YOU")
              print("THE CAR PARKING FEE HAVE TO BE PAID ON REACHING THE LOCATION")
              print("A MESSAGE WILL BE SEND TO YOUR EMAIL ADDRESS,WHICH HAS TO BE SHOWN ON REACHING THE LOCATION AND PAYMENT HAS TO BE MADE THERE")
     csvfile.close()  
     data=(emailaddress,selection,space)
     mycur.execute('insert into carparking(EMAILADDRESS,SELECTION,SPACE)values(%s,%s,%s)',data)
     conn.commit()
def mainmenu():
    
    print()
    print("        WELCOME TO THE MUMBAI MOVIE TICKET BOOKING SYSTEM          ")
    print()
    while True:
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1.MOVIES STREAMING NOW")
        print("2.THEARTES")
        print("3.MOVIE TICKET BOOKING AND COSTUMER MANAGAMENT")
        print("4.CARPARKING BOOKING")
        print("5.FEEDBACK")
        print("6.EXIT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        b=input("\nENTER YOUR CHOICE(SLNO):")
        if (b=='1'): 
            movies_streamingnow()
        elif(b=='2'):
            mumbai_theatres()
        elif(b=='3'):
            customer_service()
        elif (b=='4'):
            carparking()
        elif (b=='5'):
            feedback()
        elif (b=='6'):
             quit()
        else:
             print("WRONG CHOICE")
mainmenu()
conn.close()        

                

