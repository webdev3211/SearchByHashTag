from bs4 import BeautifulSoup
import requests
import json

tag = "metoo"
url = "https://www.instagram.com/explore/tags/"+ tag +"/?__a=1"

keys = [
    'id', 
    'display_url',
    # 'thumbnail_src',
    # 'owner',
    # 'edge_liked_by'
]

keys2 = [
    'edge_media_to_caption',
]

def jprint(data_dict):
    print(json.dumps(data_dict, indent=4))

def get_ig_page(url, session=None):
    print(url)
    session = session or requests.Session()
    r = session.get(url)
    r_code = r.status_code
    print(r_code)
    if r_code == requests.codes.ok:
        #the code is 200 and valid
        print('OK')
        return r
    else:
        return None

# def get_captions(media_dict):


ig_data_dict = get_ig_page(url)

if ig_data_dict is not None:
    ig_data_dict = ig_data_dict.json()
    # jprint(ig_data_dict)

    graphql = ig_data_dict.get('graphql', None)
    hashtag = graphql.get('hashtag', None)
    edge_hashtag_to_media = hashtag.get('edge_hashtag_to_media', None)
    recent_posts = edge_hashtag_to_media.get('edges', None)
    #Getting top posts
    # top_posts = data.get('top_posts', None)
    # if top_posts is not None:
    #     top_posts = top_posts.get('nodes')

    #Getting recent posts
    # jprint(recent_posts)
    # for nodex in recent_posts:
    #     jprint(nodex)
    # node = recent_posts[0].get("node")
    # for item in node:
    #     # if item in keys:
    #     #     print(item, ":", type(node[item]))
    #     if item in keys2:
    #         for comment in node[item].get("edges"):
    #             dict = comment.get("node")
    #             text = dict.get("text")
    #             print(item, " : " ,text)
    for x in recent_posts:
        node = x.get("node")
        for item in node:
            if item == "shortcode":
                link = "https://www.instagram.com/p/" + node[item] + "/"
                print(link)
            if item in keys:
                print(item, " : ", node[item])
            if item in keys2:
                if node[item] is not None:
                    for comment in node[item].get("edges"):
                        dict = comment.get("node")
                        text = dict.get("text")
                        # u = unicode(text, "utf-8")
                        my_str = u"{}".format(text)
                        try:
                            print(my_str)
                        except UnicodeEncodeError:
                            pass
                        print()
                        print()                      
    
else:
    print('Oops something went wrong')





# source = requests.get(url).text
# print(source)

