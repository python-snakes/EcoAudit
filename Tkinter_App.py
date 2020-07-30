########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
#                                                 Patinoire Rossens
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################



########################################################################################################################
#                                                   Essentials
########################################################################################################################

### Imports
import tkinter as tk
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor
import os
os.environ['MATPLOTLIBDATA'] =fr"C:/Users/{os.getlogin()}\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\matplotlib\mpl-data"

from os import path
import calendar
from datetime import datetime
import datetime as dt
import matplotlib.ticker as ticker
from matplotlib import dates
from PIL import ImageTk, Image
import PIL
from reportlab.pdfgen import canvas as pdfcanvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table , TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import math
import time
import calendar
import matplotlib.font_manager

### Need root to work on
root=tk.Tk()



########################################################################################################################
#                                                   Global Variables
########################################################################################################################

# Entire Dataframes
df=pd.DataFrame()
df_2=pd.DataFrame()
df_3=pd.DataFrame()
df_4=pd.DataFrame()
df_5=pd.DataFrame()
df_6=pd.DataFrame()

EER=2.2
# Dataframes of 1 Device
df_for_Dev_1=pd.DataFrame()
df_for_Dev_2=pd.DataFrame()
df_for_Dev_3=pd.DataFrame()
# Filenames
filename_1=""
filename_2=""
filename_3=""
filename_4=""
filename_5=""
filename_6=""

def drawRuler():
    pdf.drawString(100,810,"x100")
    pdf.drawString(200,810,"x200")
    pdf.drawString(300,810,"x300")
    pdf.drawString(400,810,"x400")
    pdf.drawString(500,810,"x500")


    pdf.drawString(10, 100, "y100")
    pdf.drawString(10, 200, "y200")
    pdf.drawString(10, 300, "y300")
    pdf.drawString(10, 400, "y400")
    pdf.drawString(10, 500, "y500")
    pdf.drawString(10, 600, "y600")
    pdf.drawString(10, 700, "y700")
    pdf.drawString(10, 800, "y800")

## Data frame indexing by device

Dev_00_index=[0,1,2,3,53]       # T toit, Hum toit, Pt.Rosée toit       Plaf Est Haut
Dev_01_index=[0,4,5,6,53]       # T toit, Hum toit, Pt.Rosée toit       Plaf Est Milieu
Dev_02_index=[0,7,8,9,53]       # T toit, Hum toit, Pt.Rosée toit       Plaf Est Bas
Dev_03_index=[0,10,11,12,53]    # T toit, Hum toit, Pt.Rosée toit       Plaf Ouest Haut
Dev_04_index=[0,13,14,15,53]    # T toit, Hum toit, Pt.Rosée toit       Plaf Ouest Milieu
Dev_05_index=[0,16,17,18,53]    # T toit, Hum toit, Pt.Rosée toit        Plaf Ouest Bas
Dev_06_index=[0,19,20,21,53]    # T toit, Hum toit, Pt.Rosée toit       Filet N-E
Dev_07_index=[0,22,23,24,53]    # T toit, Hum toit, Pt.Rosée toit       Filet S-E
Dev_08_index=[0,27,53]          # T glace                               Glace Est
Dev_09_index=[0,27,53]          # T glace                               Glace Ouest
Dev_10_index=[0,27,53]          # T glace                               Reserve
Dev_11_index=[0,28,53]          # T glace                               Reserve
Dev_12_index=[0,29,30,53]       # P, E                                  P,E_1
Dev_13_index=[0,31,32,53]       # P, E                                  P,E_2
Dev_14_index=[0,33,34,35,36,37,53]       # T res, Hum res, Pression res, Pt.Rosée res   Filet S-O
Dev_15_index=[0,38,39,40,41,42,53]       # T res, Hum res, Pression res, Pt.Rosée res   Filet N-O
Dev_16_index=[0,43,44,45,46,47,53]       # T res, Hum res, Pression res, Pt.Rosée res
Dev_17_index=[0,48,49,50,51,52,53]       # T res, Hum res, Pression res, Pt.Rosée res







########################################################################################################################
#                                              Setting Up App Window
########################################################################################################################

# Setting default App geometry to Maximised Screen
Window_width = root.winfo_screenwidth()
Window_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (Window_width, Window_height))
# App Title
root.title("EcoAudit")
# App logo
root.iconbitmap(f"App_logo.ico")
# Opens window in maximised format
root.state("zoomed")







########################################################################################################################
#                                                      Tabs
########################################################################################################################

nb=ttk.Notebook(root)
nb.pack(fill = BOTH, expand=1)
ttk.Style().configure("TNotebook.Tab", foreground= "#090975")
Tab1=ttk.Frame(nb)
nb.add(Tab1,text="Graph & Audit report")
ttk.Style().configure("TNotebook", background= "Grey")
#Tab2=ttk.Frame(nb)
#nb.add(Tab2,text="Chop Data")
#Tab3=ttk.Frame(nb)
#nb.add(Tab3,text="User Manual")
Tab1_Canvas=Canvas(Tab1, width=Window_width, height=Window_height,bg="#005580")
Tab1_Canvas.place(x=0,y=0)
#Tab2_Canvas=Canvas(Tab2, width=Window_width, height=Window_height,bg="#005580")
#Tab2_Canvas.place(x=0,y=0)




########################################################################################################################
########################################################################################################################
#                                              Functions Tab 1
########################################################################################################################
########################################################################################################################

# Get Filename from User Via "Filename_Button"

########################################################################################################################
#                                           Functions Tab 1 Canvas 1
########################################################################################################################


def get_filename_1():
    global df
    global filename_1
    filename_1=root.filename= filedialog.askopenfilename( initialdir='C:' ,  title="Select file",filetypes
    =(("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    #Label(root,text=root.filename).place(x=10,y=10)
    Selected_csv_Label = Label(Canvas1_1, text=root.filename, fg="#090975", bg="Grey",borderwidth=1,relief="ridge",
                               font=("Arial", 8))
    Label1_1_3_window = Canvas1_1.create_window(5,280, anchor=NW, window=Selected_csv_Label)
    df = pd.read_csv(root.filename, sep=';', engine="python")

    Date_Label1_1_6=Label(Canvas1_1, text=df.iloc[0,0][0:10], fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
    Label1_1_6_window = Canvas1_1.create_window(55, 70, anchor=NW, window=Date_Label1_1_6)
    return filename_1

Count=0
def count():
    global Count
    Count = Count + 1
    print(Count)
    return Count



# Plot csv Data Via "Plot_csv_Button"
def mybuttonfct_csvplot_1():
    global df_for_Dev_1
    global filename_1
    # First column [Température du toit #1 (Plaf.Est-Haut) [°C]]

    plt.style.use("seaborn")
    if(len(df_for_Dev_1.columns)>4):
        if (df_for_Dev_1.iloc[:, 1]).any():
            plt.plot(df_for_Dev_1.loc[0:,"TimeStamp x"],df_for_Dev_1.iloc[0:,1],Label=clicked1_1_7.get()+" Température ambiante")
        if (df_for_Dev_1.iloc[:, 2].any()):
            plt.plot(df_for_Dev_1.loc[0:, "TimeStamp x"], df_for_Dev_1.iloc[0:, 2], Label=clicked1_1_7.get()+" Humidité")
        if (df_for_Dev_1.iloc[:, 3].any()):
                plt.plot(df_for_Dev_1.loc[0:, "TimeStamp x"], df_for_Dev_1.iloc[0:, 3], Label=clicked1_1_7.get()+" Pt. Rosée")
        plt.ylabel("Température [˚C] \n \n Humidité [% Hr]")
        if (df_for_Dev_1.iloc[:, 1].any() or df_for_Dev_1.iloc[:, 2].any() or df_for_Dev_1.iloc[:, 3].any()):
            plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
            plt.title(filename_1.rsplit('/', 1)[1])
        else:
            plt.title(filename_1.rsplit('/', 1)[1] + "\n No values")

    elif(len(df_for_Dev_1.columns)==3):
        if (df_for_Dev_1.iloc[:, 1].any()):
                plt.plot(df_for_Dev_1.loc[0:, "TimeStamp x"], df_for_Dev_1.iloc[0:, 1], Label=clicked1_1_7.get()+" Température glace")
        plt.ylabel("Température [˚C]")
        if (df_for_Dev_1.iloc[:, 1].any()):
            plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
            plt.title(filename_1.rsplit('/', 1)[1])
        else:
            plt.title(filename_1.rsplit('/', 1)[1] +"\n No values")

    elif(len(df_for_Dev_1.columns)==4):
        if (df_for_Dev_1.iloc[:, 1].any()):
                plt.plot(df_for_Dev_1.loc[0:, "TimeStamp x"], df_for_Dev_1.iloc[0:, 1], Label=clicked1_1_7.get()+" Puissance")
        if (df_for_Dev_1.iloc[:, 2].any()):
                plt.plot(df_for_Dev_1.loc[0:, "TimeStamp x"], df_for_Dev_1.iloc[0:, 2], Label=clicked1_1_7.get()+" Energie")
        plt.ylabel("Puissance [W] \n \n Energie [kWh]")
        if (df_for_Dev_1.iloc[:, 1].any() or df_for_Dev_1.iloc[:, 2].any()):
            plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
            plt.title(filename_1.rsplit('/', 1)[1])
        else:
            plt.title(filename_1.rsplit('/', 1)[1] +"\n No values")





    plt.legend()
    plt.show()

x_tick_incr=0
x_ticks = []
def create_x_axis_ticks(df_for_Dev_1):
    global x_tick_incr, x_ticks
    x_ticks.append(df_for_Dev_1.iloc[x_tick_incr,0][11:16])
    x_tick_incr += 12
    return x_ticks
def go_to_x_axis_ticks(df_for_Dev_1):
    for x in range(int(len(df_for_Dev_1)/12)):
        create_x_axis_ticks(df_for_Dev_1)
    return x_ticks
### Assigning data file columns to corresponding sensors ###
def Select_Sensor(MyCurrentDev):
    global df
    global df_for_Dev_1, x_ticks, x_tick_incr,Dev_00_index
    df["TimeStamp x"] = pd.to_datetime(df["Time Stamp"], dayfirst=True, yearfirst=False)
    if (clicked1_1_7.get() == "Plaf.Est-Haut"):
        df_for_Dev_1 = df.iloc[:, Dev_00_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get()== "Plaf.Est-Milieu"):
        df_for_Dev_1 = df.iloc[:, Dev_01_index]
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Plaf.Est-Bas"):
        df_for_Dev_1 = df.iloc[:, Dev_02_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Plaf.Ouest-Haut"):
        df_for_Dev_1 = df.iloc[:, Dev_03_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Plaf.Ouest-Milieu"):
        df_for_Dev_1 = df.iloc[:, Dev_04_index]
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Plaf.Ouest-Bas"):
        df_for_Dev_1 = df.iloc[:, Dev_05_index]
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Filet N-E"):
        df_for_Dev_1 = df.iloc[:, Dev_06_index]
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Filet S-E"):
        df_for_Dev_1 = df.iloc[:, Dev_07_index]
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get()== "Filet S-O"):
        df_for_Dev_1 = df.iloc[:, Dev_14_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Filet N-O"):
        df_for_Dev_1 = df.iloc[:, Dev_15_index]# No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Glace Est"):
        df_for_Dev_1 = df.iloc[:, Dev_10_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "Glace Ouest"):
        df_for_Dev_1 = df.iloc[:, Dev_09_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "P,E_1"):
        df_for_Dev_1 = df.iloc[:, Dev_12_index] # No Val
        x_ticks=[]
        x_tick_incr=0
    elif (clicked1_1_7.get() == "P,E_2"):
        df_for_Dev_1 = df.iloc[:, Dev_13_index] # No Val
        x_ticks=[]
        x_tick_incr=0

    return df_for_Dev_1, x_ticks


def Pdf_Report_Day():
    return







########################################################################################################################
#                                         Functions Tab 1 Canvas 2
########################################################################################################################

def get_filename_2():
    global df_2
    global filename_2
    filename_2=root.filename= filedialog.askopenfilename( initialdir='C:' ,  title="Select file",filetypes
    =(("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    #Label(root,text=root.filename).place(x=10,y=10)
    Selected_csv_Label_2 = Label(Canvas1_2, text=root.filename, fg="#090975", bg="Grey",borderwidth=1,relief="ridge",
                              font=("Arial", 8))
    Label1_2_3_window = Canvas1_2.create_window(5, 280, anchor=NW, window=Selected_csv_Label_2)
    df_2 = pd.read_csv(root.filename, sep=';', engine="python")
    Date_Label1_2_6=Label(Canvas1_2, text=df_2.iloc[0,0][0:10], fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
    Label1_2_6_window = Canvas1_2.create_window(55, 70, anchor=NW, window=Date_Label1_2_6)


    return filename_2

# Plot csv Data Via "Plot_csv_Button"
def mybuttonfct_csvplot_2():
    global df_for_Dev_2, filename_2, Dev_2

    plt.style.use("seaborn")


    if (len(df_for_Dev_2.columns)>4):
        if (df_for_Dev_2.iloc[:,1]).any():
            plt.plot(df_for_Dev_2.loc[0:,"TimeStamp x"],df_for_Dev_2.iloc[0:,1],Label= clicked1_2_7.get() +" Température")
        if (df_for_Dev_2.iloc[:, 2]).any():
            plt.plot(df_for_Dev_2.loc[0:,"TimeStamp x"], df_for_Dev_2.iloc[0:, 2], Label= clicked1_2_7.get() +" Humidité")
        if (df_for_Dev_2.iloc[:, 3]).any():
            plt.plot(df_for_Dev_2.loc[0:, "TimeStamp x"], df_for_Dev_2.iloc[0:, 3],Label=clicked1_2_7.get() + " Pt. Rosée")

    elif(len(df_for_Dev_2.columns)==3):
        if (df_for_Dev_2.iloc[:, 1]).any():
            plt.plot(df_for_Dev_2.loc[0:,"TimeStamp x"], df_for_Dev_2.iloc[0:, 1], Label= clicked1_2_7.get() +" Température glace")
    elif (len(df_for_Dev_2.columns) == 4):
        if (df_for_Dev_2.iloc[:,1]).any():
            plt.plot(df_for_Dev_2.loc[0:,"TimeStamp x"], df_for_Dev_2.iloc[0:, 1], Label= clicked1_2_7.get() +" Puissance")
        if (df_for_Dev_2.iloc[:, 2]).any():
            plt.plot(df_for_Dev_2.loc[0:, "TimeStamp x"], df_for_Dev_2.iloc[0:, 2],Label=clicked1_2_7.get() + " Energie")

    plt.title("Week of" + " " + str(df_for_Dev_2.loc[0, "TimeStamp x"].month)+ "_" + str(
        df_for_Dev_2.loc[0, "TimeStamp x"].day) + "_" + str(
        df_for_Dev_2.loc[0, "TimeStamp x"].year))
    #+ str(df_for_Dev_2.loc[1,"TimeStamp x"].day)+"th of " + str(calendar.month_name[df_for_Dev_2.loc[1,"TimeStamp x"].month])

    plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%a"))
    ylab=plt.ylabel("Température [˚C] \n \n Humidité [% Hr]")
    plt.legend()

    plt.tight_layout()
    plt.show()


### Assigning data file columns to corresponding sensors ###
def Select_Sensor2(MyCurrentDev):
    global df_2, df_for_Dev_2,Dev_00_index

    df_2["TimeStamp x"]=pd.to_datetime(df_2["Time Stamp"], dayfirst=True, yearfirst=False)
    if (clicked1_2_7.get() == "Plaf.Est-Haut"):
        df_for_Dev_2 = df_2.iloc[:,Dev_00_index] # No Val
    elif (clicked1_2_7.get() == "Plaf.Est-Milieu"):
        df_for_Dev_2 = df_2.iloc[:,Dev_01_index] # No Val
    elif (clicked1_2_7.get() == "Plaf.Est-Bas"):
        df_for_Dev_2 = df_2.iloc[:,Dev_02_index] # No Val
    elif (clicked1_2_7.get() == "Plaf.Ouest-Haut"):
        df_for_Dev_2 = df_2.iloc[:,Dev_03_index] # No Val
    elif (clicked1_2_7.get() == "Plaf.Ouest-Milieu"):
        df_for_Dev_2 = df_2.iloc[:,Dev_04_index]
    elif (clicked1_2_7.get() == "Plaf.Ouest-Bas"):
        df_for_Dev_2 = df_2.iloc[:,Dev_05_index]
    elif (clicked1_2_7.get() == "Filet N-E"):
        df_for_Dev_2 = df_2.iloc[:,Dev_06_index]
    elif (clicked1_2_7.get() == "Filet S-E"):
        df_for_Dev_2 = df_2.iloc[: Dev_07_index]
    elif (clicked1_2_7.get() == "Filet S-O"):
        df_for_Dev_2 = df_2.iloc[:, Dev_14_index]  # No Val
    elif (clicked1_2_7.get() == "Filet N-O"):
        df_for_Dev_2 = df_2.iloc[:, Dev_15_index] # No Val
    elif (clicked1_2_7.get() == "Glace Est"):
        df_for_Dev_2 = df_2.iloc[:, Dev_08_index]  # No Val
    elif (clicked1_2_7.get() == "Glace Ouest"):
        df_for_Dev_2 = df_2.iloc[:, Dev_09_index]
    elif (clicked1_2_7.get() == "P,E_1"):
        df_for_Dev_2 = df_2.iloc[:, Dev_12_index]
    elif (clicked1_2_7.get() == "P,E_1"):
        df_for_Dev_2 = df_2.iloc[:, Dev_13_index]

    return df_for_Dev_2



########################################################################################################################
#                                           Week Report
########################################################################################################################


def Pdf_Report_Week():


    df_2["TimeStamp x"]=pd.to_datetime(df_2["Time Stamp"], dayfirst=True, yearfirst=False)

    Entire_Energy_Delta="{:.2f}".format(df_2.iloc[-1,30]-df_2.iloc[0,30])






    data_for_Ice_temp = {'TS': df_2["TimeStamp x"], "Ice_temp": df_2.iloc[:, 27]}
    df_for_Ice_temp = pd.DataFrame(data=data_for_Ice_temp)
    df_for_Ice_temp = df_for_Ice_temp[df_for_Ice_temp['Ice_temp'] < 0]
    df_for_Ice_temp = df_for_Ice_temp[df_for_Ice_temp['Ice_temp'] > -20]

    Ranges_X = [-8, -5, -3, 0]
    Ice_temp_prctg_week_entire = df_for_Ice_temp.groupby(pd.cut(df_for_Ice_temp.Ice_temp, Ranges_X)).count()
    Ice_temp_prctg_week_out_func_entire = [Ice_temp_prctg_week_entire.loc[0, "Ice_temp"], Ice_temp_prctg_week_entire.loc[1, "Ice_temp"],
                              Ice_temp_prctg_week_entire.loc[2, "Ice_temp"]]

    def calc_my_factor(df_energy_Counter):
        global Mean_count_in_func ,Mean_theor_in_func,Mean_Fact_in_func,Ice_temp_prctg_week_in_func
        Mean_count_in_func = []
        Mean_theor_in_func = []
        Ai = 160
        Ac = 250
        hc = 3.41
        Fci = 0.25
        fci = 1 / ((1 / Fci) + ((1 / 0.9) - 1) + (Ac / Ai) * ((1 / 0.95) - 1))
        Boltz = 5.67E-8

        #df_energy_Counter = pd.read_csv("C:/Users\Malcolm\Desktop/AuditBox_no_2_Mesures_LORA_200720_092204.csv", sep=';',
                                       # engine="python")


        # df_energy_Counter=pd.DataFrame(df_for_Ener_fact.iloc[:,1:8])

        Energy_delta_list = [1]

        for x in range(len(df_energy_Counter) - 1):
            Energy_delta_list.append(((df_energy_Counter.iloc[x + 1, 30]) * EER - (df_energy_Counter.iloc[x, 30]) * EER))
            #                                         energie                     energie


        data_for_Ener_Delta = {'TS': df_energy_Counter["TimeStamp x"], 'Energy_delta_list': Energy_delta_list}
        df_for_Ener_Delta = pd.DataFrame(data=data_for_Ener_Delta)
        Mean_with_0_production = df_for_Ener_Delta.mean()
        df_for_Ener_Delta = df_for_Ener_Delta[df_for_Ener_Delta['Energy_delta_list'] > 0]
        Proper_index = df_for_Ener_Delta.index



        Qconv_list = []
        for x in range(len(df_energy_Counter) - 1):
            Qconv_list.append(
                (Ai * hc * (df_energy_Counter.iloc[x, 19] + 273) - Ai * hc * (df_energy_Counter.iloc[x, 27] + 273)))
                                         # Temp amb                                   Temp glace

        Pressure_1_list = []
        for x in range(len(df_energy_Counter) - 1):
            Pressure_1_list.append(
                (df_energy_Counter.iloc[x, 35] / 1000) * math.exp(12.03 - (4025 / (235 + df_energy_Counter.iloc[x, 19]))))
        #                                        Pression                                           Temp Amb

        Pressure_2_list = []
        for x in range(len(df_energy_Counter) - 1):
            Pressure_2_list.append((df_energy_Counter.iloc[x, 35] / 1000) * math.exp(
                17.391 - (6142.83 / (273.15 + df_energy_Counter.iloc[x, 27]))))
        #                                       Pression                                            Temp glace


        hd_list = []
        for x in range(len(df_energy_Counter) - 1):
            hd_list.append(
                1750 * hc * (((df_energy_Counter.iloc[x, 20]) / 100) * Pressure_1_list[x] - Pressure_2_list[x]) / (
                            df_energy_Counter.iloc[x, 19] - df_energy_Counter.iloc[x, 27]))
        #                               humidité                                                                                       #Temp amb               Temp glace


        Qcnds_list = []
        for x in range(len(df_energy_Counter) - 1):
            Qcnds_list.append(
                (Ai * hd_list[x] * df_energy_Counter.iloc[x, 19] - Ai * hd_list[x] * df_energy_Counter.iloc[x, 27]))
        #                                              Temp amb                             Temp glace


        Qrad_list = []
        for x in range(len(df_energy_Counter) - 1):
            Qrad_list.append(
                Ac * fci * Boltz * (pow(df_energy_Counter.iloc[x, 19], 4) - pow(df_energy_Counter.iloc[x, 27], 4)))
        #                                                 Temp amb                             Temp glace


        Qtot_list = [1]
        for x in range(len(df_energy_Counter) - 1):
            Qtot_list.append((Qconv_list[x] + Qcnds_list[x] + Qrad_list[x]) / (12 * 1000))
        print(Qtot_list[5])
        data_for_Qtot = {'TS': df_energy_Counter["TimeStamp x"], 'Qtot_list': Qtot_list}
        df_for_Qtot = pd.DataFrame(data=data_for_Qtot)
        df_for_Qtot = df_for_Qtot.reindex(index=Proper_index)
        df_for_Qtot = df_for_Qtot.reset_index(drop=True)



        energy_fact_list = []
        for x in range(len(df_for_Ener_Delta) - 1):
            energy_fact_list.append(((df_for_Qtot.iloc[x, 1] * 1.17) / (df_for_Ener_Delta.iloc[x, 1])))
        energy_fact_list.insert(0, energy_fact_list[0])



        data_for_Ener_fact = {'TS': df_for_Ener_Delta["TS"], 'energy_fact_list': energy_fact_list}
        global df_for_Ener_fact
        df_for_Ener_fact = pd.DataFrame(data=data_for_Ener_fact)
        df_for_Ener_fact = df_for_Ener_fact[df_for_Ener_fact['energy_fact_list'] < 3]
        df_for_Ener_fact = df_for_Ener_fact[df_for_Ener_fact['energy_fact_list'] > -3]


        data_for_Ice_temp_in_func = {'TS': df_energy_Counter["TimeStamp x"], "Ice_temp": df_energy_Counter.iloc[:, 27]}
        global df_for_Ice_temp_in_func
        df_for_Ice_temp_in_func = pd.DataFrame(data=data_for_Ice_temp_in_func)
        df_for_Ice_temp_in_func = df_for_Ice_temp_in_func[df_for_Ice_temp_in_func['Ice_temp'] < 0]
        df_for_Ice_temp_in_func = df_for_Ice_temp_in_func[df_for_Ice_temp_in_func['Ice_temp'] > -20]


        df_for_Qtot = df_for_Qtot[df_for_Qtot['Qtot_list'] < 8]
        df_for_Qtot = df_for_Qtot[df_for_Qtot['Qtot_list'] > 0]

        Ener_Delta_mean = df_for_Ener_Delta.sum()
        Qtot_mean = df_for_Qtot.sum()
        Ener_fact_mean = df_for_Ener_fact.mean()*100

        Ranges = [-8, -5, -3, 0]
        Ice_temp_prctg_week = df_for_Ice_temp_in_func.groupby(pd.cut(df_for_Ice_temp_in_func.Ice_temp, Ranges)).count()
        Ice_temp_prctg_week_in_func = [Ice_temp_prctg_week.loc[0, "Ice_temp"],Ice_temp_prctg_week.loc[1, "Ice_temp"],
                                  Ice_temp_prctg_week.loc[2, "Ice_temp"]]

        Mean_count_in_func = [np.float(Ener_Delta_mean)]
        Mean_theor_in_func = [np.float(Qtot_mean)]
        Mean_Fact_in_func=[np.float(Ener_fact_mean)]

        return



    ########################################################################################################################
    ######################################### Seperating days function #####################################################
    ########################################################################################################################
    Mean_count=[]
    Mean_theor=[]
    Means_fact=[]
    Ice_temp_prctg_week=[]
    Bar_Label_Week=[]
    def export_daily_csv(pdf_Day_df):

        global Means,filename_2
        nonlocal Bar_Label_Week
        pdf_Day_df["TimeStamp x"] = pd.to_datetime(pdf_Day_df["Time Stamp"], dayfirst=True, yearfirst=False)
        pdf_Days_of_year_in_df = pdf_Day_df["TimeStamp x"].dt.dayofweek

        ############################################### pdf_Day 1 #################################################################

        pdf_Day_1 = []
        pdf_Day_1_Count = 0

        def Seperate_pdf_Days_pdf_Day_1():

            nonlocal pdf_Days_of_year_in_df, pdf_Day_1, pdf_Day_1_Count
            if pdf_Days_of_year_in_df[pdf_Day_1_Count] == pdf_Days_of_year_in_df[pdf_Day_1_Count + 1]:
                pdf_Day_1.append(pdf_Days_of_year_in_df[pdf_Day_1_Count])
                pdf_Day_1_Count += 1
            return pdf_Day_1, pdf_Day_1_Count

        for x in range(len(pdf_Day_df)):
            Seperate_pdf_Days_pdf_Day_1()
        global pdf_Day_1_df

        pdf_Day_1_df = pdf_Day_df.iloc[0:len(pdf_Day_1) + 1, :]

        calc_my_factor(pdf_Day_1_df)
        Mean_count.append((Mean_count_in_func[0]))
        Mean_theor.append((Mean_theor_in_func[0]))
        Means_fact.append((Mean_Fact_in_func[0]))
        Ice_temp_prctg_week.append((Ice_temp_prctg_week_in_func))
        Bar_Label_Week.append(calendar.day_name[pdf_Day_1_df.loc[0,"TimeStamp x"].dayofweek])

        ############################################### pdf_Day 2 #################################################################

        pdf_Day_df_2 = pdf_Day_df.iloc[len(pdf_Day_1_df):len(pdf_Day_df), :]
        pdf_Day_df_2 = pdf_Day_df_2.reset_index(drop=True)
        pdf_Days_of_year_in_df_2 = pdf_Day_df_2["TimeStamp x"].dt.dayofweek
        pdf_Days_of_year_in_df_2 = pdf_Days_of_year_in_df_2.reset_index(drop=True)

        pdf_Day_2 = []
        pdf_Day_2_Count = 0

        def Seperate_pdf_Days_pdf_Day_2():
            nonlocal pdf_Days_of_year_in_df_2, pdf_Day_2, pdf_Day_2_Count
            if len(pdf_Days_of_year_in_df_2) > pdf_Day_2_Count + 1:
                if pdf_Days_of_year_in_df_2[pdf_Day_2_Count] == pdf_Days_of_year_in_df_2[pdf_Day_2_Count + 1]:
                    pdf_Day_2.append(pdf_Days_of_year_in_df_2[pdf_Day_2_Count])
                    pdf_Day_2_Count += 1

            return pdf_Day_2, pdf_Day_2_Count

        for x in range(len(pdf_Days_of_year_in_df_2)):
            Seperate_pdf_Days_pdf_Day_2()
        global pdf_Day_2_df
        pdf_Day_2_df = pdf_Day_df_2.iloc[0:len(pdf_Day_2) + 1, :]
        if len(pdf_Days_of_year_in_df_2) > pdf_Day_2_Count + 1:
            calc_my_factor(pdf_Day_2_df)
            Mean_count.append((Mean_count_in_func[0]))
            Mean_theor.append((Mean_theor_in_func[0]))
            Means_fact.append((Mean_Fact_in_func[0]))
            Bar_Label_Week.append(calendar.day_name[pdf_Day_2_df.loc[0, "TimeStamp x"].dayofweek])
        ############################################### pdf_Day 3 #################################################################

        pdf_Day_df_3 = pdf_Day_df.iloc[len(pdf_Day_1_df) + len(pdf_Day_2_df):len(pdf_Day_df), :]
        pdf_Day_df_3 = pdf_Day_df_3.reset_index(drop=True)
        pdf_Days_of_year_in_df_3 = pdf_Day_df_3["TimeStamp x"].dt.dayofweek
        pdf_Days_of_year_in_df_3 = pdf_Days_of_year_in_df_3.reset_index(drop=True)

        pdf_Day_3 = []
        pdf_Day_3_Count = 0

        def Seperate_pdf_Days_pdf_Day_3():
            nonlocal pdf_Days_of_year_in_df_3, pdf_Day_3, pdf_Day_3_Count
            if len(pdf_Days_of_year_in_df_3) > pdf_Day_3_Count + 1:
                if pdf_Days_of_year_in_df_3[pdf_Day_3_Count] == pdf_Days_of_year_in_df_3[pdf_Day_3_Count + 1]:
                    pdf_Day_3.append(pdf_Days_of_year_in_df_3[pdf_Day_3_Count])
                    pdf_Day_3_Count += 1

            return pdf_Day_3, pdf_Day_3_Count

        for x in range(len(pdf_Days_of_year_in_df_3)):
            Seperate_pdf_Days_pdf_Day_3()
        global pdf_Day_3_df
        pdf_Day_3_df = pdf_Day_df_3.iloc[0:len(pdf_Day_3) + 1, :]
        if len(pdf_Days_of_year_in_df_3) > pdf_Day_3_Count + 1:
            calc_my_factor(pdf_Day_3_df)
            Mean_count.append((Mean_count_in_func[0]))
            Mean_theor.append((Mean_theor_in_func[0]))
            Means_fact.append((Mean_Fact_in_func[0]))
            Bar_Label_Week.append(calendar.day_name[pdf_Day_3_df.loc[0, "TimeStamp x"].dayofweek])
        ############################################### pdf_Day 4 #################################################################

        pdf_Day_df_4 = pdf_Day_df.iloc[len(pdf_Day_1_df) + len(pdf_Day_2_df)+ len(pdf_Day_3_df):len(pdf_Day_df), :]
        pdf_Day_df_4 = pdf_Day_df_4.reset_index(drop=True)
        pdf_Days_of_year_in_df_4 = pdf_Day_df_4["TimeStamp x"].dt.dayofweek
        pdf_Days_of_year_in_df_4 = pdf_Days_of_year_in_df_4.reset_index(drop=True)

        pdf_Day_4 = []
        pdf_Day_4_Count = 0

        def Seperate_pdf_Days_pdf_Day_4():
            nonlocal pdf_Days_of_year_in_df_4, pdf_Day_4, pdf_Day_4_Count
            if len(pdf_Days_of_year_in_df_4) > pdf_Day_4_Count + 1:
                if pdf_Days_of_year_in_df_4[pdf_Day_4_Count] == pdf_Days_of_year_in_df_4[pdf_Day_4_Count + 1]:
                    pdf_Day_4.append(pdf_Days_of_year_in_df_4[pdf_Day_4_Count])
                    pdf_Day_4_Count += 1

            return pdf_Day_4, pdf_Day_4_Count

        for x in range(len(pdf_Days_of_year_in_df_4)):
            Seperate_pdf_Days_pdf_Day_4()
        global pdf_Day_4_df
        pdf_Day_4_df = pdf_Day_df_4.iloc[0:len(pdf_Day_4) + 1, :]
        if len(pdf_Days_of_year_in_df_4) > pdf_Day_4_Count + 1:
            calc_my_factor(pdf_Day_4_df)
            Mean_count.append((Mean_count_in_func[0]))
            Mean_theor.append((Mean_theor_in_func[0]))
            Means_fact.append((Mean_Fact_in_func[0]))
            Bar_Label_Week.append(calendar.day_name[pdf_Day_4_df.loc[0, "TimeStamp x"].dayofweek])
        ############################################### pdf_Day 5 #################################################################

        pdf_Day_df_5 = pdf_Day_df.iloc[len(pdf_Day_1_df) + len(pdf_Day_2_df)+ len(pdf_Day_3_df)+ len(pdf_Day_4_df):len(pdf_Day_df), :]
        pdf_Day_df_5 = pdf_Day_df_5.reset_index(drop=True)
        pdf_Days_of_year_in_df_5 = pdf_Day_df_5["TimeStamp x"].dt.dayofweek
        pdf_Days_of_year_in_df_5 = pdf_Days_of_year_in_df_5.reset_index(drop=True)

        pdf_Day_5 = []
        pdf_Day_5_Count = 0

        def Seperate_pdf_Days_pdf_Day_5():
            nonlocal pdf_Days_of_year_in_df_5, pdf_Day_5, pdf_Day_5_Count
            if len(pdf_Days_of_year_in_df_5) > pdf_Day_5_Count + 1:
                if pdf_Days_of_year_in_df_5[pdf_Day_5_Count] == pdf_Days_of_year_in_df_5[pdf_Day_5_Count + 1]:
                    pdf_Day_5.append(pdf_Days_of_year_in_df_5[pdf_Day_5_Count])
                    pdf_Day_5_Count += 1

            return pdf_Day_5, pdf_Day_5_Count

        for x in range(len(pdf_Days_of_year_in_df_5)):
            Seperate_pdf_Days_pdf_Day_5()
        global pdf_Day_5_df
        pdf_Day_5_df = pdf_Day_df_5.iloc[0:len(pdf_Day_5) + 1, :]
        if len(pdf_Days_of_year_in_df_5) > pdf_Day_5_Count + 1:
            calc_my_factor(pdf_Day_5_df)
            Mean_count.append((Mean_count_in_func[0]))
            Mean_theor.append((Mean_theor_in_func[0]))
            Means_fact.append((Mean_Fact_in_func[0]))
            Bar_Label_Week.append(calendar.day_name[pdf_Day_5_df.loc[0, "TimeStamp x"].dayofweek])
        ############################################### pdf_Day6 #################################################################

        pdf_Day_df_6 = pdf_Day_df.iloc[len(pdf_Day_1_df) + len(pdf_Day_2_df)+ len(pdf_Day_3_df)+ len(pdf_Day_4_df)+
                                       len(pdf_Day_5_df):len(pdf_Day_df), :]
        pdf_Day_df_6 = pdf_Day_df_6.reset_index(drop=True)
        pdf_Days_of_year_in_df_6 = pdf_Day_df_6["TimeStamp x"].dt.dayofweek
        pdf_Days_of_year_in_df_6 = pdf_Days_of_year_in_df_6.reset_index(drop=True)

        pdf_Day_6 = []
        pdf_Day_6_Count = 0

        def Seperate_pdf_Days_pdf_Day_6():
            nonlocal pdf_Days_of_year_in_df_6, pdf_Day_6, pdf_Day_6_Count
            if len(pdf_Days_of_year_in_df_6) > pdf_Day_6_Count + 1:
                if pdf_Days_of_year_in_df_6[pdf_Day_6_Count] == pdf_Days_of_year_in_df_6[pdf_Day_6_Count + 1]:
                    pdf_Day_6.append(pdf_Days_of_year_in_df_6[pdf_Day_6_Count])
                    pdf_Day_6_Count += 1

            return pdf_Day_6, pdf_Day_6_Count

        for x in range(len(pdf_Days_of_year_in_df_6)):
            Seperate_pdf_Days_pdf_Day_6()
        global pdf_Day_6_df
        pdf_Day_6_df = pdf_Day_df_6.iloc[0:len(pdf_Day_6) + 1, :]

        if len(pdf_Days_of_year_in_df_6) > pdf_Day_6_Count + 1:
            calc_my_factor(pdf_Day_6_df)
            Mean_count.append((Mean_count_in_func[0]))
            Mean_theor.append((Mean_theor_in_func[0]))
            Means_fact.append((Mean_Fact_in_func[0]))
            Bar_Label_Week.append(calendar.day_name[pdf_Day_6_df.loc[0, "TimeStamp x"].dayofweek])
        return

    export_daily_csv(df_2)

    def Pdf_Report_Week():

        Mean_fact = "{:.2f}".format((df_for_Ener_fact["energy_fact_list"].mean(axis=0))*100)





        style_IND=TableStyle([
            ("BACKGROUND",(0,0),(-1,0), colors.darkblue),
            ("TEXTCOLOR",(0,0),(-1,0), colors.ghostwhite),
            ("ALIGN",(0,0),(-1,0),"CENTER"),
            ("BACKGROUND",(0,1),(-1,-1), colors.blanchedalmond),
            ("BOX",(0,0),(-1,-1),1.5, colors.black),
            ("GRID",(0,1),(-1,-1),1, colors.black),
            ("FONTSIZE",(0,0),(-1,-1),7)
        ])





        style_THP=TableStyle([
            ("BACKGROUND",(0,0),(-1,0), colors.darkblue),
            ("TEXTCOLOR",(0,0),(-1,0), colors.ghostwhite),
            ("ALIGN",(0,0),(-1,0),"CENTER"),
            ("BACKGROUND",(0,1),(-1,1), colors.blanchedalmond),
            ("BACKGROUND",(0,2),(-1,2), colors.lightsalmon),
            ("BACKGROUND",(0,3),(-1,3), colors.blanchedalmond),
            ("BOX",(0,0),(-1,-1),2, colors.black),
            ("GRID",(0,1),(-1,-1),1, colors.black),
            ("FONTSIZE",(0,0),(-1,0),8)
        ])










        #Data_THP_1=[["","Plaf.Est-Haut","Plaf.Est-Milieu","Plaf.Est-Bas","Plaf.Ouest-Haut","Plaf.Ouest-Milieu","Plaf.Ouest-Bas"],["Température [C]",Mean[0],Mean[4],Mean[8],Mean[12],Mean[16],Mean[19]],["Humidité [%Hr]",Mean[1],Mean[25],Mean[5],Mean[9],Mean[13],Mean[17]],["Pt. Rosée [C]",Mean[2],Mean[6],Mean[10],Mean[14],"x","x"]]
        #Data_THP_2=[["","Filet N-E","Filet S-E","Filet S-O","Filet N-O","Glace Est","Glace Ouest"],["Température [C]",Mean[22],Mean[25],Mean[28],Mean[30],Mean[32],Mean[34]],["Humidité [%Hr]",Mean[20],Mean[23],Mean[26],"x","x","x"],["Pt. Rosée [C]","x","x","x","x","x","x"]]


        def drawRuler():
            pdf.drawString(100,810,"x100")
            pdf.drawString(200,810,"x200")
            pdf.drawString(300,810,"x300")
            pdf.drawString(400,810,"x400")
            pdf.drawString(500,810,"x500")


            pdf.drawString(10, 100, "y100")
            pdf.drawString(10, 200, "y200")
            pdf.drawString(10, 300, "y300")
            pdf.drawString(10, 400, "y400")
            pdf.drawString(10, 500, "y500")
            pdf.drawString(10, 600, "y600")
            pdf.drawString(10, 700, "y700")
            pdf.drawString(10, 800, "y800")


        pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
        ###################################################### Variables ############################################################
        for x in range(len(Mean_count)):
            Mean_count[x]=float("{:.2f}".format(Mean_count[x]))
        for x in range(len(Mean_theor)):
            Mean_theor[x]=float("{:.2f}".format(Mean_theor[x]))
        for x in range(len(Means_fact)):
            Means_fact[x] = int(Means_fact[x])
        ###################################################### Means ############################################################
        if "TempÃƒÂ©rature du toit #1 (Dev00) [Ã‚Â°C]" in df_2.columns:
            Mean_Temp_0=float("{:.2f}".format(df_2.loc[:,"TempÃƒÂ©rature du toit #1 (Dev00) [Ã‚Â°C]"].mean()))
            Mean_Temp_1=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature du toit #2 (Dev01) [Ã‚Â°C]'].mean()))
            Mean_Temp_2=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature du toit #3 (Dev02) [Ã‚Â°C]'].mean()))
            Mean_Temp_3=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature du toit #4 (Dev03) [Ã‚Â°C]'].mean()))
            Mean_Temp_4=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature ambiante #1 (Dev04) [Ã‚Â°C]'].mean()))
            Mean_Temp_5=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature ambiante #2 (Dev05) [Ã‚Â°C]'].mean()))
            Mean_Temp_6=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature ambiante #3 (Dev06) [Ã‚Â°C]'].mean()))
            Mean_Temp_7=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature ambiante #4 (Dev07) [Ã‚Â°C]'].mean()))
            Mean_Temp_8=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature rÃƒÂ©serve #1 (Dev14) [Ã‚Â°C]'].mean()))
            Mean_Temp_9=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature rÃƒÂ©serve #2 (Dev15) [Ã‚Â°C]'].mean()))
            Mean_Temp_10=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature de glace #3 (Dev10) [Ã‚Â°C]'].mean()))
            Mean_Temp_11=float("{:.2f}".format(df_2.loc[:,'TempÃƒÂ©rature de glace #3 (Dev10) [Ã‚Â°C]'].mean()))

            Mean_Hum_0=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© du toit #1 (Dev00) [%Hr]'].mean()))
            Mean_Hum_1=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© du toit #2 (Dev01) [%Hr]'].mean()))
            Mean_Hum_2=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© du toit #3 (Dev02) [%Hr]'].mean()))
            Mean_Hum_3=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© du toit #4 (Dev03) [%Hr]'].mean()))
            Mean_Hum_4=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© ambiante #1 (Dev04) [%Hr]'].mean()))
            Mean_Hum_5=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© ambiante #2 (Dev05) [%Hr]'].mean()))
            Mean_Hum_6=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© ambiante #3 (Dev06) [%Hr]'].mean()))
            Mean_Hum_7=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© ambiante #4 (Dev07) [%Hr]'].mean()))
            Mean_Hum_8=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© rÃƒÂ©serve #1 (Dev14) [%Hr]'].mean()))
            Mean_Hum_9=float("{:.2f}".format(df_2.loc[:,'HumiditÃƒÂ© rÃƒÂ©serve #2 (Dev15) [%Hr]'].mean()))

            Mean_Pt_Ros_0=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e du toit #1 (Dev00) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_1=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e du toit #2 (Dev01) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_2=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e du toit #3 (Dev02) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_3=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e du toit #4 (Dev03) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_4=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e ambiance #1 (Dev04) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_5=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e ambiance #2 (Dev05) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_6=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e ambiance #3 (Dev06) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_7=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e ambiance #4 (Dev07) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_8=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e rÃƒÂ©serve #1 (Dev14) [Ã‚Â°C]'].mean()))
            Mean_Pt_Ros_9=float("{:.2f}".format(df_2.loc[:,'Pt de rosÃƒÂ©e rÃƒÂ©serve #2 (Dev15) [Ã‚Â°C]'].mean()))
        else:
            Mean_Temp_0 = float("{:.2f}".format(df_2.loc[:, "Température du toit #1 (Dev00) [°C]"].mean()))
            Mean_Temp_1 = float("{:.2f}".format(df_2.loc[:, 'Température du toit #2 (Dev01) [°C]'].mean()))
            Mean_Temp_2 = float("{:.2f}".format(df_2.loc[:, 'Température du toit #3 (Dev02) [°C]'].mean()))
            Mean_Temp_3 = float("{:.2f}".format(df_2.loc[:, 'Température du toit #4 (Dev03) [°C]'].mean()))
            Mean_Temp_4 = float("{:.2f}".format(df_2.loc[:, 'Température ambiante #1 (Dev04) [°C]'].mean()))
            Mean_Temp_5 = float("{:.2f}".format(df_2.loc[:, 'Température ambiante #2 (Dev05) [°C]'].mean()))
            Mean_Temp_6 = float("{:.2f}".format(df_2.loc[:, 'Température ambiante #3 (Dev06) [°C]'].mean()))
            Mean_Temp_7 = float("{:.2f}".format(df_2.loc[:, 'Température ambiante #4 (Dev07) [°C]'].mean()))
            Mean_Temp_8 = float("{:.2f}".format(df_2.loc[:, 'Température réserve #1 (Dev14) [°C]'].mean()))
            Mean_Temp_9 = float("{:.2f}".format(df_2.loc[:, 'Température réserve #2 (Dev15) [°C]'].mean()))
            Mean_Temp_10 = float("{:.2f}".format(df_2.loc[:, 'Température de glace #3 (Dev10) [°C]'].mean()))
            Mean_Temp_11 = float("{:.2f}".format(df_2.loc[:, 'Température de glace #3 (Dev10) [°C]'].mean()))

            Mean_Hum_0 = float("{:.2f}".format(df_2.loc[:, 'Humidité du toit #1 (Dev00) [%Hr]'].mean()))
            Mean_Hum_1 = float("{:.2f}".format(df_2.loc[:, 'Humidité du toit #2 (Dev01) [%Hr]'].mean()))
            Mean_Hum_2 = float("{:.2f}".format(df_2.loc[:, 'Humidité du toit #3 (Dev02) [%Hr]'].mean()))
            Mean_Hum_3 = float("{:.2f}".format(df_2.loc[:, 'Humidité du toit #4 (Dev03) [%Hr]'].mean()))
            Mean_Hum_4 = float("{:.2f}".format(df_2.loc[:, 'Humidité ambiante #1 (Dev04) [%Hr]'].mean()))
            Mean_Hum_5 = float("{:.2f}".format(df_2.loc[:, 'Humidité ambiante #2 (Dev05) [%Hr]'].mean()))
            Mean_Hum_6 = float("{:.2f}".format(df_2.loc[:, 'Humidité ambiante #3 (Dev06) [%Hr]'].mean()))
            Mean_Hum_7 = float("{:.2f}".format(df_2.loc[:, 'Humidité ambiante #4 (Dev07) [%Hr]'].mean()))
            Mean_Hum_8 = float("{:.2f}".format(df_2.loc[:, 'Humidité réserve #1 (Dev14) [%Hr]'].mean()))
            Mean_Hum_9 = float("{:.2f}".format(df_2.loc[:, 'Humidité réserve #2 (Dev15) [%Hr]'].mean()))

            Mean_Pt_Ros_0 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée du toit #1 (Dev00) [°C]'].mean()))
            Mean_Pt_Ros_1 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée du toit #2 (Dev01) [°C]'].mean()))
            Mean_Pt_Ros_2 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée du toit #3 (Dev02) [°C]'].mean()))
            Mean_Pt_Ros_3 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée du toit #4 (Dev03) [°C]'].mean()))
            Mean_Pt_Ros_4 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée ambiance #1 (Dev04) [°C]'].mean()))
            Mean_Pt_Ros_5 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée ambiance #2 (Dev05) [°C]'].mean()))
            Mean_Pt_Ros_6 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée ambiance #3 (Dev06) [°C]'].mean()))
            Mean_Pt_Ros_7 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée ambiance #4 (Dev07) [°C]'].mean()))
            Mean_Pt_Ros_8 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée réserve #1 (Dev14) [°C]'].mean()))
            Mean_Pt_Ros_9 = float("{:.2f}".format(df_2.loc[:, 'Pt de rosée réserve #2 (Dev15) [°C]'].mean()))



        LoRa_Devices=["Plaf.Est-Haut","Plaf.Est-Milieu","Plaf.Est-Bas","Plaf.Ouest-Haut","Plaf.Ouest-Milieu","Plaf.Ouest-Bas","Filet N-E","Filet S-E","Filet S-O","Filet N-O","Glace Est","Glace Ouest"]
        Data_IND_1=[["Indice fonct. [%]"],[float("{:.2f}".format(sum(Means_fact)/len(Means_fact)))]]
        Data_Energ_1 = [["Energie électrique [kWh]"], [Entire_Energy_Delta]]
        Data_THP_1 = [["Moyenne", "Plaf.Est-Haut", "Plaf.Est-Milieu", "Plaf.Est-Bas", "Plaf.Ouest-Haut", "Plaf.Ouest-Milieu",
                       "Plaf.Ouest-Bas"],
                      ["Température [C]", Mean_Temp_0, Mean_Temp_1, Mean_Temp_2, Mean_Temp_3, Mean_Temp_4, Mean_Temp_5],
                      ["Humidité [%Hr]", Mean_Hum_0, Mean_Hum_1, Mean_Hum_2, Mean_Hum_3, Mean_Hum_4, Mean_Hum_5],
                      ["Pt. Rosée [C]", Mean_Pt_Ros_0, Mean_Pt_Ros_1, Mean_Pt_Ros_2, Mean_Pt_Ros_3, Mean_Pt_Ros_4, Mean_Pt_Ros_5]]
        Data_THP_2 = [["Moyenne", "Filet N-E", "Filet S-E", "Filet S-O", "Filet N-O", "Glace Est", "Glace Ouest"],
                      ["Température [C]", Mean_Temp_6, Mean_Temp_7, Mean_Temp_8, Mean_Temp_9, Mean_Temp_10, Mean_Temp_11],
                      ["Humidité [%Hr]", Mean_Hum_6, Mean_Hum_7, Mean_Hum_8, Mean_Hum_9, "x", "x"],
                      ["Pt. Rosée [C]", Mean_Pt_Ros_6, Mean_Pt_Ros_7, Mean_Pt_Ros_8, Mean_Pt_Ros_9, "x", "x"]]

        ###################################################### Matplotlib ############################################################

        #Bar_Label_Week=[calendar.day_name[pdf_Day_1_df.loc[0,"TimeStamp x"].dayofweek],calendar.day_name[pdf_Day_2_df.loc[0,"TimeStamp x"].dayofweek],
          #         calendar.day_name[pdf_Day_3_df.loc[0,"TimeStamp x"].dayofweek],calendar.day_name[pdf_Day_4_df.loc[0,"TimeStamp x"].dayofweek],
           #        calendar.day_name[pdf_Day_5_df.loc[0,"TimeStamp x"].dayofweek],calendar.day_name[pdf_Day_6_df.loc[0,"TimeStamp x"].dayofweek]
              #     ]
        xpos = np.arange(len(Bar_Label_Week))



        #plt.plot(pdf_Day_df.loc[:, "TimeStamp x"], pdf_Day_df.iloc[:, 1], Label=" Température")
        ###################################################### fig1 ############################################################
        plt.style.use("seaborn")
        plt.xticks(xpos,Bar_Label_Week)
        plt.bar(xpos-0.2,Mean_count,label="Q comptée",width=0.4,color="#1a3aad")
        plt.bar(xpos+0.2,Mean_theor,label="Q théorique",width=0.4,color="#6f8f11")
        for i, v in enumerate(Mean_count):
            plt.text(i-.30, v/Mean_count[i]+100, Mean_count[i],color="White")
        for i, v in enumerate(Mean_theor):
            plt.text(i+.08, v/Mean_theor[i]+150, Mean_theor[i],color="White")
        for i, v in enumerate(Means_fact):
            plt.text(i-0.1, v/Means_fact[i]-50, Means_fact[i],color="green",label="label")
        plt.title("Production comptée et théorique")
        #plt.tick_params( axis='x',labelbottom=False)
        plt.ylabel("Energie thermique [kWh]")
        plt.xlabel(" \n Indice de bon fonctionnement [%]",color="green")
        #plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%d "))
        plt.legend()
        plt.savefig(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig.png")


        ###################################################### fig 2 ############################################################
        print(Ice_temp_prctg_week_in_func)
        plt.figure()
        plt.style.use("seaborn")
        _, _, autopcts =plt.pie(Ice_temp_prctg_week_out_func_entire,radius=.85,autopct="%1.1f%%",colors=["darkblue","green","orange"], textprops={'color':"w"})
        plt.legend(["Trop froid: moins de -5°C","Bonne température: entre -5 et -3 °C","Trop chaud: plus de -3°C"],loc="best")

        plt.setp(autopcts, **{'color': 'white', 'weight': 'bold', 'fontsize': 12.5})
        plt.title("Température de la glace",fontsize=18)

        plt.savefig(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig2.png")

        ###################################################### fig 3 ############################################################

        upper_red_line=[-3]*len(df_for_Ice_temp)
        lower_red_line=[-5]*len(df_for_Ice_temp)


        print(df_for_Ice_temp_in_func)
        plt.figure()
        plt.style.use("seaborn")
        plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%a"))
        plt.plot(df_for_Ice_temp["TS"],upper_red_line,color="red",label="Limite Max et Min")
        plt.plot(df_for_Ice_temp["TS"],lower_red_line,color="red")
        plt.plot(df_for_Ice_temp["TS"],df_for_Ice_temp["Ice_temp"],label="Temp. glace")
        plt.title("Qualité de glace")
        plt.ylabel("Température glace °C")
        plt.legend()
        figure=plt.gcf()
        figure.set_size_inches(12, 4)
        plt.savefig(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig3.png")






        ###################################################### Pdf ############################################################

        Mean_Calc= 50


        pdf=pdfcanvas.Canvas("pdf.pdf")
        #drawRuler()
        pdf.setTitle("Pdf Title")
        ###################################################### Logo ############################################################
        pdf.drawInlineImage(fr"Logo_Eco_Audi_2.png",230,780,width=140,height=70)
        ############################################### Title and date #########################################################
        pdf.setFont("VeraBd",25)
        pdf.drawString(120,750,"Rapport d'audit hebdomadaire ")
        pdf.setFont("VeraBd",15)
        pdf.drawString(220,710, str(df_2.loc[0, "TimeStamp x"].month)+ "_" + str(
                        df_2.loc[0, "TimeStamp x"].day) + "_" + str(
                        df_2.loc[0, "TimeStamp x"].year)+ "_"+ str(
                        calendar.day_name[df_2.loc[0, "TimeStamp x"].dayofweek]))
        ############################################### Line ###################################################################
        pdf.setLineWidth(1)
        pdf.line(15,700,580,700)
        ###############################################################################################################
        ############################################### P, E et indice ################################################################
        ###############################################################################################################

        ############################################### Sous-titre ################################################################
        pdf.setFont("VeraBd",15)
        pdf.drawString(180,670,"Statistiques hedbomadaire")
        ############################################### Line ###################################################################
        pdf.setLineWidth(0.5)
        pdf.line(80, 660, 520, 660)

        ############################################### Moyenne ind. ################################################################


        ############################################### Stat indic ################################################################
        table_IND_1 = Table(Data_IND_1)
        table_IND_1.setStyle((style_IND))
        table_IND_1.wrapOn(pdf, 100, 100)
        table_IND_1.drawOn(pdf, 460, 525)
        ############################################### Stat Energie elec ################################################################
        table_Energ_1 = Table(Data_Energ_1)
        table_Energ_1.setStyle((style_IND))
        table_Energ_1.wrapOn(pdf, 100, 100)
        table_Energ_1.drawOn(pdf, 460, 490)

        ############################################### Temp moy ################################################################

        table_T_H_P_1 = Table(Data_THP_1)
        table_T_H_P_1.setStyle((style_THP))
        table_T_H_P_1.wrapOn(pdf, 100, 100)
        table_T_H_P_1.drawOn(pdf, 50, 580)
        pdf.setFont("VeraBd", 7)
        pdf.drawString(50, 570, "x : Mesures inexistantes")
        table_T_H_P_2 = Table(Data_THP_2)
        table_T_H_P_2.setStyle(style_THP)
        table_T_H_P_2.wrapOn(pdf, 100, 100)
        table_T_H_P_2.drawOn(pdf, 50, 490)
        pdf.setFont("VeraBd", 7)
        pdf.drawString(50, 480, "x : Mesures inexistantes")
        ############################################### Sous-titre 2 ################################################################
        pdf.setFont("VeraBd", 15)
        pdf.drawString(170, 460, "Fonctionnement patinoire")
        ############################################### Line ###################################################################
        pdf.setLineWidth(0.5)
        pdf.line(80, 450, 520, 450)
        ############################################### Plot ###################################################################
        pdf.drawInlineImage(f"C:/Users/{os.getlogin()}/Desktop/pdf_fig.png", 20, 240, width=300, height=200)
        pdf.drawInlineImage(f"C:/Users/{os.getlogin()}/Desktop/pdf_fig2.png", 280, 240, width=300, height=200)
        pdf.drawImage(f"C:/Users/{os.getlogin()}/Desktop/pdf_fig3.png", 5, 100,width=600,height=120)
        ############################################### Line ###################################################################
        pdf.setLineWidth(1)
        pdf.line(15,80,580,80)
        ###################################################### Logo ############################################################
        pdf.drawInlineImage(fr"Logo_Eco_Audi_2.png",275,25,width=35,height=17.5)
        ###################################################### Page numb ############################################################
        pdf.setFont("VeraBd", 7)
        pdf.drawString(280,20,"Page 1")

        pdf.showPage()



         ############################################### Line ###################################################################
        pdf.setLineWidth(1)
        pdf.line(15,800,580,800)
        ############################################### Sous-titre 3 ################################################################
        pdf.setFont("VeraBd", 15)
        pdf.drawString(190, 750, "Emplacement capteurs")
        ############################################### Line ###################################################################
        pdf.setLineWidth(0.5)
        pdf.line(80, 740, 520, 740)
        ############################################### Sous-titre 4 ################################################################
        pdf.setFont("VeraBd", 15)
        pdf.drawString(250, 350, "Référence")
        ############################################### Line ###################################################################
        pdf.setLineWidth(0.5)
        pdf.line(80, 340, 520, 340)
        ############################################### Référence ################################################################

        pdf.setFont("VeraBd", 8)
        pdf.drawString(70, 300, filename_2)
        ############################################### Logo Emplacements ###################################################################
        #pdf.drawInlineImage(fr"Capteurs_plafond_Rossens.jpg", 40, 380, width=450, height=200)
        #pdf.drawInlineImage(fr"Capteurs_en_glace_Rossens.jpg", 10, 600, width=250, height=100)
        #pdf.drawInlineImage(fr"Compass.jpg", 280, 630, width=50, height=50, anchor='n')
        #pdf.drawInlineImage(fr"Capteurs_filets_Rossens.jpg", 350, 602, width=250, height=100)
        ############################################### Line ###################################################################
        pdf.setLineWidth(1)
        pdf.line(15,80,580,80)
        ###################################################### Logo ############################################################
        pdf.drawInlineImage(fr"Logo_Eco_Audi_2.png",275,25,width=35,height=17.5)
        ###################################################### Page numb ############################################################

        pdf.setFont("VeraBd", 7)
        pdf.drawString(280,20,"Page 2")







        #pdf.drawString(50,340,LoRa_Devices[0]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,320,LoRa_Devices[1]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,300,LoRa_Devices[2]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,280,LoRa_Devices[3]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,260,LoRa_Devices[4]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,240,LoRa_Devices[5]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,220,LoRa_Devices[6]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,200,LoRa_Devices[7]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,180,LoRa_Devices[8]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,160,LoRa_Devices[9]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,140,LoRa_Devices[10]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
        #pdf.drawString(50,120,LoRa_Devices[11]+" : "+"Temp : " + str(Mean_Calc)+"C ,"+"Hum : "+ str(Mean_Calc)+"[%Hr] ,"+"Pt. Rosée : "+ str(Mean_Calc)+"[C]")
















        pdf.save()

        os.remove(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig.png")
        os.remove(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig2.png")
        os.remove(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig3.png")

    Pdf_Report_Week()

    return



########################################################################################################################
#                                         Functions Tab 1 Canvas 3
########################################################################################################################

def get_filename_3():
    global df_3
    global filename_3
    filename_3=root.filename= filedialog.askopenfilename( initialdir='C:' ,  title="Select file",filetypes
    =(("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    #Label(root,text=root.filename).place(x=10,y=10)
    Selected_csv_Label_3 = Label(Canvas1_3, text=root.filename, fg="#090975", bg="Grey",borderwidth=1,relief="ridge",
                               font=("Arial", 8))
    Label1_3_3_window = Canvas1_3.create_window(5, 280, anchor=NW, window=Selected_csv_Label_3)
    df_3 = pd.read_csv(root.filename, sep=';', engine="python")
    return filename_3

# Plot csv Data Via "Plot_csv_Button"
def mybuttonfct_csvplot_3():
    global df_3
    global filename_3
    plt.style.use("seaborn")
    if (len(df_for_Dev_3.columns) > 4):
        if (df_for_Dev_3.iloc[:, 1]).any():
            plt.plot(df_for_Dev_3.loc[0:,"TimeStamp x"],df_for_Dev_3.iloc[0:,1],Label=clicked1_3_7.get()+" Température")
        if (df_for_Dev_3.iloc[:, 2]).any():
            plt.plot(df_for_Dev_3.loc[0:, "TimeStamp x"], df_for_Dev_3.iloc[0:, 2], Label=clicked1_3_7.get()+" Humidité")
        if (df_for_Dev_3.iloc[:, 3]).any():
            plt.plot(df_for_Dev_3.loc[0:, "TimeStamp x"], df_for_Dev_3.iloc[0:, 3], Label=clicked1_3_7.get() + " Pt. Rosée")

        plt.ylabel("Temperature [˚C] \n \n Humidity[% Hr]")

    if (len(df_for_Dev_3.columns) == 3):
        if (df_for_Dev_3.iloc[:, 1]).any():
            plt.plot(df_for_Dev_3.loc[0:, "TimeStamp x"], df_for_Dev_3.iloc[0:, 1], Label=clicked1_3_7.get()+" Température glace")

        plt.ylabel("Temperature [˚C]")

    if (len(df_for_Dev_3.columns) == 4):
        if (df_for_Dev_3.iloc[:, 1]).any():
            plt.plot(df_for_Dev_3.loc[0:, "TimeStamp x"], df_for_Dev_3.iloc[0:, 1],Label=clicked1_3_7.get() + " Puissance")
        if (df_for_Dev_3.iloc[:, 2]).any():
            plt.plot(df_for_Dev_3.loc[0:, "TimeStamp x"], df_for_Dev_3.iloc[0:, 2],Label=clicked1_3_7.get() + " Energie")

        plt.ylabel("Puissance [W] \n \n Energie [kWh]")

    plt.title(str(calendar.month_name[df_for_Dev_3.loc[1,"TimeStamp x"].month]))
    plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%d"))

    plt.legend()
    plt.show()
### Assigning data file columns to corresponding sensors ###
def Select_Sensor3(MyCurrentDev):
    global df_3
    global df_for_Dev_3
    df_3["TimeStamp x"] = pd.to_datetime(df_3["Time Stamp"], dayfirst=True, yearfirst=False)
    if (clicked1_3_7.get() == "Plaf.Est-Haut"):
        df_for_Dev_3 = df_3.iloc[:,Dev_00_index]  # No Val
    elif (clicked1_3_7.get() == "Plaf.Est-Milieu"):
        df_for_Dev_3= df_3.iloc[:,Dev_01_index]  # No Val
    elif (clicked1_3_7.get() == "Plaf.Est-Bas"):
        df_for_Dev_3 = df_3.iloc[:,Dev_02_index]  # No Val
    elif (clicked1_3_7.get() == "Plaf.Ouest-Haut"):
        df_for_Dev_3 = df_3.iloc[:,Dev_03_index]  # No Val
    elif (clicked1_3_7.get() == "Plaf.Ouest-Milieu"):
        df_for_Dev_3 = df_3.iloc[:,Dev_04_index]
    elif (clicked1_3_7.get() == "Plaf.Ouest-Bas"):
        df_for_Dev_3 = df_3.iloc[:,Dev_05_index]
    elif (clicked1_3_7.get() == "Filet N-E"):
        df_for_Dev_3 = df_3.iloc[:,Dev_06_index]
    elif (clicked1_3_7.get() == "Filet S-E"):
        df_for_Dev_3 = df_3.iloc[:,Dev_07_index]
    elif (clicked1_3_7.get() == "Filet S-O"):
        df_for_Dev_3 = df_3.iloc[:, Dev_14_index]  # No Val
    elif (clicked1_3_7.get() == "Filet N-O"):
        df_for_Dev_3 = df_3.iloc[:, Dev_15_index]  # No Val
    elif (clicked1_3_7.get() == "Glace Est"):
        df_for_Dev_3 = df_3.iloc[:, Dev_08_index]  # No Val
    elif (clicked1_3_7.get() == "Glace Ouest"):
        df_for_Dev_3 = df_3.iloc[:, Dev_09_index]  # No Val
    elif (clicked1_3_7.get() == "P,E_1"):
        df_for_Dev_3 = df_3.iloc[:, Dev_12_index]
    elif (clicked1_3_7.get() == "P,E_2"):
        df_for_Dev_3 = df_3.iloc[:, Dev_13_index]


    return df_for_Dev_3

def Pdf_Report_Month():

    pdf = pdfcanvas.Canvas("pdf.pdf")
    drawRuler()
    pdf.setFont("VeraBd", 25)
    pdf.setTitle("Pdf Title")
    pdf.drawString(120, 750, "Rapport d'audit Journalier :")
    pdf.drawString(200, 710, "02.06.2020")
    pdf.line(15, 700, 580, 700)
    pdf.drawInlineImage(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig.png", 300, 480, width=300, height=200)
    pdf.save()

    os.remove(fr"C:/Users/{os.getlogin()}/Desktop/pdf_fig.png")


########################################################################################################################
#                                              Canvases in Tab 1
########################################################################################################################

### Screen Size Guidelines : Upper left " 10,10" Upper right "1500,10" Lower left "10,720" Lower right "1500,720"

#############################################     Canvas 1_1    ##########################################################

Canvas1_1=Canvas(Tab1, width=500, height=300,bg="Grey")
Canvas1_1.place(x=10,y=10)

#############################################     Canvas 1_2    ##########################################################

Canvas1_2=Canvas(Tab1, width=500, height=300 ,bg="Grey")
Canvas1_2.place(x=515,y=10)

#############################################     Canvas 1_3    ##########################################################

Canvas1_3=Canvas(Tab1, width=500, height=300 ,bg="Grey")
Canvas1_3.place(x=1020,y=10)

#############################################     Canvas 1_4    ##########################################################

Canvas1_4=Canvas(Tab1, width=500, height=80 ,bg="Grey")
Canvas1_4.place(x=10,y=315)

#############################################     Canvas 1_5    ##########################################################

Canvas1_5=Canvas(Tab1, width=500, height=80 ,bg="Grey")
Canvas1_5.place(x=515,y=315)

#############################################     Canvas 1_6    ##########################################################

Canvas1_6=Canvas(Tab1, width=500, height=80 ,bg="Grey")
Canvas1_6.place(x=1020,y=315)

#############################################     Canvas 1_7    ##########################################################

Canvas1_7=Canvas(Tab1, width=1510, height=145 ,bg="#005580")
Canvas1_7.place(x=10,y=620)


########################################################################################################################
########################################################################################################################
#                                                    Widgets Tab 1
########################################################################################################################
########################################################################################################################


########################################################################################################################
#                                              Widgets in Canvas 1_1
########################################################################################################################


#############################################  Button 1_1_1 Get filename    ############################################

Filename_Button1_1_1=Button(Canvas1_1,text="Select file", width=17, font=("Arial", 9)
                            ,command=get_filename_1 ,bg="White",fg="#090975")
Button1_1_1_window = Canvas1_1.create_window(10, 40, anchor=NW, window=Filename_Button1_1_1)

#############################################  Button 1_1_2 Plot csv    ################################################

Plot_csv_Button1_1_2=Button(Canvas1_1,text="Plot Temp and Hum.",command=mybuttonfct_csvplot_1,bg="White",fg="#090975")
Button1_1_2_window = Canvas1_1.create_window(10,140, anchor=NW, window=Plot_csv_Button1_1_2)

                                 # Label 1_1_3 show file name is within get_filename_1()

#############################################     Label 1_1_4 Date      ################################################

Data_Date_Label1_1_4 = Label(Canvas1_1, text="Date:",width=6, fg="#090975", bg="White",borderwidth=1,
                                        relief="ridge")
Label1_1_4_window = Canvas1_1.create_window(10, 70, anchor=NW, window=Data_Date_Label1_1_4)
#############################################     Label 1_1_5 Directory      ###########################################

Currently_Selected_csv_Label1_1_5 = Label(Canvas1_1, text="Current file directory :",  fg="#090975",
                                          bg="White",borderwidth=1, relief="ridge")
Label1_1_5_window = Canvas1_1.create_window(5, 260, anchor=NW, window=Currently_Selected_csv_Label1_1_5)


                                # Label 1_1_6 Date is within get_filename_1()


#############################################  Label 1_1_7 Drop down menu      #########################################

LoRa_Devices=["Plaf.Est-Haut","Plaf.Est-Milieu","Plaf.Est-Bas","Plaf.Ouest-Haut","Plaf.Ouest-Milieu","Plaf.Ouest-Bas","Filet N-E","Filet S-E","Filet S-O","Filet N-O","Glace Est","Glace Ouest","P,E_1","P,E_2"]
clicked1_1_7= tk.StringVar(root)
clicked1_1_7.set("Select Device")
drop1_1_7=tk.OptionMenu(root,clicked1_1_7,LoRa_Devices[0],LoRa_Devices[1],LoRa_Devices[2],LoRa_Devices[3],
LoRa_Devices[4],LoRa_Devices[5],LoRa_Devices[6],LoRa_Devices[7],LoRa_Devices[8],LoRa_Devices[9],
LoRa_Devices[10],LoRa_Devices[11],LoRa_Devices[12],LoRa_Devices[13],command=Select_Sensor)
drop1_1_7_window = Canvas1_1.create_window(10, 95, anchor=NW, window=drop1_1_7)
drop1_1_7.config(width=11)
drop1_1_7.config(bg="White",fg="#090975",borderwidth=5)


#############################################  Label 1_1_8 Title for Daily Analysis      ###############################

Data_Date_Label1_1_8 = Label(Canvas1_1, text="Daily Analysis",font=("Arial", 16), fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
Label1_1_8_window = Canvas1_1.create_window(160, 5, anchor=NW, window=Data_Date_Label1_1_8)



#############################################  Button 1_1_9 Pdf export      ############################################


Pdf_Export_Button1_1_9=Button(Canvas1_1,text="Audit report", width=17, font=("Arial", 9)
                            ,command=Pdf_Report_Day ,bg="White",fg="#090975")
Button1_1_9_window = Canvas1_1.create_window(10, 180, anchor=NW, window=Pdf_Export_Button1_1_9)


########################################################################################################################
#                                              Widgets in Canvas 1_2
########################################################################################################################


#############################################  Button 1_2_1 Get filename    ############################################

Filename_Button1_2_1=Button(Canvas1_2,text="Select file", width=17, font=("Arial", 9)
                            ,command=get_filename_2,bg= "White",fg="#090975")
Button1_2_1_window = Canvas1_2.create_window(10, 40, anchor=NW, window=Filename_Button1_2_1)

#############################################  Button 1_2_2 Plot csv    ################################################

Plot_csv_Button1_2_2=Button(Canvas1_2,text="Plot Temp and Hum.",command=mybuttonfct_csvplot_2,bg="White",fg="#090975")
Button1_2_2_window = Canvas1_2.create_window(10, 140, anchor=NW, window=Plot_csv_Button1_2_2)

                                 # Label 1_2_3 show file name is within get_filename()

#############################################     Label 1_2_4 Date      ################################################

Data_Date_Label1_2_4 = Label(Canvas1_2, text="Date:",width=6, fg="#090975", bg="White",borderwidth=1,
                                        relief="ridge")
Label1_2_4_window = Canvas1_2.create_window(10, 70, anchor=NW, window=Data_Date_Label1_2_4)
#############################################     Label 1_2_5 Directory      ###########################################

Currently_Selected_csv_Label1_2_5 = Label(Canvas1_2, text="Current file directory :",  fg="#090975",
                                          bg="White",borderwidth=1, relief="ridge")
Label1_2_5_window = Canvas1_2.create_window(5, 260, anchor=NW, window=Currently_Selected_csv_Label1_2_5)






#############################################  Label 1_2_7 Drop down menu      #########################################

LoRa_Devices2=["Plaf.Est-Haut","Plaf.Est-Milieu","Plaf.Est-Bas","Plaf.Ouest-Haut","Plaf.Ouest-Milieu","Plaf.Ouest-Bas","Filet N-E","Filet S-E","Filet S-O","Filet N-O","Glace Est","Glace Ouest"]
clicked1_2_7= tk.StringVar(root)
clicked1_2_7.set("Select Device")
drop1_2_7=tk.OptionMenu(root,clicked1_2_7,LoRa_Devices2[0],LoRa_Devices2[1],LoRa_Devices2[2],LoRa_Devices2[3],
LoRa_Devices2[4],LoRa_Devices2[5],LoRa_Devices2[6],LoRa_Devices2[7],LoRa_Devices2[8],LoRa_Devices2[9],
LoRa_Devices2[10],LoRa_Devices2[11],command=Select_Sensor2)
drop1_2_7_window = Canvas1_2.create_window(10, 95, anchor=NW, window=drop1_2_7)
drop1_2_7.config(width=11)
drop1_2_7.config(bg="White",fg="#090975",borderwidth=5)



#############################################  Label 1_2_8 Title for Weekly Analysis      ##############################

Data_Date_Label1_2_8 = Label(Canvas1_2, text="Weekly Analysis",font=("Arial", 16), fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
Label1_2_8_window = Canvas1_2.create_window(160, 5, anchor=NW, window=Data_Date_Label1_2_8)


#############################################  Button 1_2_9 Pdf export      ############################################


Pdf_Export_Button1_2_9=Button(Canvas1_2,text="Audit report", width=17, font=("Arial", 9)
                            ,command= Pdf_Report_Week,bg="White",fg="#090975")
Button1_2_9_window = Canvas1_2.create_window(10, 180, anchor=NW, window=Pdf_Export_Button1_2_9)



########################################################################################################################
#                                              Widgets in Canvas 1_3
########################################################################################################################


#############################################  Button 1_3_1 Get filename    ############################################

Filename_Button1_3_1=Button(Canvas1_3,text="Select file", width=17, font=("Arial", 9)
                            ,command=get_filename_3,bg="White",fg="#090975" )
Button1_3_1_window = Canvas1_3.create_window(10, 40, anchor=NW, window=Filename_Button1_3_1)

#############################################  Button 1_3_2 Plot csv    ################################################

Plot_csv_Button1_3_2=Button(Canvas1_3,text="Plot Temp and Hum.",command=mybuttonfct_csvplot_3,bg="White",fg="#090975")
Button1_3_2_window = Canvas1_3.create_window(10, 140, anchor=NW, window=Plot_csv_Button1_3_2)

                                 # Label 1_2_3 show file name is within get_filename() line xxx

#############################################     Label 1_3_4 Date      ################################################

Data_Date_Label1_3_4 = Label(Canvas1_3, text="Date:",width=6, fg="#090975", bg="White",borderwidth=1,
                                        relief="ridge")
Label1_3_4_window = Canvas1_3.create_window(10, 70, anchor=NW, window=Data_Date_Label1_3_4)
#############################################     Label 1_3_5 Directory      ###########################################

Currently_Selected_csv_Label1_3_5 = Label(Canvas1_3, text="Current file directory:",  fg="#090975",
                                          bg="White",borderwidth=1, relief="ridge")
Label1_3_5_window = Canvas1_3.create_window(5, 260, anchor=NW, window=Currently_Selected_csv_Label1_3_5)


                                        # Label 1_3_6 Date is within get_filename_1()

#############################################  Label 1_3_7 Drop down menu      #########################################

LoRa_Devices3=["Plaf.Est-Haut","Plaf.Est-Milieu","Plaf.Est-Bas","Plaf.Ouest-Haut","Plaf.Ouest-Milieu","Plaf.Ouest-Bas","Filet N-E","Filet S-E","Filet S-O","Filet N-O","Glace Est","Glace Ouest"]
clicked1_3_7= tk.StringVar(root)
clicked1_3_7.set("Select Device")
drop1_3_7=tk.OptionMenu(root,clicked1_3_7,LoRa_Devices3[0],LoRa_Devices3[1],LoRa_Devices3[2],LoRa_Devices3[3],
LoRa_Devices3[4],LoRa_Devices3[5],LoRa_Devices3[6],LoRa_Devices3[7],LoRa_Devices3[8],LoRa_Devices3[9],
LoRa_Devices3[10],LoRa_Devices3[11],command=Select_Sensor3)
drop1_3_7_window = Canvas1_3.create_window(10, 95, anchor=NW, window=drop1_3_7)
drop1_3_7.config(width=11)
drop1_3_7.config(bg="White",fg="#090975",borderwidth=5)

#############################################  Label 1_3_8 Title for Monthly Analysis      #############################

Data_Date_Label1_3_8 = Label(Canvas1_3, text="Monthly Analysis",font=("Arial", 16), fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
Label1_3_8_window = Canvas1_3.create_window(160, 5, anchor=NW, window=Data_Date_Label1_3_8)



#############################################  Button 1_3_9 Pdf export      ############################################


Pdf_Export_Button1_3_9=Button(Canvas1_3,text="Audit report", width=17, font=("Arial", 9)
                            ,command=Pdf_Report_Month,bg="White",fg="#090975")
Button1_3_9_window = Canvas1_3.create_window(10, 180, anchor=NW, window=Pdf_Export_Button1_3_9)



########################################################################################################################
#                                              Widgets in Canvas 1_4
########################################################################################################################




########################################################################################################################
#                                              Widgets in Canvas 1_5
########################################################################################################################




########################################################################################################################
#                                              Widgets in Canvas 1_6
########################################################################################################################




########################################################################################################################
#                                              Widgets in Canvas 1_7
########################################################################################################################


#Device_Legend_Label1_7_1 = Label(Canvas1_7, text=" Legende Devices \nPlaf.Est-Haut : Sur le toit de la patinoire EST ? Plaf.Est-Milieu : "
    #                                             "Sur le toit Nord \n "
   #                               "Plaf.Est-Bas à l'intérieur OUEST"
  #                               , fg="#090975", bg="#005580",borderwidth=1,
 #                                 relief="flat",anchor="w")

#Label1_7_1_window = Canvas1_7.create_window(10, 10, anchor=NW, window=Device_Legend_Label1_7_1)



EcoAudit_Logo_Load = Image.open(fr"Logo_Eco_Audi_2.png")
EcoAudit_Logo_Load = EcoAudit_Logo_Load.resize((800, 150), Image.ANTIALIAS)
EcoAudit_Logo_Load_Tk=ImageTk.PhotoImage(EcoAudit_Logo_Load)
EcoAudit_Logo_1_7_2 = Label(Canvas1_7, image = EcoAudit_Logo_Load_Tk)
Label1_7_2_window=Canvas1_7.create_window(1120,70,window=EcoAudit_Logo_1_7_2)

########################################################################################################################
########################################################################################################################
#                                              Functions Tab 2
########################################################################################################################
########################################################################################################################


########################################################################################################################
#                                              Functions Tab 2 Canvas 1
########################################################################################################################


# Get file from user to seperate the days

df_2_1_1=pd.DataFrame()
filename_2_1_1=""

def get_filename_2_1_1():
    global df_2_1_1
    global filename_2_1_1
    filename_2_1_1=root.filename= filedialog.askopenfilename( initialdir='C:' ,  title="Select file",filetypes
    =(("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    #Label(root,text=root.filename).place(x=10,y=10)
    Selected_csv_Label_2_1_1 = Label(Canvas2_1, text=root.filename, fg="#090975", bg="Grey",borderwidth=1,relief="ridge",
                               font=("Arial", 6))
    Label2_1_1_window = Canvas2_1.create_window(280, 30, anchor=NW, window=Selected_csv_Label_2_1_1)
    df_2_1_1 = pd.read_csv(filename_2_1_1, sep=';', engine="python")

    return filename_2_1_1


########################################################################################################################
#                                              Functions Tab 2 Canvas 2
########################################################################################################################


# Get file from user to seperate the weeks

df_2_2_1=pd.DataFrame()
filename_2_2_1=""

def get_filename_2_2_1():
    global df_2_2_1
    global filename_2_2_1
    filename_2_2_1=root.filename= filedialog.askopenfilename( initialdir='C:' ,  title="Select file",filetypes
    =(("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    #Label(root,text=root.filename).place(x=10,y=10)
    Selected_csv_Label_2_2_1 = Label(Canvas2_2, text=root.filename, fg="#090975", bg="Grey",borderwidth=1,relief="ridge",
                               font=("Arial", 6))
    Label2_2_1_window = Canvas2_2.create_window(280, 30, anchor=NW, window=Selected_csv_Label_2_2_1)
    df_2_2_1 = pd.read_csv(filename_2_2_1, sep=';', engine="python")

    return filename_2_2_1 ,df_2_2_1

########################################################################################################################
#                                              Functions Tab 2 Canvas 3
########################################################################################################################


# Get file from user to seperate the weeks

df_2_3_1=pd.DataFrame()
filename_2_3_1=""

def get_filename_2_3_1():
    global df_2_3_1
    global filename_2_3_1
    filename_2_3_1=root.filename= filedialog.askopenfilename( initialdir='C:' ,  title="Select file",filetypes
    =(("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    #Label(root,text=root.filename).place(x=10,y=10)
    Selected_csv_Label_2_3_1 = Label(Canvas2_3, text=root.filename, fg="#090975", bg="Grey",borderwidth=1,relief="ridge",
                               font=("Arial", 6))
    Label2_3_1_window = Canvas2_3.create_window(280, 30, anchor=NW, window=Selected_csv_Label_2_3_1)
    df_2_3_1 = pd.read_csv(root.filename, sep=';', engine="python")

    return filename_2_3_1 ,df_2_3_1















########################################################################################################################
######################################### Seperating days function #####################################################
########################################################################################################################


def export_daily_csv(Day_df):
    Day_df["TimeStamp x"] = pd.to_datetime(Day_df["Time Stamp"], dayfirst=True, yearfirst=False)
    Days_of_year_in_df = Day_df["TimeStamp x"].dt.dayofweek

    ############################################### Day 1 #################################################################

    Day_1 = []
    Day_1_Count = 0

    def Seperate_Days_Day_1():
        nonlocal Days_of_year_in_df, Day_1, Day_1_Count
        if Days_of_year_in_df[Day_1_Count] == Days_of_year_in_df[Day_1_Count + 1]:
            Day_1.append(Days_of_year_in_df[Day_1_Count])
            Day_1_Count += 1
        return Day_1, Day_1_Count

    for x in range(len(Day_df)):
        Seperate_Days_Day_1()

    Day_1_df = Day_df.iloc[0:len(Day_1) + 1, :]

    ############################################### Day 2 #################################################################

    Day_df_2 = Day_df.iloc[len(Day_1_df):len(Day_df), :]
    Day_df_2 = Day_df_2.reset_index(drop=True)
    Days_of_year_in_df_2 = Day_df_2["TimeStamp x"].dt.dayofweek
    Days_of_year_in_df_2 = Days_of_year_in_df_2.reset_index(drop=True)

    Day_2 = []
    Day_2_Count = 0

    def Seperate_Days_Day_2():
        nonlocal Days_of_year_in_df_2, Day_2, Day_2_Count
        if len(Days_of_year_in_df_2) > Day_2_Count + 1:
            if Days_of_year_in_df_2[Day_2_Count] == Days_of_year_in_df_2[Day_2_Count + 1]:
                Day_2.append(Days_of_year_in_df_2[Day_2_Count])
                Day_2_Count += 1

        return Day_2, Day_2_Count

    for x in range(len(Days_of_year_in_df_2)):
        Seperate_Days_Day_2()

    Day_2_df = Day_df_2.iloc[0:len(Day_2) + 1, :]

    ############################################### Day 3 #################################################################

    Day_df_3 = Day_df.iloc[len(Day_1_df) + len(Day_2_df):len(Day_df), :]
    Day_df_3 = Day_df_3.reset_index(drop=True)
    Days_of_year_in_df_3 = Day_df_3["TimeStamp x"].dt.dayofweek
    Days_of_year_in_df_3 = Days_of_year_in_df_3.reset_index(drop=True)

    Day_3 = []
    Day_3_Count = 0

    def Seperate_Days_Day_3():
        nonlocal Days_of_year_in_df_3, Day_3, Day_3_Count
        if len(Days_of_year_in_df_3) > Day_3_Count + 1:
            if Days_of_year_in_df_3[Day_3_Count] == Days_of_year_in_df_3[Day_3_Count + 1]:
                Day_3.append(Days_of_year_in_df_3[Day_3_Count])
                Day_3_Count += 1

        return Day_3, Day_3_Count

    for x in range(len(Days_of_year_in_df_3)):
        Seperate_Days_Day_3()

    Day_3_df = Day_df_3.iloc[0:len(Day_3) + 1, :]

    ############################################### Day 4 #################################################################

    Day_df_4 = Day_df.iloc[len(Day_1_df) + len(Day_2_df) + len(Day_3_df):len(Day_df), :]
    Day_df_4 = Day_df_4.reset_index(drop=True)
    Days_of_year_in_df_4 = Day_df_4["TimeStamp x"].dt.dayofweek
    Days_of_year_in_df_4 = Days_of_year_in_df_4.reset_index(drop=True)

    Day_4 = []
    Day_4_Count = 0

    def Seperate_Days_Day_4():
        nonlocal Days_of_year_in_df_4, Day_4, Day_4_Count
        if len(Days_of_year_in_df_4) > Day_4_Count + 1:
            if Days_of_year_in_df_4[Day_4_Count] == Days_of_year_in_df_4[Day_4_Count + 1]:
                Day_4.append(Days_of_year_in_df_4[Day_4_Count])
                Day_4_Count += 1

        return Day_4, Day_4_Count

    for x in range(len(Days_of_year_in_df_4)):
        Seperate_Days_Day_4()

    Day_4_df = Day_df_4.iloc[0:len(Day_4) + 1, :]

    ############################################### Day 5 #################################################################

    Day_df_5 = Day_df.iloc[len(Day_1_df) + len(Day_2_df) + len(Day_3_df) + len(Day_4_df):len(Day_df), :]
    Day_df_5 = Day_df_5.reset_index(drop=True)
    Days_of_year_in_df_5 = Day_df_5["TimeStamp x"].dt.dayofweek
    Days_of_year_in_df_5 = Days_of_year_in_df_5.reset_index(drop=True)

    Day_5 = []
    Day_5_Count = 0

    def Seperate_Days_Day_5():
        nonlocal Days_of_year_in_df_5, Day_5, Day_5_Count
        if len(Days_of_year_in_df_5) > Day_5_Count + 1:
            if Days_of_year_in_df_5[Day_5_Count] == Days_of_year_in_df_5[Day_5_Count + 1]:
                Day_5.append(Days_of_year_in_df_5[Day_5_Count])
                Day_5_Count += 1

        return Day_5, Day_5_Count

    for x in range(len(Days_of_year_in_df_5)):
        Seperate_Days_Day_5()

    Day_5_df = Day_df_5.iloc[0:len(Day_5) + 1, :]

    ############################################### Day 6 #################################################################

    Day_df_6 = Day_df.iloc[
               len(Day_1_df) + len(Day_2_df) + len(Day_3_df) + len(Day_4_df) + len(Day_5_df):len(Day_df), :]
    Day_df_6 = Day_df_6.reset_index(drop=True)
    Days_of_year_in_df_6 = Day_df_6["TimeStamp x"].dt.dayofweek
    Days_of_year_in_df_6 = Days_of_year_in_df_6.reset_index(drop=True)

    Day_6 = []
    Day_6_Count = 0

    def Seperate_Days_Day_6():
        nonlocal Days_of_year_in_df_6, Day_6, Day_6_Count
        if len(Days_of_year_in_df_6) > Day_6_Count + 1:
            if Days_of_year_in_df_6[Day_6_Count] == Days_of_year_in_df_6[Day_6_Count + 1]:
                Day_6.append(Days_of_year_in_df_6[Day_6_Count])
                Day_6_Count += 1

        return Day_6, Day_6_Count

    for x in range(len(Days_of_year_in_df_6)):
        Seperate_Days_Day_6()

    Day_6_df = Day_df_6.iloc[0:len(Day_6) + 1, :]

    ############################################### Day 7 #################################################################

    Day_df_7 = Day_df.iloc[
               len(Day_1_df) + len(Day_2_df) + len(Day_3_df) + len(Day_4_df) + len(Day_5_df) + len(Day_6_df):len(
                   Day_df), :]
    Day_df_7 = Day_df_7.reset_index(drop=True)
    Days_of_year_in_df_7 = Day_df_7["TimeStamp x"].dt.dayofweek
    Days_of_year_in_df_7 = Days_of_year_in_df_7.reset_index(drop=True)

    Day_7 = []
    Day_7_Count = 0

    def Seperate_Days_Day_7():
        nonlocal Days_of_year_in_df_7, Day_7, Day_7_Count
        if len(Days_of_year_in_df_7) > Day_7_Count + 1:
            if Days_of_year_in_df_7[Day_7_Count] == Days_of_year_in_df_7[Day_7_Count + 1]:
                Day_7.append(Days_of_year_in_df_7[Day_7_Count])
                Day_7_Count += 1

        return Day_7, Day_7_Count

    for x in range(len(Days_of_year_in_df_7)):
        Seperate_Days_Day_7()

    Day_7_df = Day_df_7.iloc[0:len(Day_7) + 1, :]

    global filename_2_1_1

    if not (path.exists(f"C:/Users/{os.getlogin()}/Desktop/EcoAuditData")):
        os.makedirs(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData")

    if not (path.exists(f"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData")):
        os.makedirs(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData")

    Day_1_export_name = str(filename_2_1_1[-36:-23])+"_"  + str(Day_1_df.loc[0, "TimeStamp x"].month)+ "_" + str(
        Day_1_df.loc[0, "TimeStamp x"].day) + "_" + str(
        Day_1_df.loc[0, "TimeStamp x"].year)+ "_"+ str(
        calendar.day_name[Day_1_df.loc[0, "TimeStamp x"].dayofweek][0:2])
    Day_1_df = Day_1_df.drop(columns="TimeStamp x")
    Day_1_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_1_export_name + ".csv", index=False,
                    sep=";")

    if len(Days_of_year_in_df_2) > Day_2_Count:
        Day_2_export_name = str(filename_2_1_1[-36:-23]) + "_" + str(Day_2_df.loc[0, "TimeStamp x"].month) + "_" + str(
            Day_2_df.loc[0, "TimeStamp x"].day) + "_" + str(
            Day_2_df.loc[0, "TimeStamp x"].year) + "_" + str(
            calendar.day_name[Day_2_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Day_2_df = Day_2_df.drop(columns="TimeStamp x")
        Day_2_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_2_export_name + ".csv",
                        index=False,
                        sep=";")

    if len(Days_of_year_in_df_3) > Day_3_Count:
        Day_3_export_name = str(filename_2_1_1[-36:-23]) + "_" + str(Day_3_df.loc[0, "TimeStamp x"].month) + "_" + str(
            Day_3_df.loc[0, "TimeStamp x"].day) + "_" + str(
            Day_3_df.loc[0, "TimeStamp x"].year) + "_" + str(
            calendar.day_name[Day_3_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Day_3_df = Day_3_df.drop(columns="TimeStamp x")
        Day_3_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_3_export_name + ".csv",
                        index=False,
                        sep=";")

    if len(Days_of_year_in_df_4) > Day_4_Count:
        Day_4_export_name = str(filename_2_1_1[-36:-23]) + "_" + str(Day_4_df.loc[0, "TimeStamp x"].month) + "_" + str(
            Day_4_df.loc[0, "TimeStamp x"].day) + "_" + str(
            Day_4_df.loc[0, "TimeStamp x"].year) + "_" + str(
            calendar.day_name[Day_4_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Day_4_df = Day_4_df.drop(columns="TimeStamp x")
        Day_4_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_4_export_name + ".csv",
                        index=False,
                        sep=";")

    if len(Days_of_year_in_df_5) > Day_5_Count:
        Day_5_export_name = str(filename_2_1_1[-36:-23]) + "_" + str(Day_5_df.loc[0, "TimeStamp x"].month) + "_" + str(
            Day_5_df.loc[0, "TimeStamp x"].day) + "_" + str(
            Day_5_df.loc[0, "TimeStamp x"].year) + "_" + str(
            calendar.day_name[Day_5_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Day_5_df = Day_5_df.drop(columns="TimeStamp x")
        Day_5_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_5_export_name + ".csv",
                        index=False,
                        sep=";")

    if len(Days_of_year_in_df_6) > Day_6_Count:
        Day_6_export_name = str(filename_2_1_1[-36:-23]) + "_" + str(Day_6_df.loc[0, "TimeStamp x"].month) + "_" + str(
            Day_6_df.loc[0, "TimeStamp x"].day) + "_" + str(
            Day_6_df.loc[0, "TimeStamp x"].year) + "_" + str(
            calendar.day_name[Day_6_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Day_6_df = Day_6_df.drop(columns="TimeStamp x")
        Day_6_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_6_export_name + ".csv",
                        index=False,
                        sep=";")

    if len(Days_of_year_in_df_7) > Day_7_Count:
        Day_7_export_name = str(filename_2_1_1[-36:-23]) + "_" + str(Day_7_df.loc[0, "TimeStamp x"].month) + "_" + str(
            Day_7_df.loc[0, "TimeStamp x"].day) + "_" + str(
            Day_7_df.loc[0, "TimeStamp x"].year) + "_" + str(
            calendar.day_name[Day_7_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Day_7_df = Day_7_df.drop(columns="TimeStamp x")
        Day_7_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/DailyData/" + Day_7_export_name + ".csv",
                        index=False,
                        sep=";")

    return


########################################################################################################################
######################################### Seperating Weeks function #####################################################
########################################################################################################################



def export_weekly_csv(Week_df):
    Week_df["TimeStamp x"] = pd.to_datetime(Week_df["Time Stamp"], dayfirst=True, yearfirst=False)
    Weeks_of_year_in_df = Week_df["TimeStamp x"].dt.weekofyear


############################################### Week 1 #################################################################

    Week_1 = []
    Week_1_Count = 0
    def Seperate_Weeks_Week_1():
        nonlocal Weeks_of_year_in_df, Week_1, Week_1_Count
        if Weeks_of_year_in_df[Week_1_Count] == Weeks_of_year_in_df[Week_1_Count + 1]:
            Week_1.append(Weeks_of_year_in_df[Week_1_Count])
            Week_1_Count += 1
        return Week_1, Week_1_Count

    for x in range(len(Week_df)):
        Seperate_Weeks_Week_1()



    Week_1_df = Week_df.iloc[0:len(Week_1)+1 , :]


    ############################################### Week 2 #################################################################

    Week_df_2=Week_df.iloc[len(Week_1_df):len(Week_df),:]
    Week_df_2=Week_df_2.reset_index(drop=True)
    Weeks_of_year_in_df_2 = Week_df_2["TimeStamp x"].dt.weekofyear
    Weeks_of_year_in_df_2=Weeks_of_year_in_df_2.reset_index(drop=True)


    Week_2 = []
    Week_2_Count = 0
    def Seperate_Weeks_Week_2():
        nonlocal Weeks_of_year_in_df_2, Week_2, Week_2_Count
        if len(Weeks_of_year_in_df_2)>Week_2_Count+1:
            if Weeks_of_year_in_df_2[Week_2_Count] == Weeks_of_year_in_df_2[Week_2_Count+1]:
                Week_2.append(Weeks_of_year_in_df_2[Week_2_Count])
                Week_2_Count += 1

        return Week_2, Week_2_Count

    for x in range(len(Weeks_of_year_in_df_2)):
        Seperate_Weeks_Week_2()

    Week_2_df = Week_df_2.iloc[0:len(Week_2)+1 , :]




    ############################################### Week 3 #################################################################

    Week_df_3=Week_df.iloc[len(Week_1_df)+len(Week_2_df):len(Week_df),:]
    Week_df_3=Week_df_3.reset_index(drop=True)
    Weeks_of_year_in_df_3 = Week_df_3["TimeStamp x"].dt.weekofyear


    Week_3 = []
    Week_3_Count = 0
    def Seperate_Weeks_Week_3():
        nonlocal Weeks_of_year_in_df_3, Week_3, Week_3_Count
        if len(Weeks_of_year_in_df_3) > Week_3_Count + 1:
            if Weeks_of_year_in_df_3[Week_3_Count] == Weeks_of_year_in_df_3[Week_3_Count+1]:
                Week_3.append(Weeks_of_year_in_df_3[Week_3_Count])
                Week_3_Count += 1
        return Week_3, Week_3_Count

    for x in range(len(Week_df_3)):
        Seperate_Weeks_Week_3()

    Week_3_df = Week_df_3.iloc[0:len(Week_3)+1 , :]



    ############################################### Week 4 #################################################################


    Week_df_4=Week_df.iloc[len(Week_1_df)+len(Week_2_df)+len(Week_3_df):len(Week_df),:]
    Week_df_4=Week_df_4.reset_index(drop=True)
    Weeks_of_year_in_df_4 = Week_df_4["TimeStamp x"].dt.weekofyear


    Week_4 = []
    Week_4_Count = 0
    def Seperate_Weeks_Week_4():
        nonlocal Weeks_of_year_in_df_4, Week_4, Week_4_Count
        if len(Weeks_of_year_in_df_4) > Week_4_Count + 1:
            if Weeks_of_year_in_df_4[Week_4_Count] == Weeks_of_year_in_df_4[Week_4_Count+1]:
                Week_4.append(Weeks_of_year_in_df_4[Week_4_Count])
                Week_4_Count += 1
        return Week_4, Week_4_Count

    for x in range(len(Week_df_4)):
        Seperate_Weeks_Week_4()

    Week_4_df = Week_df_4.iloc[0:len(Week_4)+1 , :]




    ############################################### Week 5 #################################################################


    Week_df_5=Week_df.iloc[len(Week_1_df)+len(Week_2_df)+len(Week_3_df)+len(Week_4_df):len(Week_df),:]
    Week_df_5=Week_df_5.reset_index(drop=True)
    Weeks_of_year_in_df_5 = Week_df_5["TimeStamp x"].dt.weekofyear

    Week_5 = []
    Week_5_Count = 0
    def Seperate_Weeks_Week_5():
        nonlocal Weeks_of_year_in_df_5, Week_5, Week_5_Count
        if len(Weeks_of_year_in_df_5) > Week_5_Count + 1:
            if Weeks_of_year_in_df_5[Week_5_Count] == Weeks_of_year_in_df_5[Week_5_Count+1]:
                Week_5.append(Weeks_of_year_in_df_5[Week_5_Count])
                Week_5_Count += 1
        return Week_5, Week_5_Count

    for x in range(len(Week_df_5)):
        Seperate_Weeks_Week_5()

    Week_5_df = Week_df_5.iloc[0:len(Week_5)+1 , :]







    ############################################### Week 6 #################################################################


    Week_df_6=Week_df.iloc[len(Week_1_df)+len(Week_2_df)+len(Week_3_df)+len(Week_4_df)+len(Week_5_df):len(Week_df),:]
    Week_df_6=Week_df_6.reset_index(drop=True)
    Weeks_of_year_in_df_6 = Week_df_6["TimeStamp x"].dt.weekofyear

    Week_6 = []
    Week_6_Count = 0
    def Seperate_Weeks_Week_6():
        nonlocal Weeks_of_year_in_df_6, Week_6, Week_6_Count
        if len(Weeks_of_year_in_df_6) > Week_6_Count + 1:
            if Weeks_of_year_in_df_6[Week_6_Count] == Weeks_of_year_in_df_6[Week_6_Count+1]:
                Week_6.append(Weeks_of_year_in_df_6[Week_6_Count])
                Week_6_Count += 1
        return Week_6, Week_6_Count

    for x in range(len(Week_df_6)):
        Seperate_Weeks_Week_6()

    Week_6_df = Week_df_6.iloc[0:len(Week_6)+1 , :]




    ############################################### Week 7 #################################################################


    Week_df_7=Week_df.iloc[len(Week_1_df)+len(Week_2_df)+len(Week_3_df)+len(Week_4_df)+len(Week_5_df)+len(Week_6_df):len(Week_df),:]
    Week_df_7=Week_df_7.reset_index(drop=True)
    Weeks_of_year_in_df_7 = Week_df_7["TimeStamp x"].dt.weekofyear

    Week_7 = []
    Week_7_Count = 0
    def Seperate_Weeks_Week_7():
        nonlocal Weeks_of_year_in_df_7, Week_7, Week_7_Count
        if len(Weeks_of_year_in_df_7) > Week_7_Count + 1:
            if Weeks_of_year_in_df_7[Week_7_Count] == Weeks_of_year_in_df_7[Week_7_Count+1]:
                Week_7.append(Weeks_of_year_in_df_7[Week_7_Count])
                Week_7_Count += 1
        return Week_7, Week_7_Count

    for x in range(len(Week_df_7)):
        Seperate_Weeks_Week_7()

    Week_7_df = Week_df_7.iloc[0:len(Week_7)+1 , :]



    global filename_2_2_1

    if not (path.exists(f"C:/Users/{os.getlogin()}/Desktop/EcoAuditData")):
        os.makedirs(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData")


    if not (path.exists(f"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData")):
        os.makedirs(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData")

    Week_1_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_1_df.loc[0, "TimeStamp x"].month) + "_" + str(
        Week_1_df.loc[0, "TimeStamp x"].day) + "_" + str(
        Week_1_df.loc[0, "TimeStamp x"].year) + "_" + str(
        calendar.day_name[Week_1_df.loc[0, "TimeStamp x"].dayofweek][0:2])
    Week_1_df = Week_1_df.drop(columns="TimeStamp x")
    Week_1_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/" + Week_1_export_name +"(Week)" ".csv", index=False, sep=";")

    if len(Weeks_of_year_in_df_2) > Week_2_Count :
        Week_2_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_2_df.loc[0, "TimeStamp x"].month) +"_" + str(
            Week_2_df.loc[0, "TimeStamp x"].day)  + "_" + str(
            Week_2_df.loc[0, "TimeStamp x"].year)+"_" + str(
            calendar.day_name[Week_2_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Week_2_df = Week_2_df.drop(columns="TimeStamp x")
        Week_2_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/"+ Week_2_export_name +"(Week)"".csv", index=False, sep=";")

    if len(Weeks_of_year_in_df_3) > Week_3_Count :
        Week_3_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_3_df.loc[0, "TimeStamp x"].month) +"_" + str(
            Week_3_df.loc[0, "TimeStamp x"].day)  + "_" + str(
            Week_3_df.loc[0, "TimeStamp x"].year)+"_" + str(
            calendar.day_name[Week_3_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Week_3_df = Week_3_df.drop(columns="TimeStamp x")
        Week_3_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/"+ Week_3_export_name +"(Week)"".csv", index=False, sep=";")

    if len(Weeks_of_year_in_df_4) > Week_4_Count :
        Week_4_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_4_df.loc[0, "TimeStamp x"].month) +"_" + str(
            Week_4_df.loc[0, "TimeStamp x"].day)  + "_" + str(
            Week_4_df.loc[0, "TimeStamp x"].year)+"_" + str(
            calendar.day_name[Week_4_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Week_4_df = Week_4_df.drop(columns="TimeStamp x")
        Week_4_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/"+ Week_4_export_name +"(Week)"".csv", index=False, sep=";")

    if len(Weeks_of_year_in_df_5) > Week_5_Count :
        Week_5_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_5_df.loc[0, "TimeStamp x"].month) +"_" + str(
            Week_5_df.loc[0, "TimeStamp x"].day)  + "_" + str(
            Week_5_df.loc[0, "TimeStamp x"].year)+"_" + str(
            calendar.day_name[Week_5_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Week_5_df = Week_5_df.drop(columns="TimeStamp x")
        Week_5_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/"+ Week_5_export_name +"(Week)"".csv", index=False, sep=";")

    if len(Weeks_of_year_in_df_6) > Week_6_Count :
        Week_6_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_6_df.loc[0, "TimeStamp x"].month) +"_" + str(
            Week_6_df.loc[0, "TimeStamp x"].day)  + "_" + str(
            Week_6_df.loc[0, "TimeStamp x"].year)+"_" + str(
            calendar.day_name[Week_6_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Week_6_df = Week_6_df.drop(columns="TimeStamp x")
        Week_6_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/"+ Week_6_export_name +"(Week)"".csv", index=False, sep=";")

    if len(Weeks_of_year_in_df_7) > Week_7_Count :
        Week_7_export_name = str(filename_2_2_1[-27:-14]) + "_" + str(Week_7_df.loc[0, "TimeStamp x"].month) +"_" + str(
            Week_7_df.loc[0, "TimeStamp x"].day)  + "_" + str(
            Week_7_df.loc[0, "TimeStamp x"].year)+"_" + str(
            calendar.day_name[Week_7_df.loc[0, "TimeStamp x"].dayofweek][0:2])
        Week_7_df = Week_7_df.drop(columns="TimeStamp x")
        Week_7_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/WeeklyData/"+ Week_7_export_name +"(Week)"".csv", index=False, sep=";")



########################################################################################################################
######################################### Seperating Months function ###################################################
########################################################################################################################


def export_monthly_csv(Month_df):
    Month_df["TimeStamp x"] = pd.to_datetime(Month_df["Time Stamp"], dayfirst=True, yearfirst=False)
    Months_of_year_in_df = Month_df["TimeStamp x"].dt.month

    ############################################### Month 1 #################################################################

    Month_1 = []
    Month_1_Count = 0

    def Seperate_Months_Month_1(Month_df):
        nonlocal Months_of_year_in_df, Month_1, Month_1_Count
        if len(Months_of_year_in_df) > Month_1_Count + 1:
            if Months_of_year_in_df[Month_1_Count] == Months_of_year_in_df[Month_1_Count + 1]:
                Month_1.append(Months_of_year_in_df[Month_1_Count])
                Month_1_Count += 1
        return Month_1, Month_1_Count

    for x in range(len(Month_df)):
        Seperate_Months_Month_1(Month_df)

    Month_1_df = Month_df.iloc[0:len(Month_1) + 1, :]


    ############################################### Month 2 #################################################################
    Month_df_2 = Month_df.iloc[len(Month_1_df):len(Month_df), :]
    Month_df_2 = Month_df_2.reset_index(drop=True)
    Months_of_year_in_df_2 = Month_df_2["TimeStamp x"].dt.month
    Months_of_year_in_df_2 = Months_of_year_in_df_2.reset_index(drop=True)

    Month_2 = []
    Month_2_Count = 0

    def Seperate_Months_Month_2():
        nonlocal Months_of_year_in_df_2, Month_2, Month_2_Count
        if len(Months_of_year_in_df_2) > Month_2_Count + 1:
            if Months_of_year_in_df_2[Month_2_Count] == Months_of_year_in_df_2[Month_2_Count + 1]:
                Month_2.append(Months_of_year_in_df_2[Month_2_Count])
                Month_2_Count += 1
        return Month_2, Month_2_Count

    for x in range(len(Months_of_year_in_df_2)):
        Seperate_Months_Month_2()

    Month_2_df = Month_df_2.iloc[0:len(Month_2) + 1, :]


    ############################################### Month 3 #################################################################
    Month_df_3 = Month_df.iloc[len(Month_1_df) + len(Month_2_df):len(Month_df), :]
    Month_df_3 = Month_df_3.reset_index(drop=True)
    Months_of_year_in_df_3 = Month_df_3["TimeStamp x"].dt.month
    Months_of_year_in_df_3 = Months_of_year_in_df_3.reset_index(drop=True)

    Month_3 = []
    Month_3_Count = 0

    def Seperate_Months_Month_3():
        nonlocal Months_of_year_in_df_3, Month_3, Month_3_Count
        if len(Months_of_year_in_df_3) > Month_3_Count + 1:
            if Months_of_year_in_df_3[Month_3_Count] == Months_of_year_in_df_3[Month_3_Count + 1]:
                Month_3.append(Months_of_year_in_df_3[Month_3_Count])
                Month_3_Count += 1
        return Month_3, Month_3_Count

    for x in range(len(Months_of_year_in_df_3)):
        Seperate_Months_Month_3()

    Month_3_df = Month_df_3.iloc[0:len(Month_3) + 1, :]


    ############################################### Month 4 #################################################################
    Month_df_4 = Month_df.iloc[len(Month_1_df) + len(Month_2_df) + len(Month_3_df):len(Month_df), :]
    Month_df_4 = Month_df_4.reset_index(drop=True)
    Months_of_year_in_df_4 = Month_df_4["TimeStamp x"].dt.month
    Months_of_year_in_df_4 = Months_of_year_in_df_4.reset_index(drop=True)

    Month_4 = []
    Month_4_Count = 0

    def Seperate_Months_Month_4():
        nonlocal Months_of_year_in_df_4, Month_4, Month_4_Count
        if len(Months_of_year_in_df_4) > Month_4_Count + 1:
            if Months_of_year_in_df_4[Month_4_Count] == Months_of_year_in_df_4[Month_4_Count + 1]:
                Month_4.append(Months_of_year_in_df_4[Month_4_Count])
                Month_4_Count += 1
        return Month_4, Month_4_Count

    for x in range(len(Months_of_year_in_df_4)):
        Seperate_Months_Month_4()

    Month_4_df = Month_df_4.iloc[0:len(Month_4) + 1, :]


    ############################################### Month 5 #################################################################
    Month_df_5 = Month_df.iloc[len(Month_1_df) + len(Month_2_df) + len(Month_3_df) + len(Month_4_df):len(Month_df),
                 :]
    Month_df_5 = Month_df_5.reset_index(drop=True)
    Months_of_year_in_df_5 = Month_df_5["TimeStamp x"].dt.month
    Months_of_year_in_df_5 = Months_of_year_in_df_5.reset_index(drop=True)

    Month_5 = []
    Month_5_Count = 0

    def Seperate_Months_Month_5():
        nonlocal Months_of_year_in_df_5, Month_5, Month_5_Count
        if len(Months_of_year_in_df_5) > Month_5_Count + 1:
            if Months_of_year_in_df_5[Month_5_Count] == Months_of_year_in_df_5[Month_5_Count + 1]:
                Month_5.append(Months_of_year_in_df_5[Month_5_Count])
                Month_5_Count += 1
        return Month_5, Month_5_Count

    for x in range(len(Months_of_year_in_df_5)):
        Seperate_Months_Month_5()

    Month_5_df = Month_df_5.iloc[0:len(Month_5) + 1, :]


    ############################################### Month 6 #################################################################
    Month_df_6 = Month_df.iloc[
                 len(Month_1_df) + len(Month_2_df) + len(Month_3_df) + len(Month_4_df) + len(Month_5_df):len(
                     Month_df), :]
    Month_df_6 = Month_df_6.reset_index(drop=True)
    Months_of_year_in_df_6 = Month_df_6["TimeStamp x"].dt.month
    Months_of_year_in_df_6 = Months_of_year_in_df_6.reset_index(drop=True)

    Month_6 = []
    Month_6_Count = 0

    def Seperate_Months_Month_6():
        nonlocal Months_of_year_in_df_6, Month_6, Month_6_Count
        if len(Months_of_year_in_df_6) > Month_6_Count + 1:
            if Months_of_year_in_df_6[Month_6_Count] == Months_of_year_in_df_6[Month_6_Count + 1]:
                Month_6.append(Months_of_year_in_df_6[Month_6_Count])
                Month_6_Count += 1
        return Month_6, Month_6_Count

    for x in range(len(Months_of_year_in_df_6)):
        Seperate_Months_Month_6()

    Month_6_df = Month_df_6.iloc[0:len(Month_6) + 1, :]


    global filename_2_3_1




    if not (path.exists(f"C:/Users/{os.getlogin()}/Desktop/EcoAuditData")):
        os.makedirs(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData")

    if not (path.exists(f"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData")):
        os.makedirs(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData")

    Month_1_export_name=str(filename_2_3_1[-44:-30])+str(calendar.month_name[Month_1_df.loc[0,"TimeStamp x"].month])+"_"+str( Month_1_df.loc[0, "TimeStamp x"].year)
    Month_1_df = Month_1_df.drop(columns="TimeStamp x")
    Month_1_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData/" + Month_1_export_name + ".csv", index=False, sep=";")

    if len(Months_of_year_in_df_2) > Month_2_Count:
        Month_2_export_name = str(filename_2_3_1[-44:-30]) + str(
            calendar.month_name[Month_2_df.loc[0, "TimeStamp x"].month]) + "_" + str(
            Month_2_df.loc[0, "TimeStamp x"].year)
        Month_2_df = Month_2_df.drop(columns="TimeStamp x")
        Month_2_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData/" + Month_2_export_name + ".csv",
                          index=False, sep=";")

    if len(Months_of_year_in_df_3) > Month_3_Count:
        Month_3_export_name = str(filename_2_3_1[-44:-30]) + str(
            calendar.month_name[Month_3_df.loc[0, "TimeStamp x"].month]) + "_" + str(
            Month_3_df.loc[0, "TimeStamp x"].year)
        Month_3_df = Month_3_df.drop(columns="TimeStamp x")
        Month_3_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData/" + Month_3_export_name + ".csv",
                          index=False, sep=";")


    if len(Months_of_year_in_df_4) > Month_4_Count:
        Month_4_export_name = str(filename_2_3_1[-44:-30]) + str(
            calendar.month_name[Month_4_df.loc[0, "TimeStamp x"].month]) + "_" + str(
            Month_4_df.loc[0, "TimeStamp x"].year)
        Month_4_df = Month_4_df.drop(columns="TimeStamp x")
        Month_4_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData/" + Month_4_export_name + ".csv",
                          index=False, sep=";")

    if len(Months_of_year_in_df_5) > Month_5_Count:
        Month_5_export_name = str(filename_2_3_1[-44:-30]) + str(
            calendar.month_name[Month_5_df.loc[0, "TimeStamp x"].month]) + "_" + str(
            Month_5_df.loc[0, "TimeStamp x"].year)
        Month_5_df = Month_5_df.drop(columns="TimeStamp x")
        Month_5_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData/" + Month_5_export_name + ".csv",
                          index=False, sep=";")

    if len(Months_of_year_in_df_6) > Month_6_Count:
        Month_6_export_name = str(filename_2_3_1[-44:-30]) + str(
            calendar.month_name[Month_6_df.loc[0, "TimeStamp x"].month]) + "_" + str(
            Month_6_df.loc[0, "TimeStamp x"].year)
        Month_6_df = Month_6_df.drop(columns="TimeStamp x")
        Month_6_df.to_csv(fr"C:/Users/{os.getlogin()}/Desktop/EcoAuditData/MonthlyData/" + Month_6_export_name + ".csv",
                          index=False, sep=";")



    return



########################################################################################################################
#                                              Canvases in Tab 2
########################################################################################################################

### Screen Size Guidelines : Upper left " 10,10" Upper right "1500,10" Lower left "10,720" Lower right "1500,720"

#############################################     Canvas 2_1    ##########################################################

#Canvas2_1=Canvas(Tab2, width=500, height=300,bg="Grey")
#Canvas2_1.place(x=10,y=10)


#############################################     Canvas 2_2    ##########################################################

#Canvas2_2=Canvas(Tab2, width=500, height=300,bg="Grey")
#Canvas2_2.place(x=510,y=10)

#############################################     Canvas 2_3    ##########################################################

#Canvas2_3=Canvas(Tab2, width=500, height=300,bg="Grey")
#Canvas2_3.place(x=1010,y=10)



########################################################################################################################
########################################################################################################################
#                                                    Widgets Tab 2
########################################################################################################################
########################################################################################################################




########################################################################################################################
#                                              Widgets in Canvas 2_1
########################################################################################################################



#############################################  Button 2_1_1 Get filename    ############################################

Filename_Button2_1_1=Button(Canvas1_4,text="Press to select a csv file", width=17, font=("Arial", 7)
                            ,command=get_filename_2_1_1 )
Button2_1_1_window = Canvas1_4.create_window(10, 25, anchor=NW, window=Filename_Button2_1_1)



Create_daily_csv_2_1_2=Button(Canvas1_4,text="Chop",command= lambda:export_daily_csv(df_2_1_1))
Button2_1_2_window = Canvas1_4.create_window(10, 50, anchor=NW, window=Create_daily_csv_2_1_2)


#############################################  Label 2_1_3 Title    ############################################

Canvas_Title_2_1_3 = Label(Canvas1_4, text="Daily Chopping",font=("Arial", 16), fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
Label2_1_3_window = Canvas1_4.create_window(160, 5, anchor=NW, window=Canvas_Title_2_1_3)



########################################################################################################################
#                                              Widgets in Canvas 2_2
########################################################################################################################

#############################################  Button 2_2_1 Get filename    ############################################

Filename_Button2_2_1=Button(Canvas1_5,text="Press to select a csv file", width=17, font=("Arial", 7)
                            ,command=get_filename_2_2_1 )
Button2_2_1_window = Canvas1_5.create_window(10, 25, anchor=NW, window=Filename_Button2_2_1)



Create_weekly_csv_2_2_2=Button(Canvas1_5,text="Chop",command= lambda:export_weekly_csv(df_2_2_1))
Button2_2_2_window = Canvas1_5.create_window(10, 50, anchor=NW, window=Create_weekly_csv_2_2_2)

#############################################  Label 2_2_3 Title    ############################################

Canvas_Title_2_2_3 = Label(Canvas1_5, text="Weekly Chopping",font=("Arial", 16), fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
Label2_2_3_window = Canvas1_5.create_window(160, 5, anchor=NW, window=Canvas_Title_2_2_3)



########################################################################################################################
#                                              Widgets in Canvas 2_3
########################################################################################################################

#############################################  Button 2_3_1 Get filename    ############################################

Filename_Button2_3_1=Button(Canvas1_6,text="Press to select a csv file", width=17, font=("Arial", 7)
                            ,command=get_filename_2_3_1 )
Button2_3_1_window = Canvas1_6.create_window(10, 25, anchor=NW, window=Filename_Button2_3_1)



Create_monthly_csv_2_3_2=Button(Canvas1_6,text="Chop",command= lambda:export_monthly_csv(df_2_3_1))
Button2_3_2_window = Canvas1_6.create_window(10, 50, anchor=NW, window=Create_monthly_csv_2_3_2)


#############################################  Label 2_3_3 Title    ############################################

Canvas_Title_2_2_3 = Label(Canvas1_6, text="Monthly Chopping",font=("Arial", 16), fg="#090975", bg="Grey",borderwidth=1,
                                        relief="ridge")
Label2_3_3_window = Canvas1_6.create_window(160, 5, anchor=NW, window=Canvas_Title_2_2_3)




print(df)
print(df_2)


root.mainloop()