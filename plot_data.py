import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

with open('./docs/timeseries.json') as f:
    data = json.load(f)

country="India"

country_df=data[country]
days=[]
confirmed=[]
deaths=[]
recovered=[]

day=0
DataToPlot=pd.DataFrame(columns=["days","confirmed","deaths","recovered"])
for day_data in country_df:
    #print(day_data)
    days.append(day)
    confirmed.append(day_data['confirmed'])
    deaths.append(day_data['deaths'])
    recovered.append(day_data['recovered'])
    day+=1

DataToPlot['days']=days
DataToPlot['confirmed']=confirmed
DataToPlot['deaths']=deaths
DataToPlot['recovered']=recovered

#.. For plotting rate of changes
d_confirmed=list(np.array(DataToPlot['confirmed'].tolist()[1:]) - np.array(DataToPlot['confirmed'].tolist()[:-1]))
DataToPlot['d_confirmed']=[0]+d_confirmed
d_deaths=list(np.array(DataToPlot['deaths'].tolist()[1:]) - np.array(DataToPlot['deaths'].tolist()[:-1]))
DataToPlot['d_deaths']=[0]+d_deaths
d_recovered=list(np.array(DataToPlot['recovered'].tolist()[1:]) - np.array(DataToPlot['recovered'].tolist()[:-1]))
DataToPlot['d_recovered']=[0]+d_recovered

s_confirmed=list(np.array(DataToPlot['d_confirmed'].tolist()[1:]) - np.array(DataToPlot['d_confirmed'].tolist()[:-1]))
DataToPlot['s_confirmed']=[0]+s_confirmed
s_deaths=list(np.array(DataToPlot['d_deaths'].tolist()[1:]) - np.array(DataToPlot['d_deaths'].tolist()[:-1]))
DataToPlot['s_deaths']=[0]+s_deaths
s_recovered=list(np.array(DataToPlot['d_recovered'].tolist()[1:]) - np.array(DataToPlot['d_recovered'].tolist()[:-1]))
DataToPlot['s_recovered']=[0]+s_recovered


fig, axs = plt.subplots(3, 1)
# =============================================================================
# axs[0].bar(DataToPlot['days'].tolist(),DataToPlot['s_confirmed'].tolist())
# axs[0].set_ylabel('incr confirmed')
# axs[1].bar(DataToPlot['days'].tolist(),DataToPlot['s_deaths'].tolist())
# axs[1].set_ylabel('incr deaths')
# axs[2].bar(DataToPlot['days'].tolist(),DataToPlot['s_recovered'].tolist())
# axs[2].set_ylabel('incr recovered')
# =============================================================================

axs[0].bar(DataToPlot['days'].tolist(),DataToPlot['confirmed'].tolist())
axs[0].set_ylabel('total confirmed')
axs[1].bar(DataToPlot['days'].tolist(),DataToPlot['deaths'].tolist())
axs[1].set_ylabel('total deaths')
axs[2].bar(DataToPlot['days'].tolist(),DataToPlot['recovered'].tolist())
axs[2].set_ylabel('total recovered')

# =============================================================================
# axs[0].bar(DataToPlot['days'].tolist(),DataToPlot['d_confirmed'].tolist())
# axs[0].set_ylabel('daily confirmed')
# axs[1].bar(DataToPlot['days'].tolist(),DataToPlot['d_deaths'].tolist())
# axs[1].set_ylabel('daily deaths')
# axs[2].bar(DataToPlot['days'].tolist(),DataToPlot['d_recovered'].tolist())
# axs[2].set_ylabel('daily recovered')
# =============================================================================
plt.show()



