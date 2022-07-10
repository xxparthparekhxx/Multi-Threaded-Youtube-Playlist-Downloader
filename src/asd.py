
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys;
print(sys.executable); print(sys.argv)
artist_name = input("Enter the artist name > ");
url = input("Enter the url of the playlists > ");

ops = Options();
ops.add_argument("--headless")

w = webdriver.Chrome(options=ops)
w.get(url)

for i in range(10,0,-1):
    print( f"Strting download in {i} seconds")
    sleep(1)

links = w.find_elements(By.XPATH,"// a[contains(text(),'View full playlist')]")
titles = w.find_elements(By.ID,"video-title")

Titles = []
Links = []

for ele in titles:
    title =  ele.text 
    print(title)
    Titles.append(title)
for ele in links:
    link =  ele.get_attribute("href")
    print(link)
    Links.append(link)

w.close();

from  threading import Thread

try:
    os.mkdir(artist_name)
    os.chdir(artist_name)
except:
    os.chdir(artist_name)



def download(url,title):        
    os.system(f'cd ./"{title}" && youtube-dl -u xx.storageunt1@gmail.com -p Parthparekh007_!  --xattrs  --embed-thumbnail   --add-metadata   --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 320K --output "%(title)s.%(ext)s" --yes-playlist {url}')

threads = [];

if (len(Titles) == len(Links)):
    for i in range(len(Titles)):
        try:
            os.mkdir(Titles[i])
        except:
            pass

    for i in range(len(Titles)):
        threads.append(Thread(target=download,args=(Links[i],Titles[i]),name=Titles[i]))
    
    for thread in threads:
        thread.start()