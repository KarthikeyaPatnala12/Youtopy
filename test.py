import os
import shutil
from moviepy.editor import *
from datetime import datetime
import instaloader



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

listof=['memes', 'succc.exe', 'baked.ziti.memes', 'meme_dealer', 'dankest_memes_m8', 'dystopiacity', 'hits_the_blunt', 'scoobydoograhamcrackers', '_eldanko_', 'memelord', 'beanosofficial', 'creamy1s', 'dank_meme_bandit', 'spicydeepfriedmemesv3', 'bepiz.man', 'andrew_lastname', 'cringepostrandy', 'nutposting', 'funnyhoodvidz', 'pubity', 'todayyearsold', 'epicfunnypage']
for i in listof:
    L = instaloader.Instaloader()
    instapostsdownload(i)
print("we have downloaded the posts and now we are going to ")
path=os.getcwd()
destination=os.path.join(path,"final")
shutil.rmtree(destination,ignore_errors=True)
os.mkdir(destination)
dest_text_file=os.path.join(destination,"data.txt")
file=open(dest_text_file,"a+")
file.close()



for i in os.listdir(path):
    # print(i)
    if i.endswith(".py") or i.endswith(".txt") or i=="LICENSE" or i.endswith(".md") or i.endswith(".git") or i.endswith(".csv") or i=="final":
        continue
    else:
        source=os.path.join(path,i)
        os.chdir(source)
        for j in os.listdir(source):
            if j.endswith(".mp4"):
                account_name=source[source.rfind("\\")+1:]
                src_path = os.path.join(source, j)
                dst_path = os.path.join(destination, j)
                os.rename(src_path, dst_path)
                file_1=open(dest_text_file, 'r')
                if account_name in file_1.read():
                    file_1.close()
                    break
                file = open(dest_text_file, 'a+')
                file.write(account_name+"\n")
                file.close()

for i in os.listdir(path):
    if i.endswith(".py") or i.endswith(".txt") or i=="LICENSE" or i.endswith(".md") or i.endswith(".git") or i.endswith(".csv") or i=="final":
        continue
    else:
        source=os.path.join(path,i)
        shutil.rmtree(source,ignore_errors=True)






final_video_number=1
# from lines 72-109 needs to be tested
def final_video_creator():
    j=0
    duration=0
    clipnames=[]
    clip=[]
    os.chdir(destination)
    for i in os.listdir():
        if i.endswith(".mp4") and not(i.startswith("final")) and not(i.endswith(".txt")):
            clipnames.append(i)
            clip_j=VideoFileClip(i)
            clip.append(clip_j)
            duration+=clip_j.duration
            j+=1
            if duration>=480:
                break
    final_video=concatenate_videoclips(clip)
    final_video.write_videofile(f"final_{final_video_number}.mp4")
    for i in clip:
        i.close()
    final_video.close()
    del(clip)
    for i in clipnames:
        os.remove(i)
    final_video_number+=1


os.chdir(destination)

count=1
while count!=0:
    count=0
    for i in os.listdir():
        if i.startswith("final") or i.endswith(".txt"):
            pass
        else:
            count+=1
    if count>0:
        final_video_creator()