import bs4
import requests
import http.cookiejar
import urllib.request
import json
import sys


tag = "swiggy"
# hashtagurl = "https://m.facebook.com/graphsearch/str/%23" + tag +"/keywords_search?tsid=0.7578778873516137&source=result"
# print(hashtagurl)

hashtagurl = "https://mbasic.facebook.com/graphsearch/str/%23"+ tag +"/stories-keyword/stories-feed?source=pivot&ref=104&__xts__%5B0%5D=12.%7B%22unit_id_click_type%22%3A%22graph_search_results_see_more_on_module_tapped%22%2C%22click_type%22%3A%22see_more%22%2C%22module_id%22%3A3%2C%22session_id%22%3A%22ea49bc0003b399d10ad2d4f5269e839a%22%2C%22module_role%22%3A%22FEED_POSTS%22%2C%22unit_id%22%3A%22browse_ml%3Aff5c64b8-e40f-87f8-a693-54499dda0a9c%22%7D"
print(hashtagurl)

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def jprint(data_dict):
    print(json.dumps(data_dict, indent=4))

urllib.request.install_opener(opener)

authentication_url = "https://m.facebook.com/login.php"
payload = {
    'email': '',
    'pass': ''
}
# parse the data
data = urllib.parse.urlencode(payload).encode('utf-8')

req = urllib.request.Request(authentication_url, data)

resp = urllib.request.urlopen(req)
contents = resp.read()


response = requests.get(hashtagurl, cookies=cj).text
soup = bs4.BeautifulSoup(response, 'lxml')



divs = soup.find_all('div', id="BrowseResultsContainer")
jprint(divs)
# children = div.findChildren("span" , recursive=False)
# for child in children:
#     try:
#         print(child)        
#     except UnicodeEncodeError:
#         pass

    

# for i in soup.find_all('span'):
#     try:
#         print(i)
#         print()
#         print()
#     except UnicodeEncodeError:
#         pass

# source = requests.get(url).text
# soup = BeautifulSoup(source, 'lxml')

    
# for line in soup.find_all('div', class_="_59k _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt"):
#     print(line)




# print(contents)


# url = "https://m.facebook.com/ankit.garg.7965/friends"
# data = requests.get(url, cookies=cj)
# soup = bs4.BeautifulSoup(data.text, 'html.parser')
# # print(soup.prettify())
# z = 0
# for i in soup.find_all('a'):

#     if i.text.lower()[0:2].isdigit():
#         break
#     if z > 17:
#         print(i.text)
#     z = z + 1
# url = "https://mbasic.facebook.com/hindicodingzone"
# # url = "https://mbasic.facebook.com/ymcauniversity/"
# index = 0
# z = []
# while(index < 10):
#     data = requests.get(url, cookies=cj)
#     soup = bs4.BeautifulSoup(data.text, 'html.parser')
#     for i in soup.find_all('a', href=True):
#         if(i['href'][0:23] == "/HindiCodingZone/photos"):
#             z.append(i['href'])
#         if i.text.lower() == "show more":
#             url = "https://mbasic.facebook.com" + i['href']
#         # print(i)

#     index = index + 1


# photos = []
# num = 0
# for url in z:
#     url = "https://mbasic.facebook.com" + url
#     data = requests.get(url, cookies=cj)
#     soup = bs4.BeautifulSoup(data.text, 'html.parser')
#     for i in soup.find_all('a', href=True):
#         if i.text.lower() == "view full size":
#             photos.append(i['href'])
#             urllib.request.urlretrieve(i['href'], str(num) + '.jpg')
#             num = num + 1


# print(len(photos))
# print(photos)
