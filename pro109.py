import pandas as pd
import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import statistics as st
import random

df=pd.read_csv("pro109.csv")

data=df["reading score"].tolist()


mean=st.mean(data)
median=st.median(data)
mode=st.mode(data)
stdev=st.stdev(data)


print("Mean : " , mean)
print("Median : " , median)
print("Mode : " , mode)
print("Stdev : " , stdev)

print("------------------------------------------")

# -------------------------------------------------------------------------------------------------

firstStdevStart , firstStdevEnd =  mean - stdev , mean + stdev

secondStdevStart , secondStdevEnd =  mean - (2 * stdev) , mean + (2 * stdev)

thirdStdevStart , thirdStdevEnd =  mean - (3 * stdev) , mean + (3 * stdev)

# -------------------------------------------------------------------------------------------------

listOfDataWithin1Stdev = [i for i in data if i>firstStdevStart and i<firstStdevEnd]

listOfDataWithin2Stdev = [i for i in data if i>secondStdevStart and i<secondStdevEnd]

listOfDataWithin3Stdev = [i for i in data if i>thirdStdevStart and i<thirdStdevEnd]

# for i in data:
#     if i > firstStdevStart and i < firstStdevEnd:
#         listOfDataWithin1Stdev.append(i)


# -------------------------------------------------------------------------------------------------

n = len(data)

a = len(listOfDataWithin1Stdev)

b = len(listOfDataWithin2Stdev)

c = len(listOfDataWithin3Stdev)

p1 = (a*100)/n

p2 = (b*100)/n

p3 = (c*100)/n


print("Percentage Of Data lying within 1 stdev : " , p1)

print("Percentage Of Data lying within 2 stdev : " , p2)

print("Percentage Of Data lying within 3 stdev : " , p3)

