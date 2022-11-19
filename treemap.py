import pandas as pd
import plotly.express as pxx



def job_creation_rate(data, years=[i for i in range(1978,2018)]):
  data = data.loc[data['Year'].isin(years)]
  data["US"] = "US"

  fig = pxx.treemap(data, path=['US','State','Year'], values='Data.Job Creation.Rate',
                    color='Data.Job Creation.Rate', color_continuous_scale='RdBu',hover_data=['Data.Job Creation.Rate'],)
  fig.show()

def job_creation_rate1(data, years=[i for i in range(1978, 2018)]):
    data = data.loc[data['Year'].isin(years)]
    data["US"] = "US"

    fig = pxx.treemap(data, path=['US', 'Year', 'State'], values='Data.Job Creation.Rate',
                      color='Data.Job Creation.Rate', color_continuous_scale='RdBu',
                      hover_data=['Data.Job Creation.Rate'], )
    fig.show()


if __name__ == '__main__':
  data = pd.read_csv("business_dynamics.csv",header=0)

  print(data.columns)

  state = list(set(data["State"]))
  state_index = {state[i]:i for i in range(len(state))}

  data["state_index"] = data.apply(lambda row: state_index[row.State], axis = 1)
  data = data.fillna(data.mean())

  job_creation_rate1(data)




