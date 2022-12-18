from datetime import datetime
import instaloader
import os

L = instaloader.Instaloader()

def instapostsdownload(user):
    posts = instaloader.Profile.from_username(L.context, user).get_posts()
    SINCE = datetime.today().date() 
    for post in posts:
        postdate = post.date
        postdate=postdate.date()
        if postdate==SINCE:
            L.download_post(post, target=user)
        elif post.is_pinned:
            continue
        else:
            break

instapostsdownload("instbrooo")
instapostsdownload("telugu_meme_master")

path="C:/Users/madhu/OneDrive/Desktop/instascrapper"
destination="C:/Users/madhu/OneDrive/Desktop/instascrapper/final"
for i in os.listdir(path):
    # print(i)
    if i.endswith(".py"):
        continue
    if i=="final":
        continue
    else:
        source=path+f"/{i}"
        os.chdir(source)
        for j in os.listdir(source):
            if j.endswith(".jpg"):
                src_path = os.path.join(source, j)
                dst_path = os.path.join(destination, j)
                os.rename(src_path, dst_path)
            elif j.endswith(".mp4"):
                src_path = os.path.join(source, j)
                dst_path = os.path.join(destination, j)
                os.rename(src_path, dst_path)
        os.rmdir(source)