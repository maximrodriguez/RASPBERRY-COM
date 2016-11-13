# -*- coding: utf-8 -*-
# Communication Program for Arduino Rev0.1-17/09/2016
# For 2 Arduino Uno through Serial  USB

import serial   # Serial COM Library
import datetime # For Date & Time 
import time     # For delays and durations
import os       # For OS shell commands


MyDateTime = datetime.datetime(2016,1,3,8,30,20)
flag1=0
flag2=0

Data_Temp_filename="/home/max/Projects/Pi/Pi_Programs/Data/Room_temp.txt"

ser1 = serial.Serial('/dev/ttyACM0', 9600)
ser2 = serial.Serial('/dev/ttyACM1', 9600)
time.sleep(4)


while True:
    MyDateTime = datetime.datetime.now()
    second=MyDateTime.second
    minute=MyDateTime.minute
    hour=MyDateTime.hour
    if (second==0 and flag1==0):
         flag1=1
         ser1.write('5')
         Temperature= ser1.readline()
         Date= str(MyDateTime.day)+"/"+ str(MyDateTime.month)+"/"+ str(MyDateTime.year)
         Time = str(MyDateTime.hour)+":"+ str(MyDateTime.minute)+":"+ str(MyDateTime.second)
         filename="/home/max/Projects/Pi/Pi_Programs/Data/"+str(MyDateTime.year)+str(MyDateTime.month)+str(MyDateTime.day)+"_Data.txt"
         datafile=open(filename,"a")
         datafile.write(Date)
         datafile.write(",")
         datafile.write(Time)
         datafile.write(",")
         datafile.write(Temperature)
         datafile.close()
         data_Temp=open(Data_Temp_filename,"w")
         data_Temp.write(Temperature)
         data_Temp.close()
    if (second!=0 and flag1==1):
         flag1=0
    if (minute==59 and second==30 and flag2==0):
         flag2=1
         os.system("sudo -u max /home/max/Dropbox-Uploader/dropbox_uploader.sh upload "+filename+" Projets/Pi/Pi_Programs/Data")
    if (minute!=0 and flag2==1):
         flag2=0





