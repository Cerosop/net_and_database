import urllib.request as req
import bs4
import pandas as pd

pd_data = {
    'Topic Title': [],
    'Topic Link': [],
    'Topic Content': []
}


url="https://tw.news.yahoo.com/"
Request=req.Request(url, headers={
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36"
    })
with req.urlopen(Request) as response:
    data=response.read().decode("utf-8")
    
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("a", class_="C(#fff)")    
    for title in titles: 
        if 'Google Chrome' in title.string:
            continue
        pd_data['Topic Title'].append(title.string)
        print(title.string)
        
        url=title["href"]
        pd_data['Topic Link'].append(url)
        Request=req.Request(url, headers={
            "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36"   
            })
        with req.urlopen(Request) as response:
            data=response.read().decode("utf-8")
            
            root=bs4.BeautifulSoup(data, "html.parser")
            contents=root.find_all("p", class_ = "")    
            content_text = ''
            for content in contents: 
                if "更多" in content.text:
                    break
                print(content.text)
                content_text += content.text + '\n'
            pd_data['Topic Content'].append(content_text)    
        print()

df = pd.DataFrame(pd_data)
df.to_excel('1120/yahooNews.xlsx', index=True)