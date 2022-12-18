import instaloader
from datetime import datetime


# insta loader downloads some posts under the hashtag memes

L = instaloader.Instaloader()

posts = instaloader.Hashtag.from_name(L.context, "memes").get_posts()

From_date = datetime(2022, 12, 18)  # further from today, inclusive
To_date = datetime(2022, 12, 19)  # closer to today, not inclusive

k = 0  # initiate k
#k_list = []  # uncomment this to tune k

for post in posts:
    postdate = post.date

    if postdate > To_date:
        continue
    elif postdate <= From_date:
        k += 1
        if k == 50:
            break
        else:
            continue
    else:
        L.download_post(post, "#memes")
        # if you want to tune k, uncomment below to get your k max
        #k_list.append(k)
        k = 0  # set k to 0