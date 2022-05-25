from bs4 import BeautifulSoup
import requests

#webscrape Yahoo for name and price of stocks

def getValue(url):
  page = requests.get(url) #get page
  soup = BeautifulSoup(page.content, "html.parser") #scrape for content

  #results = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)") #find specific class name on page, this class contains info for price
  #print(results.prettify()) 
  #results = soup.find("h1", class_ = "D(ib) Fz(18px)") #find specific class name on page, this class contains info for name
  #print(results.prettify())

  findNameOfItem = [a.text for a in soup.select_one('h1')] #find the text in specific h1
  stringOfItem = str(findNameOfItem) #convert to string
  index = stringOfItem.index("(") #use indexing to find the end of name of item
  nameOfItem = stringOfItem[2:index -1] #clean up name of item, get rid of outer parenthesis and quotes
  valueOfItem = soup.select_one('fin-streamer[data-test="qsp-price"]')["value"]
  print("The price of",nameOfItem,"is",valueOfItem) #print out name and value

#examples
getValue("https://finance.yahoo.com/quote/BTC-USD/")
getValue("https://finance.yahoo.com/quote/GOOG/")
getValue("https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC")
getValue("https://finance.yahoo.com/quote/GME?p=GME&.tsrc=fin-srch")
getValue("https://finance.yahoo.com/quote/TSLA/")