import bs4 
import requests
import sys
import os 

os.system("")

lis = sys.argv
white = '\033[00m'
green = '\033[92m'
yellow = '\033[93m'

def finder(url):
    respone = requests.get(url)
    app = bs4.BeautifulSoup(respone.text, "html.parser")
    
    lisx = []
    
    for x in app.find_all("a"):
        lisx.append(x['href'])
        
    return lisx

def helper() -> str:
    return "Usage: {} -u URL -w FILE_NAME (optional)".format(lis[0])

if "-u" in lis:
    if "-w" in lis:
        numb = 0
        fileToWrite = lis[lis.index("-w")+1]
        with open(fileToWrite, "w") as fl:
            for i in finder(lis[lis.index("-u")+1]):
                numb += 1
                print(f"{white}{green}{numb}: {yellow}{i}{white}\n")
                fl.write(str(i)+"\n")
            
            fl.close()
        
        print(f"{green}Data Saved in {yellow}{fileToWrite}{white}")
        
    else:
        numd = 0
        for i in finder(lis[lis.index("-u")+1]):
            numd += 1
            print(f"{white}{green}{numd}: {yellow}{i}{white}\n")
    

if len(lis) <= 1 or "-h" in lis or "--help" in lis:
    print(helper())

