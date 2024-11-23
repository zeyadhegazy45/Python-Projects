from bs4 import BeautifulSoup
import requests

url = "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=programming%20instructor"
client = requests.get(url)

html = client.text
soup = BeautifulSoup(html, "html.parser")

containers = soup.find_all('div', {'class': 'css-1gatmva e1v1l3u10'})

with open("/home/zeyad/Documents/instructor.csv", "w") as f:
    headers = "job_title,company_name,job_type,mode\n"
    f.write(headers)

    for container in containers:
        try:
            jtitle = container.find("h2", {'class': 'css-m604qf'})
            job_title = jtitle.text.strip().replace(",", "-") if jtitle else "Not specified"

            cname = container.find("a", {'class': 'css-17s97q8'})
            company_name = cname.text.strip().replace(",", "-") if cname else "Not specified"

            
            jtype = container.find("div", {'class': 'css-1lh32fc'})
            job_type = (
                jtype.find("span", {"class": 'css-1ve4b75 eoyjyou0'}).text.strip().replace(",", "-")
                if jtype else "Not specified"
            )

            category = container.find("a", {'class': 'css-o171kl'})
            mode = category.text.strip().replace(",", "-") if category else "Not specified"

            f.write(f"{job_title},{company_name},{job_type},{mode}\n")

        except Exception as e:
            print(f"Error processing container: {e}")
from bs4 import BeautifulSoup
import requests

url = "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=programming%20instructor"
client = requests.get(url)

html = client.text
soup = BeautifulSoup(html, "html.parser")

containers = soup.find_all('div', {'class': 'css-1gatmva e1v1l3u10'})

with open("/home/zeyad/Documents/instructor.csv", "w") as f:
    headers = "job_title,company_name,job_type,mode\n"
    f.write(headers)

    for container in containers:
        try:
            jtitle = container.find("h2", {'class': 'css-m604qf'})
            job_title = jtitle.text.strip().replace(",", "-") if jtitle else "Not specified"

            cname = container.find("a", {'class': 'css-17s97q8'})
            company_name = cname.text.strip().replace(",", "-") if cname else "Not specified"

            
            jtype = container.find("div", {'class': 'css-1lh32fc'})
            job_type = (
                jtype.find("span", {"class": 'css-1ve4b75 eoyjyou0'}).text.strip().replace(",", "-")
                if jtype else "Not specified"
            )

            category = container.find("a", {'class': 'css-o171kl'})
            mode = category.text.strip().replace(",", "-") if category else "Not specified"

            f.write(f"{job_title},{company_name},{job_type},{mode}\n")

        except Exception as e:
            print(f"Error processing container: {e}")




import pandas as pd

data=pd.read_csv("/home/zeyad/Documents/instructor.csv")
print(data)
