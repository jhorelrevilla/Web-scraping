import sys
from criptomonedas import get_bitcoins_price
from scrapingCourses import getCoupons
if len(sys.argv) > 2:
    print("Sólo se necesita 1 argumento")
elif sys.argv[1]=="course":
    getCoupons()
elif sys.argv[1]=="img":
    print("Noai funcion xd")
elif sys.argv[1]=="crypto":
    get_bitcoins_price()