from turtle import *


def menu():
   print("PYGON: MENU")
   print("[1] Draw a polygon")
   print("[2] Name a polygon")
   str_option = input("Select option: ")
   print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

   if not str_option.isnumeric():
       print("Invalid inputs")
       print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       menu()
       return

   option = int(str_option)

   if option == 1:
       draw()
   elif option == 2:
       name()
   else:
       print("Invalid inputs")
       print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       menu()


# Draw

def draw():
   print("Let's draw a polygon!")
   str_sides = input("Input sides in your polygon: ")
   clr = input("Input color of your polygon: ")
   str_size = input("Input size of the stroke: ")
   str_dis = input("Input size of your polygon: ")
   print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

   if not str_sides.isnumeric() and not str_size.isnumeric() and not str_dis.isnumeric():
       print("Invalid inputs")
       print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       menu()
       return

   sides = int(str_sides)
   size = int(str_size)
   dis = int(str_dis)

   agl = 360 / sides

   print("What a beautiful polygon!")

   shape("arrow")
   color(clr)
   pensize(size)
   for i in range(sides):
       forward(dis)
       left(agl)
   done()

   print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

   menu()


# Name

# Convert to Greek

def gr(n):
   x = ""
   if n == 1:
       x = "hena"
   elif n == 2:
       x = "di"
   elif n == 3:
       x = "tri"
   elif n == 4:
       x = "tetra"
   elif n == 5:
       x = "penta"
   elif n == 6:
       x = "hexa"
   elif n == 7:
       x = "hepta"
   elif n == 8:
       x = "octa"
   elif n == 9:
       x = "ennea"
   return x


# Naming

def name():
   print("Let's name a polygon!")
   sides = input("Input sides in your polygon: ")
   print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

   if not sides.isnumeric():
       print("Invalid Input")
       print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       menu()
       return

   sides = "0" * 7 + sides

   aa = int(sides[-1])
   bb = int(sides[-2])
   cc = int(sides[-3])
   dd = int(sides[-4])
   ee = int(sides[-5])
   ff = int(sides[-6])
   gg = int(sides[-7])

   # One

   if aa == 0:
       a = ""
   else:
       a = gr(aa)

   # Ten

   if bb == 0:
       b = ""
   elif bb == 1:
       if a == "":
           b = "deca"
       elif a == "hena":
           b = "hen" + "deca"
       elif a == "di":
           b = "do" + "deca"
       else:
           b = a + "deca"
       a = ""
   elif bb == 2:
       if a == "":
           b = "icos" + "a" + "kai"
       else:
           b = "icos" + "i" + "kai"
   elif bb == 3:
       b = "tri" + "a" + "conta" + "kai"
   else:
       b = gr(bb) + "conta" + "kai"

   # Hundred

   if cc == 0:
       c = ""
   elif cc == 1:
       c = "hecta"
   else:
       c = gr(cc) + "hecta"

   # Thousand

   if dd == 0:
       d = ""
   elif dd == 1:
       d = "chilia"
   elif dd == 2 or dd == 3:
       d = gr(dd) + "s" + "chilia"
   else:
       d = gr(dd) + "kis" + "chilia"

   # Ten Thousand

   if ee == 0:
       e = ""
   elif ee == 1:
       e = "myria"
   elif ee == 2 or ee == 3:
       e = gr(ee) + "s" + "myria"
   else:
       e = gr(ee) + "kis" + "myria"

   # Hundred Thousand

   if ff == 0:
       f = ""
   elif e != "":
       if ff == 1:
           f = "deca"
       elif ff == 2:
           f = "icos" + "i"
       elif ff == 3:
           f = "tri" + "a" + "conta"
       else:
           f = gr(ff) + "conta"
   elif ff == 1:
       f = "deca" + "kis" + "myria"
   elif ff == 2:
       f = "icos" + "i" + "kis" + "myria"
   elif ff == 3:
       f = "tri" + "a" + "conta" + "kis" + "myria"
   else:
       f = gr(ff) + "conta" + "kis" + "myria"

   # Million

   if gg == 0:
       g = ""
   elif gg == 1:
       g = "mega"
   else:
       g = gr(gg) + "mega"

   print("The polygon is called", g + f + e + d + c + b + a + "gon" + "!")
   print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
   menu()


menu()
