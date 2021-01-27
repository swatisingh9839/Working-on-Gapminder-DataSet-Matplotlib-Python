import csv
import matplotlib.pyplot as plt
from math import pi,sin

def load_csv(fileName):
    with open(fileName, newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',',quotechar='"')
        next(csv_data) # to ignore 1st row of headers
        dic = {(val[1]).lower() : list(map(float, val[3:])) for val in csv_data }
        #print(dic)
        return dic

def smooth_a(a, n):
    denominator = 2*n + 1
    listLen = len(a)
    extList = [a[0]]*listLen+a+[a[-1]]*listLen
    newList = [(sum(extList[i+listLen-n : i+listLen+n+1]))/denominator for i, x in enumerate(a)]
    return newList

def smooth_b(a, n):
    newList = [(sum(a[max(i-n,0) : min(i+n+1,len(a))]))/(min(i+n+1,len(a))-max(i-n,0)) for i, x in enumerate(a)]
    return newList 

def intersection(list1, list2):
   comList = [val for val in list1 if val in list2]
   return comList

CO2Data = load_csv('CO2Emissions_filtered.csv')

# Data for plotting
time = list(range(1960, 2015))
fig, ax = plt.subplots()
ax.plot(time, CO2Data["dnk"], ':', color = 'blue') #Denmark
DenmarkPlot, = ax.plot(time, smooth_a(CO2Data["dnk"], 5), '-', color = 'blue') #Denmark
ax.plot(time, smooth_b(CO2Data["dnk"], 5), '--', color = 'blue') #Denmark

ax.plot(time, CO2Data["fin"], ':', color = 'orange') #Finland
FinlandPlot, = ax.plot(time, smooth_a(CO2Data["fin"], 5), '-', color = 'orange') #Finland
ax.plot(time, smooth_b(CO2Data["fin"], 5), '--', color = 'orange') #Finland

ax.plot(time, CO2Data["isl"], ':', color = 'green') #Iceland
IcelandPlot, = ax.plot(time, smooth_a(CO2Data["isl"], 5), '-', color = 'green') #Iceland
ax.plot(time, smooth_b(CO2Data["isl"], 5), '--', color = 'green') #Iceland

ax.plot(time, CO2Data["nor"], ':',  color = 'red') #Norway
NorwayPlot, = ax.plot(time, smooth_a(CO2Data["nor"], 5), '-',  color = 'red') #Norway
ax.plot(time, smooth_b(CO2Data["nor"], 5), '--',  color = 'red') #Norway

ax.plot(time, CO2Data["swe"], ':', color = 'magenta') #Sweden
SwedenPlot, = ax.plot(time, smooth_a(CO2Data["swe"], 5), '-', color = 'magenta') #Sweden
ax.plot(time, smooth_b(CO2Data["swe"], 5), '--', color = 'magenta') #Sweden

ax.set(xlabel='Years', ylabel='CO2 Emissions', title='Yearly Emission of CO2 in the Nordic Countries')
plt.legend([DenmarkPlot, FinlandPlot, IcelandPlot, NorwayPlot, SwedenPlot], ["Denmark", "Finland", "Iceland", "Norway", "Sweden"], loc='upper right')
#ax.grid()
#fig.savefig("test.png")
plt.show()


populationData = load_csv('population.csv')
populationTime = list(range(1800, 2019))
fig2, ax2 = plt.subplots()
BoliviaPlot, = ax2.plot(populationTime, populationData["bol"], ':', color = 'blue') #Bolivia
VenezuelaPlot, = ax2.plot(populationTime, populationData["ven"], ':', color = 'orange') #Venezuela
ChilePlot, = ax2.plot(populationTime, populationData["chl"], ':', color = 'green') #Chile
EcuadorPlot, = ax2.plot(populationTime, populationData["ecu"], ':', color = 'red') #Ecuador 
ParaguayPlot, = ax2.plot(populationTime, populationData["pry"], ':', color = 'magenta') #Paraguay
ax2.set(xlabel='Years', ylabel='Population', title='Yearly population')
plt.legend([BoliviaPlot, VenezuelaPlot, ChilePlot, EcuadorPlot, ParaguayPlot], ["Bolivia", "Venezuela", "Chile", "Ecuador", "Paraguay"], loc='upper right')
plt.show()


commContries = intersection(list(CO2Data.keys()), list(populationData.keys()))
fig3, ax3 = plt.subplots()
for country in commContries:
    ax3.scatter(populationData[country][-5], CO2Data[country][-1], label=country)
ax3.set_yscale('log')
ax3.set_xscale('log')

for i, txt in enumerate(commContries):
    ax3.annotate(txt, (populationData[txt][-5], CO2Data[txt][-5]))


ax3.set(xlabel='Population', ylabel='CO2 Emissions in 2014 (kt)', title='CO2 Emissions vs Population')
plt.show()
