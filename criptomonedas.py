import requests
from bs4 import BeautifulSoup 
import pandas as pd
#tr_tabla=tabla_crypto.find_all("tr",{'i':"1057391"})
#precio=tr_tabla[0].find_all('td',{"class":"price js-currency-price"})

def get_bitcoins_price():
    #-------------Request get
    url_page="https://www.investing.com/"
    head_page={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}
    http_page=requests.get(url_page,headers=head_page)
    #-------------
    soup=BeautifulSoup(http_page.text,"html.parser")
    tabla_crypto=soup.find(class_="genTbl js-all-crypto-preview-table wideTbl elpTbl elp20 topCryptoHP")
    tr_tabla=tabla_crypto.find_all("tr")
    list_cripto=[]
    for each_tr in tr_tabla:
        precio=each_tr.find_all('td',{"class":"price js-currency-price"})
        nombre=each_tr.find_all('td',{"class":"left bold elp name cryptoName first js-currency-name"})
        if(len(nombre)!=0):
            list_cripto.append([nombre[0].get_text(),precio[0].get_text().replace(",","")])
            #print(f"La criptomoneda {nombre[0].get_text()} en (USD):{precio[0].get_text()}")
    df= pd.DataFrame(list_cripto,columns=["Nombre","Precio"])
    df.to_csv("Criptomonedas.csv",index=False,header=True)
    #print(list_cripto)        
#------------------------------------------------------------------------------------------
#print(precio[0].get_text())
get_bitcoins_price()
