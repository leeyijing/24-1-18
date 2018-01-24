from uobitems import uobitems
from allredemption import allredemption
import datetime

def processtrenditems(name,cardno):
    trend_items =[]
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[1] == "Nike Voucher" or individual_items[1] == "Shaw Theatre Tickets" or individual_items[1] == "Swensen's Voucher"):
            if (points >= int(individual_items[3])):
                t = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                trend_items.append(t)
    return trend_items

def processallitems(name,cardno):
    allitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (points >= int(individual_items[3])):
            c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                individual_items[4], individual_items[5], individual_items[6],individual_items[7])
            allitems.append(c)
    return allitems


def processretailitems(name,cardno):
    retailitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point=[]
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Retail"):
            if (points >= int(individual_items[3])):
                c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                retailitems.append(c)
    return retailitems

def processdiningitems(name,cardno):
    diningitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Dining"):
            if (points >= int(individual_items[3])):
                d = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                diningitems.append(d)
    return diningitems


def processleisureitems(name,cardno):
    leisureitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            pt =points.split(",")
            point.append(int(pt[2]))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Leisure"):
            if (points >= int(individual_items[3])):
                e = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                leisureitems.append(e)
    return leisureitems



def processpoints(name,cardno):
    #uob_allpoints =[]
    uob_currentpts = 0
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    for j in avaliableuobpts_file:
        transaction = j.split(",")
        if transaction[0] == name and transaction[1] == cardno:
            uob_currentpts = transaction[2]
     #           uob_allpoints.append(int(transaction[2]))
    #uob_currentpts = uob_allpoints[-1]
    return uob_currentpts



# in transaction history of redemption
def processallredemption(name,cardno):
    allredemptionList =[]
    allredemption_file = open("file/allredemption.txt", "r")
    for i in  allredemption_file:
        list = i.split(',')
        if list[0] == name:
            s = allredemption(list[1], list[2], list[3], list[4], int(list[5]),list[6])
            allredemptionList.append(s)
    return allredemptionList

def processsallnovredemption(name, cardno):
    allnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1]== "11":
                z = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allnovredemptionList.append(z)
    return allnovredemptionList

def processsalldecredemption(name, cardno):
    alldecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1]== "12":
                z = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldecredemptionList.append(z)
    return alldecredemptionList


def addtocart(user, cardno,current_point, redeem_point, points, quantity):
    amount = int(points) * int(quantity)
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
    avaliableuobpts_file.close()
    currentpoint_file = open("file/currentuobpts.txt", "a")
    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
    currentpoint_file.close()



#def removefromcart(self, user, cardno,current_point, redeem_point, points, quantity):
#    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
#    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
#    avaliableuobpts_file.close()
#    currentpoint_file = open("file/currentuobpts.txt", "a")
#    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
#    currentpoint_file.close()



