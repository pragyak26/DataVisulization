import pandas as pd
import json
import re

#
# pcap_data = pd.read_csv(r"C:\Users\pragy\PycharmProjects\Assignment3_dv\business_dynamics.csv")
# # pandas.read_csv(r"C:\Users\DeePak\Desktop\myac.csv")
# dataframe = pcap_data
# print(dataframe)
#


import pandas as pd
from pandas_profiling import profile_report, ProfileReport

df=pd.read_csv('business_dynamics.csv')

print(df)

profile=ProfileReport(df)
profile.to_file(output_file="busines_dyn.html")