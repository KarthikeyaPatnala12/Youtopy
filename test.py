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

listof=["naughtyworld_","meme","succc.exe","baked.ziti.memes","meme_dealer","dankest_memes_m8","dystopiacity","hits_the_blunt","scoobydoograhamcrackers","_eldanko_","memelord","beanosofficial", "creamy1s","dank_meme_bandit","spicydeepfriedmemesv3","bepiz.man","andrew_lastname","cringepostrandy","nutposting","funnyhoodvidz","pubity","todayyearsold","epicfunnypage","sarcastic_us"]
for i in listof:
    instapostsdownload(i)



path=os.getcwd()
os.mkdir(path+"/final")
destination=path+"/final"
for i in os.listdir(path):
    # print(i)
    if i.endswith(".py"):
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