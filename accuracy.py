import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import glob



path = "D:\Digital\OneDrive - Cimcon Digital\Digital Test\/13_08_2021\/13_08_2021\VBS_with_potting\Raw_with_HPF_enable\Z/"
mes_freq = [5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000]

rms = []
rms_value = []
data_list = []

for i in mes_freq:
    rms_value.clear()
    data = pd.read_csv(path + str(i) + ".txt", skiprows=[0], sep =",",encoding='latin1')
    print(path + str(i) + ".txt")
    data.columns = ["X_LSB", "Y_LSB", "Z_LSB", "X_mg", "Y_mg", "Z_mg"]
    # del data["a"]
    
    for j in data:
        print(j)
        data_list = data[j].to_list()
        
        if(j == "X_LSB" or j == "Y_LSB" or j == "Z_LSB"):
            for k in range(len(data_list)):
                data_list[k] = (((data_list[k] * 0.122) / 1000) ** 2)
            value = np.mean(data_list)
            print("Mean: ", value)
            rms_v = np.sqrt(value)
            print("Sqrt: ", rms_v)
        else:
            for k in range(len(data_list)):
                data_list[k] = ((data_list[k] / 1000) ** 2)
            value = np.mean(data_list)
            print("Mean: ", value)
            rms_v = np.sqrt(value)
            print("Sqrt: ", rms_v)
                
#         value = np.sqrt(value)
        data_list.clear()
        rms_value.append(rms_v)
        
    print(rms_value)
    rms.append(rms_value)