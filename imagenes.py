import requests
from bs4 import BeautifulSoup 

images=[]
suffix="https://m.media-amazon.com"
#----------------------------------
url="https://www.amazon.com/b/ref=dp_bc_aui_C_4?ie=UTF8&node=3741111"
page_head={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"}
html_page=requests.get(url,headers=page_head)
#print(html_page)
soup=BeautifulSoup(html_page.content)
#print(html_page.text)
images_table=soup.find("div",{"class":"s-main-slot s-result-list s-search-results sg-row"}).findAll("img")

#images_table=images_table.find_all("img")

#print(len(images_table))
for imgs in images_table:
    if (imgs["src"].find(suffix)!=-1):
        images.append(imgs["src"])
#guardar imagenes
#quitar imagenes repetidas
images=list(dict.fromkeys(images))
name_dir=10
for url in images:
    images=requests.get(url).content
    with open(f"{name_dir}.jpg","wb") as handle:
        handle.write(images)
    name_dir+=1
#print(len(images))