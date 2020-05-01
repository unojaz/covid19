import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import itertools



class CovidForCountry:
    def __init__(self,country):
        self.country = country
        self.data_legend="-k"

    def read_data(self,given_data):
        county_data = given_data[self.country]
        day = 0
        self.data={}
        self.data["days"]=[]
        self.data["confirmed"] = []
        self.data["deaths"] = []
        self.data["recovered"] = []
        for day_data in county_data:
            # print(day_data)
            self.data["days"].append(day)
            self.data["confirmed"].append(day_data['confirmed'])
            self.data["deaths"].append(day_data['deaths'])
            self.data["recovered"].append(day_data['recovered'])
            day += 1

    def set_legend(self,legend_string):
        self.data_legend=legend_string
        
    def add_to_plt2(self,axes,plot_x,plot_y):
        axes.plot(self.data[plot_x][:np.size(self.data[plot_y])],self.data[plot_y],color=self.data_legend,linestyle='solid',label=self.country)

    def add_to_plt(self,axes,plot_qty):
        data_size=np.size(self.data[plot_qty])
        axes.plot(range(data_size),self.data[plot_qty],color=self.data_legend,linestyle='solid',label=self.country)

    def calculate_other(self):
        self.data["recov / conf"] = [a/b if b>50 else 0 for a,b in zip(self.data["recovered"],self.data["confirmed"])]
        self.data["death / conf"] = [a / b if b > 0 else 0 for a, b in
                                     zip(self.data["deaths"], self.data["confirmed"])]
        offset_val=100
        index = next(x for x, val in enumerate(self.data["confirmed"]) if val > offset_val)
        
        self.data["confirm log"] = [np.log10(a-offset_val) for a in self.data["confirmed"][index:]]
        self.data["confirm daily"] = list(map( lambda x,y: x - y, self.data["confirmed"][1:],self.data["confirmed"][0:-1] ))
        self.data["death daily"] = list(map( lambda x,y: x - y, self.data["deaths"][1:],self.data["deaths"][0:-1] ))

        self.data["conf doub days"] = []
        for index1 in range(np.size(self.data["confirmed"])):
            if self.data["confirmed"][index1] > 0:
                for index2 in range(index1+1,np.size(self.data["confirmed"])):
                    if self.data["confirmed"][index2]/self.data["confirmed"][index1] > 2:
                        self.data["conf doub days"].append(index2-index1)
                        break
            else:
                self.data["conf doub days"].append(0)
        #for index in range(np.size(self.data["conf doub days"]),np.size(self.data["confirmed"])):
        #    self.data["conf doub days"].append(self.data["conf doub days"][np.size(self.data["conf doub days"])-1])
                
            
        self.data["daily / conf tot"] = list(map( lambda x,y: x/y if y>0 else 0, self.data["confirm daily"][:],self.data["confirmed"][:-1] ))
        

        temp_data = pd.Series(self.data["confirm daily"])
        windows = temp_data.rolling(5)
        self.data["confirm mov avg"] = list(windows.mean())
      

    def calculate_wt_offset(self,offset=100):
        index= next(x for x, val in enumerate(self.data["confirmed"])
                                  if val > offset)
        self.data["confirmed off"] = self.data["confirmed"][index:]


with open('./docs/timeseries.json') as f:
    data = json.load(f)

#country_list=["India","Russia","France","Italy","Spain"]
country_list=["India","Switzerland","Netherlands","Canada","Brazil","Russia","Iran"]
country_legend=["orange","green","red","blue","black","yellow","magenta"]

# country_list=["India","Pakistan"]
# country_legend=["orange","green"]


covid_data=[]

for icount in range(np.size(country_list)):
    covid_data_obj=CovidForCountry(country_list[icount])
    covid_data_obj.read_data(data)
    covid_data_obj.set_legend(country_legend[icount])
    covid_data.append(covid_data_obj)

for each_data in covid_data:
    each_data.calculate_other()
    each_data.calculate_wt_offset()

what_to_plt="confirmed"
what_to_plt2="conf doub days"

fig, axs = plt.subplots(1, 1)
for each_data in covid_data:
    #each_data.add_to_plt(axs,what_to_plt)
    each_data.add_to_plt2(axs,what_to_plt,what_to_plt2)
#axs.set_xlabel("Days")
axs.set_ylabel(what_to_plt2)
axs.set_xlabel(what_to_plt)
axs.set_title(what_to_plt +" Country wise")
axs.grid(True)


#what_to_plt=[["confirmed", "deaths", "recovered", "recov / conf", "death / conf"],
#             ["confirm log", "confirm daily","death daily", "confirm mov avg", "confirmed off"]]
#fig, axs_all = plt.subplots(2, 5)
#for irow in range(2):
#    for jcol in range(5):
#        axs = axs_all[irow,jcol]
#        for each_data in covid_data:
#            each_data.add_to_plt(axs,what_to_plt[irow][jcol])
#        axs.set_xlabel("Days")
#        axs.set_ylabel(what_to_plt[irow][jcol])
#        axs.set_title(what_to_plt[irow][jcol] +" Country wise")
#        axs.grid(True)

plt.legend()
plt.show()
