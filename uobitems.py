from flask import session
session["user"]="Rubbish"
class uobitems:
    def __init__(self,item, type, points,image,width,height,full_name):
        self.__item = item
        self.__type = type
        self.__points = points
        self.__image = image
        self.__width = width
        self.__height = height
        self.__full_name = full_name
        self.__maxquantity = 0
        self.__addtocartqty= 0
        self.__count = 0

    def get_item(self):
        return self.__item

    def get_type (self):
        return self.__type

    def get_points(self):
        return self.__points

    def get_maxquantity(self):
        return self.__maxquantity

    def get_image(self):
        return self.__image

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_count(self):
        return self.__count

    def get_full_name(self):
        return self.__full_name

    def set_item(self, item):
        self.__item = item

    def set_type(self, type):
        self.__type = type

    def set_points(self, points):
        self.__points = points

    def set_maxquantity(self, maxquantity):
        self.__maxquantity = maxquantity

    def set_image(self, image):
        self.__image = image

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_item(self, count):
        self.__count = count

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def processnumberquantity(self):
        uob_points = []
        uobpts_file = open("file/avaliableuobpts.txt", "r")
        for points in uobpts_file:
            point = points.split(",")
            if session["user"] == points[0]:
                uob_points.append(int(point[2]))
        uobcurrentpts = int(uob_points[-1])
        if (uobcurrentpts >= int(self.get_points())):
            quantity = uobcurrentpts // int(self.get_points())
            self.set_maxquantity(quantity)
            return self.get_maxquantity()

    def list_qty(self):
        qty = self.processnumberquantity()
        quantity_option = []
        for num in range(qty):
            num += 1
            quantity_option.append(num)
        return quantity_option

    def addtocart(self):
            points = self.get_points

    def set_addtocartqty(self, addtocartqty):
        self.__addtocartqty = addtocartqty

    def get_addtocartqty(self):
        return self.__addtocartqty





 #   def totalitem_pts(self):
  #      return self.__points * self.__quantity







