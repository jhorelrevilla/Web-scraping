import requests
from bs4 import BeautifulSoup
import pandas as pd
list_course_url=[];


def getHtmlPage(url_page):
    headPage={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}
    httpPage=requests.get(url_page,headers=headPage)
    return httpPage.text

def getCoupons():
    htmlPage=getHtmlPage("https://cursosdev.com/coupons")
    soup=BeautifulSoup(htmlPage,"html.parser")
    container=soup.find("div",class_="w-screen sm:w-full md:full lg:w-full xl:w-full mx-auto grid grid-cols-1 px-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4")
    list_courses=container.findAll("a", class_="c-card block bg-white shadow-md hover:shadow-xl rounded-lg overflow-hidden")
    for i in list_courses:
        name=i.find_all("h2") 
        list_course_url.append([name[0].get_text(),i.get('href')])

getCoupons()
df=pd.DataFrame(list_course_url,columns=["Course","Url"])
df.to_csv("Courses.csv",index=False,header=True)
