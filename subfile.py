import wx
from wx import *
import math
from math import *
import wx.lib.buttons as bt
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="rms"
)
cursor = con.cursor()

app = App()
root = Frame(None, title="Restaurant Management", size=(1200, 650))
panel = Panel(root)
panel.SetBackgroundColour("#FF6347")
root.SetIcon(Icon("img/icon.png"))


cursor.execute("SELECT * FROM price")
calling_price=cursor.fetchall()
#variable of rms price

samosa_price = str(calling_price[0][1])
burger_price = str(calling_price[0][2])
sandwich_price = str(calling_price[0][3])
pizza_price = str(calling_price[0][4])
dosa_price = str(calling_price[0][5])
idli_price = str(calling_price[0][6])
roll_price = str(calling_price[0][7])
momos_price = str(calling_price[0][8])
cutlet_price = str(calling_price[0][9])

# Functions
def total_value(e):
    total_frame=Frame(None,title="Total Value",size=(342,395))
    total_panel=Panel(total_frame)
    total_panel.SetBackgroundColour("black")
    mainbox=BoxSizer(VERTICAL)
    tc_font=Font(20,FONTFAMILY_ROMAN,FONTSTYLE_NORMAL,FONTWEIGHT_BOLD)
    tc=TextCtrl(total_panel,1,size=(300,50),style=TE_RIGHT)
    tc.SetFont(tc_font)
    tc.SetValue("0")
    mainbox.Add(tc, 0, TOP |BOTTOM| CENTER, 10)

    grid=GridSizer(4,4,5,5)
    bt1=bt.GenBitmapButton(total_panel,-1,Bitmap("img/1.bmp"),size=(70,60))
    def tt(e):
        tc.SetValue(1 )


    bt1.Bind(EVT_BUTTON,tt,bt1)
    bt2=bt.GenBitmapButton(total_panel,-1,Bitmap("img/2.bmp"),size=(70,60))
    bt3=bt.GenBitmapButton(total_panel,-1,Bitmap("img/3.bmp"),size=(70,60))
    bt4=bt.GenBitmapButton(total_panel,-1,Bitmap("img/+.bmp"),size=(70,60))
    bt5=bt.GenBitmapButton(total_panel,-1,Bitmap("img/4.bmp"),size=(70,60))
    bt6=bt.GenBitmapButton(total_panel,-1,Bitmap("img/5.bmp"),size=(70,60))
    bt7=bt.GenBitmapButton(total_panel,-1,Bitmap("img/6.bmp"),size=(70,60))
    bt8=bt.GenBitmapButton(total_panel,-1,Bitmap("img/-.bmp"),size=(70,60))
    bt9=bt.GenBitmapButton(total_panel,-1,Bitmap("img/7.bmp"),size=(70,60))
    bt10=bt.GenBitmapButton(total_panel,-1,Bitmap("img/8.bmp"),size=(70,60))
    bt11=bt.GenBitmapButton(total_panel,-1,Bitmap("img/9.bmp"),size=(70,60))
    bt12=bt.GenBitmapButton(total_panel,-1,Bitmap("img/mul.bmp"),size=(70,60))
    bt13=bt.GenBitmapButton(total_panel,-1,Bitmap("img/0.bmp"),size=(70,60))
    bt14=bt.GenBitmapButton(total_panel,-1,Bitmap("img/=.bmp"),size=(70,60))
    bt15=bt.GenBitmapButton(total_panel,-1,Bitmap("img/clr.bmp"),size=(70,60))
    bt16=bt.GenBitmapButton(total_panel,-1,Bitmap("img/div.bmp"),size=(70,60))
    grid.Add(bt1,0,ALL)
    grid.Add(bt2,0,ALL)
    grid.Add(bt3,0,ALL)
    grid.Add(bt4,0,ALL)
    grid.Add(bt5,0,ALL)
    grid.Add(bt6,0,ALL)
    grid.Add(bt7,0,ALL)
    grid.Add(bt8,0,ALL)
    grid.Add(bt9,0,ALL)
    grid.Add(bt10,0,ALL)
    grid.Add(bt11,0,ALL)
    grid.Add(bt12,0,ALL)
    grid.Add(bt13,0,ALL)
    grid.Add(bt14,0,ALL)
    grid.Add(bt15,0,ALL)
    grid.Add(bt16,0,ALL)
    mainbox.Add(grid,0,ALL,15)
    total_panel.SetSizer(mainbox)
    total_frame.Center()
    total_frame.Show()
def order_item(e):
    samosa_value =int(samosa_input.GetValue())*int(samosa_price)
    burger_value = int(burger_input.GetValue())*int(burger_price)
    sandwich_value = int(sandwich_input.GetValue())*int(sandwich_price)
    pizza_value = int(pizza_input.GetValue())*int(pizza_price)
    dosa_value = int(dosa_input.GetValue())*int(dosa_price)
    idli_value = int(idli_input.GetValue())*int(idli_price)
    roll_value = int(roll_input.GetValue())*int(roll_price)
    momos_value = int(momos_input.GetValue())*int(momos_price)
    cutlet_value = int(cutlet_input.GetValue())*int(cutlet_price)
    sub_total=samosa_value+burger_value+sandwich_value+pizza_value+dosa_value+idli_value+roll_value+momos_value+cutlet_value
    discount=sub_total-0
    gst=sub_total*0.18
    total=sub_total+gst

    query="INSERT INTO orders(samosa,burger,sandwich,pizza,dosa,idli,roll,momos,cutlet,sub_total,discount,gst,total) value('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
        .format(samosa_value,burger_value,sandwich_value,pizza_value,dosa_value,idli_value,roll_value,momos_value,cutlet_value,sub_total,discount,gst,total)
    cursor.execute(query)
    con.commit()
    clear_tc()
def order_view(e):
    order_frame = Frame(root, title="Order View", size=(1100, 600))
    order_panel = Panel(order_frame)
    box = BoxSizer(VERTICAL)
    list = ListCtrl(order_panel, 1, style=LC_REPORT | LC_HRULES | LC_VRULES)
    list.InsertColumn(0, "Order-Id", width=60)
    list.InsertColumn(1, "Samosa",width=70)
    list.InsertColumn(2, "Burger")
    list.InsertColumn(3, "Sandwich")
    list.InsertColumn(4, "Pizza")
    list.InsertColumn(5, "Dosa")
    list.InsertColumn(6, "Idli",width=70)
    list.InsertColumn(7, "Roll")
    list.InsertColumn(8, "Momos")
    list.InsertColumn(9, "Cutlet")
    list.InsertColumn(10,"Sub Total")
    list.InsertColumn(11,"Discount")
    list.InsertColumn(12,"GST")
    list.InsertColumn(13,"Total")

    data=cursor.execute("SELECT * FROM orders")
    orders=cursor.fetchall()
    index=0
    for x in orders:
        list.InsertItem(index,str(x[0]))
        list.SetItem(index,1,str(x[1]))
        list.SetItem(index,2,str(x[2]))
        list.SetItem(index,3,str(x[3]))
        list.SetItem(index,4,str(x[4]))
        list.SetItem(index,5,str(x[5]))
        list.SetItem(index,6,str(x[6]))
        list.SetItem(index,7,str(x[7]))
        list.SetItem(index,8,str(x[8]))
        list.SetItem(index,9,str(x[9]))
        list.SetItem(index,10,str(x[10]))
        list.SetItem(index,11,str(x[11]))
        list.SetItem(index,12,str(x[12]))
        list.SetItem(index,13,str(x[13]))
        index+=1
    box.Add(list, 1, ALL | EXPAND)
    order_panel.SetSizer(box)
    order_frame.Centre()
    order_frame.Show()
def clear_tc(e=None):
    samosa_input.SetValue("0")
    burger_input.SetValue("0")
    sandwich_input.SetValue("0")
    pizza_input.SetValue("0")
    dosa_input.SetValue("0")
    idli_input.SetValue("0")
    roll_input.SetValue("0")
    momos_input.SetValue("0")
    cutlet_input.SetValue("0")
def setting(e):
    setting_frame=Frame(root,title="Setting",size=(400,500))
    setting_panel=Panel(setting_frame)
    mainbox=BoxSizer(VERTICAL)
    grid=GridSizer(2,2,0,0)
    label=StaticText(setting_panel,1,label="Change Price 👉")
    grid.Add(label,0,LEFT|TOP,40)
    label.SetFont(font1)
    change=Button(setting_panel,1,label="Change Price")
    change.Bind(EVT_BUTTON,change_price,change)
    grid.Add(change,0,TOP|CENTER,40)
    label2=StaticText(setting_panel,1,label="Change Color 👉")
    label2.SetFont(font1)
    grid.Add(label2,0,TOP|LEFT,40)
    color=ColourPickerCtrl(setting_panel,ID_SELECT_COLOR)
    def clr(e):
        c=color.GetBackgroundColour()
        panel.SetBackgroundColour(c)
    color.Bind(EVT_COLOURPICKER_CHANGED,clr,color)
    grid.Add(color,0,TOP|CENTER,40)
    mainbox.Add(grid,0,ALL|EXPAND)
    setting_panel.SetSizer(mainbox)
    setting_frame.Centre()
    setting_frame.Show()
def change_price(e):
    change = Frame(None, title="Change Price", size=(300, 400))
    change_panel = Panel(change)
    change_box = BoxSizer(VERTICAL)
    change_grid = GridSizer(11, 2, 10, 10)

    samosa = StaticText(change_panel, 1, label="Samosa")
    burger = StaticText(change_panel, 1, label="Burger")
    sandwich = StaticText(change_panel, 1, label="Sandwich")
    pizza = StaticText(change_panel, 1, label="Pizza")
    dosa = StaticText(change_panel, 1, label="Dosa")
    idli = StaticText(change_panel, 1, label="Idli")
    roll = StaticText(change_panel, 1, label="Roll")
    momos = StaticText(change_panel, 1, label="Momos")
    cutlet = StaticText(change_panel, 1, label="Cutlet")

    samosa_tc = TextCtrl(change_panel, 1)
    samosa_tc.SetValue(samosa_price)
    burger_tc = TextCtrl(change_panel, 1)
    burger_tc.SetValue(burger_price)
    sandwich_tc = TextCtrl(change_panel, 1)
    sandwich_tc.SetValue(sandwich_price)
    pizza_tc = TextCtrl(change_panel, 1)
    pizza_tc.SetValue(pizza_price)
    dosa_tc = TextCtrl(change_panel, 1)
    dosa_tc.SetValue(dosa_price)
    idli_tc = TextCtrl(change_panel, 1)
    idli_tc.SetValue(idli_price)
    roll_tc = TextCtrl(change_panel, 1)
    roll_tc.SetValue(roll_price)
    momos_tc = TextCtrl(change_panel, 1)
    momos_tc.SetValue(momos_price)
    cutlet_tc = TextCtrl(change_panel, 1)
    cutlet_tc.SetValue(cutlet_price)

    def update_price(e):
        cursor.execute("UPDATE price SET samosa='{}',burger='{}',sandwich='{}',pizza='{}',dosa='{}',idli='{}',roll='{}',momos='{}',cutlet='{}'"\
                       .format(samosa_tc.GetValue(),burger_tc.GetValue(),sandwich_tc.GetValue(),pizza_tc.GetValue(),dosa_tc.GetValue(),idli_tc.GetValue(),roll_tc.GetValue(),momos_tc.GetValue(),cutlet_tc.GetValue()))
        con.commit()
        change.SetStatusText("\tChange Successfully")
    def change_clear(e):
        samosa_tc.SetValue('')
        burger_tc.SetValue('')
        sandwich_tc.SetValue('')
        pizza_tc.SetValue('')
        dosa_tc.SetValue('')
        idli_tc.SetValue('')
        roll_tc.SetValue('')
        momos_tc.SetValue('')
        cutlet_tc.SetValue('')
        change.SetStatusText("\tClear Successfully")

    changes = Button(change_panel, 1, label="Change")
    changes.Bind(EVT_BUTTON, update_price, changes)
    clear = Button(change_panel, 1, label="Clear")
    clear.Bind(EVT_BUTTON,change_clear,clear)

    change_grid.Add(samosa, 1)
    change_grid.Add(samosa_tc, 1)
    change_grid.Add(burger, 1)
    change_grid.Add(burger_tc, 1)
    change_grid.Add(sandwich, 1)
    change_grid.Add(sandwich_tc, 1)
    change_grid.Add(pizza, 1)
    change_grid.Add(pizza_tc, 1)
    change_grid.Add(dosa, 1)
    change_grid.Add(dosa_tc, 1)
    change_grid.Add(idli, 1)
    change_grid.Add(idli_tc, 1)
    change_grid.Add(roll, 1)
    change_grid.Add(roll_tc, 1)
    change_grid.Add(momos, 1)
    change_grid.Add(momos_tc, 1)
    change_grid.Add(cutlet, 1)
    change_grid.Add(cutlet_tc, 1)
    change_grid.Add(changes, 1,TOP,10)
    change_grid.Add(clear, 1,TOP,10)

    change_box.Add(change_grid, 0, ALL | EXPAND, 30)

    change_panel.SetSizer(change_box)
    change.Center()
    change.CreateStatusBar(1)
    change.Show()
def exits(e):
    root.Close()

############################################################################################################

mainbox = BoxSizer(VERTICAL)
header = BoxSizer(HORIZONTAL)
logo = StaticBitmap(panel, 1, Bitmap("img/logo.png"))
header.Add(logo, 0, LEFT | TOP, 10)
mainbox.Add(header, 0, ALL | EXPAND)

subbox = BoxSizer(HORIZONTAL)
grid = GridSizer(9, 3, 0, 50)
font1 = Font(14, FONTFAMILY_DECORATIVE, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL)
samosa = StaticText(panel, 1, label="Samosa")
samosa.SetFont(font1)
burger = StaticText(panel, 1, label="Burger")
burger.SetFont(font1)
sandwich = StaticText(panel, 1, label="Sandwich")
sandwich.SetFont(font1)
pizza = StaticText(panel, 1, label="Pizza")
pizza.SetFont(font1)
dosa = StaticText(panel, 1, label="Dosa")
dosa.SetFont(font1)
idli = StaticText(panel, 1, label="Idli")
idli.SetFont(font1)
roll = StaticText(panel, 1, label="Roll")
roll.SetFont(font1)
momos = StaticText(panel, 1, label="Momos")
momos.SetFont(font1)
cutlet = StaticText(panel, 1, label="Cutlet")
cutlet.SetFont(font1)

font2 = Font(16, FONTFAMILY_ROMAN, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)
samosa_input = SpinCtrl(panel, 1)
samosa_input.SetFont(font2)
burger_input = SpinCtrl(panel, 1)
burger_input.SetFont(font2)
sandwich_input = SpinCtrl(panel, 1)
sandwich_input.SetFont(font2)
pizza_input = SpinCtrl(panel, 1)
pizza_input.SetFont(font2)
dosa_input = SpinCtrl(panel, 1)
dosa_input.SetFont(font2)
idli_input = SpinCtrl(panel, 1)
idli_input.SetFont(font2)
roll_input = SpinCtrl(panel, 1)
roll_input.SetFont(font2)
momos_input = SpinCtrl(panel, 1)
momos_input.SetFont(font2)
cutlet_input = SpinCtrl(panel, 1)
cutlet_input.SetFont(font2)

samosa_1= StaticText(panel, 1, label="Rs. "+samosa_price+"/pc")
samosa_1.SetBackgroundColour("green")
burger_2= StaticText(panel, 1, label="Rs. "+burger_price+"/pc")
burger_2.SetBackgroundColour("green")
sandwich_3 = StaticText(panel, 1, label="Rs. "+sandwich_price+"/pc")
sandwich_3.SetBackgroundColour("green")
pizza_4 = StaticText(panel, 1, label="Rs. "+pizza_price+"/pc")
pizza_4.SetBackgroundColour("green")
dosa_5 = StaticText(panel, 1, label="Rs. "+dosa_price+"/pc")
dosa_5.SetBackgroundColour("green")
idli_6 = StaticText(panel, 1, label="Rs. "+idli_price+"/pc")
idli_6.SetBackgroundColour("green")
roll_7 = StaticText(panel, 1, label="Rs. "+roll_price+"/pc")
roll_7.SetBackgroundColour("green")
momos_8 = StaticText(panel, 1, label="Rs. "+momos_price+"/pc")
momos_8.SetBackgroundColour("green")
cutlet_9 = StaticText(panel, 1, label="Rs. "+cutlet_price+"/pc")
cutlet_9.SetBackgroundColour("green")

grid.Add(samosa, 1, TOP, 10)
grid.Add(burger, 1, TOP, 10)
grid.Add(sandwich, 1, TOP, 10)
grid.Add(samosa_input, 1, ALL | EXPAND)
grid.Add(burger_input, 1, ALL | EXPAND)
grid.Add(sandwich_input, 1, ALL | EXPAND)
grid.Add(samosa_1, 1, TOP, 3)
grid.Add(burger_2, 1, TOP, 3)
grid.Add(sandwich_3, 1, TOP, 3)

grid.Add(pizza, 1, TOP, 10)
grid.Add(dosa, 1, TOP, 10)
grid.Add(idli, 1, TOP, 10)
grid.Add(pizza_input, 1, ALL | EXPAND)
grid.Add(dosa_input, 1, ALL | EXPAND)
grid.Add(idli_input, 1, ALL | EXPAND)
grid.Add(pizza_4, 1, TOP, 3)
grid.Add(dosa_5, 1, TOP, 3)
grid.Add(idli_6, 1, TOP, 3)

grid.Add(roll, 1, TOP, 10)
grid.Add(momos, 1, TOP, 10)
grid.Add(cutlet, 1, TOP, 10)
grid.Add(roll_input, 1, ALL | EXPAND)
grid.Add(momos_input, 1, ALL | EXPAND)
grid.Add(cutlet_input, 1, ALL | EXPAND)
grid.Add(roll_7, 1, TOP, 3)
grid.Add(momos_8, 1, TOP, 3)
grid.Add(cutlet_9, 1, TOP, 3)
subbox.Add(grid, 4, ALL | EXPAND, 50)

btngroup = GridSizer(6, 1, 10, 10)
font3 = Font(12, FONTFAMILY_DECORATIVE, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)
fg = "blue"
bg = "white"
total = bt.GenButton(panel, 1, label="TOTAL")
total.SetFont(font3)
total.SetBackgroundColour(bg)
total.SetForegroundColour(fg)
total.Bind(EVT_BUTTON,total_value,total)
order = bt.GenButton(panel, 1, label="ORDER")
order.SetFont(font3)
order.SetBackgroundColour(bg)
order.SetForegroundColour(fg)
order.Bind(EVT_BUTTON, order_item, order)
view = bt.GenButton(panel, 1, label="VIEW")
view.SetFont(font3)
view.SetBackgroundColour(bg)
view.SetForegroundColour(fg)
view.Bind(EVT_BUTTON, order_view, view)
clear = bt.GenButton(panel, 1, label="CLEAR")
clear.SetFont(font3)
clear.SetBackgroundColour(bg)
clear.SetForegroundColour(fg)
clear.Bind(EVT_BUTTON, clear_tc, clear)
settings = bt.GenButton(panel, 1, label="SETTING")
settings.SetFont(font3)
settings.SetBackgroundColour(bg)
settings.SetForegroundColour(fg)
settings.Bind(EVT_BUTTON,setting, settings)

exit = bt.GenButton(panel, 1, label="EXIT")
exit.SetFont(font3)
exit.SetBackgroundColour(bg)
exit.SetForegroundColour(fg)
exit.Bind(EVT_BUTTON,exits,exit)

btngroup.Add(total, 1, ALL | EXPAND)
btngroup.Add(order, 1, ALL | EXPAND)
btngroup.Add(view, 1, ALL | EXPAND)
btngroup.Add(clear, 1, ALL | EXPAND)
btngroup.Add(settings, 1, ALL | EXPAND)
btngroup.Add(exit, 1, ALL | EXPAND)

subbox.Add(btngroup, 1, BOTTOM | RIGHT | EXPAND, 60)
mainbox.Add(subbox, 1, ALL | EXPAND, 10)
panel.SetSizer(mainbox)
root.Maximize()
root.Center()
clear_tc()
root.Show()
app.MainLoop()
