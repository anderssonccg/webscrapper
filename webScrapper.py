from bs4 import BeautifulSoup
import requests
   
# lists
urls=[]
web="https://byandrev-blog.vercel.app"

# function created
def scrape(site, depth):
    if depth==0: return

    # getting the request from url
    r = requests.get(site)
    
    if r.status_code != 200: return

    # converting the text
    s = BeautifulSoup(r.text,"html.parser")
       
    for i in s.find_all("a"):
        href = ""
        try:
            href = i.attrs['href']
        except:
            continue
        
        print(href)
           
        if href.startswith("/"):
            site = site+href
               
            if site not in  urls:
                urls.append(href) 
                print(site+href)
                # calling it self
                scrape(site+href, depth-1)
   
# main function
if __name__ =="__main__":
   
    # website to be scrape
    site=web
   
    # calling function
    scrape(site, 3)