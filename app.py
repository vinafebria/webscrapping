from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url = 'https://www.coingecko.com/en/coins/ethereum/historical_data/?start_date=2020-01-01&end_date=2021-06-30'; 
url_get = requests.get(url, 
                      headers = {
        'User-Agent': 'Popular browser\'s user-agent',
    })
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('table', class_='table table-striped text-sm text-lg-normal')
table
print(table.prettify()[1:500])

row_length = len(table.find_all('tr'))
row_length

column_length = len(table)
column_length

temp = [] #initiating a list 

for i in range(1, row_length):
#insert the scrapping process here
    
    temp.append((____,____,____)) 

temp = temp[::-1]

#change into dataframe
import pandas as pd
dataframe = pd.DataFrame(columns=['Date','Market Cap','Volume','Open','Close'])

for row in table.tbody.find_all('tr'):    

# Find all data for each column
    date=row.find_all('th')
    columns = row.find_all('td')
    if(columns != []):
        date_1 = date[0].text.strip()
        market_cap = columns[0].text.strip()
        volume = columns[1].text.strip()
        open_ = columns[2].text.strip()
        close = columns[3].text.strip()


        dataframe = dataframe.append({'Date': date_1,  'Market Cap': market_cap, 'Volume': volume, 'Open': open_, 'Close': close}, ignore_index=True)

#insert data wrangling here
dataframe.head()

dataframe['Date'] = dataframe['Date'].astype('datetime64')
dataframe['Volume'] = dataframe['Volume'].str.replace('$','',regex=False)
dataframe['Volume'] = dataframe['Volume'].str.replace(',','')
dataframe['Volume'] = dataframe['Volume'].astype('float64')
dataframe['Volume'] = dataframe['Volume']/1000000000
dataframe = dataframe.set_index(dataframe['Date'])
df = dataframe['Volume']

df

df.plot()

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["____"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = ____.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)