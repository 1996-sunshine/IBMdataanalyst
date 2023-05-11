import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

if __name__ == "__main__":
    # final work Q1
    tsla = yf.Ticker("TSLA")
    tesla_data=tsla.history(period="max")
    tesla_data.reset_index(inplace=True)
    tesla_data.head(5)

    #final work Q2
    url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
    html_data  = requests.get(url).text
    soup = BeautifulSoup(html_data, 'html5lib')
    tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
    for row in soup.find_all("tbody")[1].find_all('tr'):
        col = row.find_all("td")
        date = col[0].text
        revenue = col[1].text
        tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
    tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
    tesla_revenue.dropna(inplace=True)
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]  
    tesla_revenue.tail(5)

    #final work Q3
    gme = yf.Ticker("GME")
    gme_data=gme.history(period="max")
    gme_data.reset_index(inplace=True)
    gme_data.head(5)


    #final work Q4
    url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
    html_data  = requests.get(url).text
    soup = BeautifulSoup(html_data, 'html5lib')
    gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
    for row in soup.find_all("tbody")[1].find_all('tr'):
        col = row.find_all("td")
        date = col[0].text
        revenue = col[1].text
        gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
    gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
    gme_revenue.dropna(inplace=True)
    gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]  
    print(gme_revenue.tail(5))

    #final work Q5
    make_graph(tesla_data, tesla_revenue, 'Tesla')
    #final work Q6
    make_graph(gme_data, gme_revenue, 'GameStop')

    #library
    # amd = yf.Ticker("AMD")
    # amd.history(period="max")
    # import json
    # with open('amd.json') as json_file:
    #     amd_info = json.load(json_file)
    # amd_info['country']
    # amd_info['sector']

    #webscraping
    # url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
    # data  = requests.get(url).text
    # print(data)
    # soup = BeautifulSoup(data, 'html5lib')
    # netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

    # # First we isolate the body of the table which contains all the information
    # # Then we loop through each row and find all the column values for each row
    # for row in soup.find("tbody").find_all('tr'):
    #     col = row.find_all("td")
    #     date = col[0].text
    #     Open = col[1].text
    #     high = col[2].text
    #     low = col[3].text
    #     close = col[4].text
    #     adj_close = col[5].text
    #     volume = col[6].text
        
    #     # Finally we append the data of each row to the table
    #     netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)  
    # netflix_data.head()  
    # read_html_pandas_data = pd.read_html(url)
    # read_html_pandas_data = pd.read_html(str(soup))
    # netflix_dataframe = read_html_pandas_data[0]

    # netflix_dataframe.head()

    

