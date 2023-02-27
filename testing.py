import os
import shutil
from moviepy.editor import *
from datetime import datetime
import instaloader
import moviepy.editor as mp




# def instapostsdownload(user):
#     posts = instaloader.Profile.from_username(L.context, user).get_posts()
#     SINCE = datetime.today().date() 
#     for post in posts:
#         postdate = post.date
#         postdate=postdate.date()
#         if postdate==SINCE:
#             L.download_post(post, target=user)
#         elif post.is_pinned:
#             continue
#         else:
#             break

# listof=['trolls_official','memes', 'succc.exe', 'baked.ziti.memes', 'meme_dealer', 'dankest_memes_m8', 'dystopiacity', 'hits_the_blunt', 'scoobydoograhamcrackers', '_eldanko_', 'memelord', 'beanosofficial', 'creamy1s', 'dank_meme_bandit', 'spicydeepfriedmemesv3', 'bepiz.man', 'andrew_lastname', 'cringepostrandy', 'nutposting', 'funnyhoodvidz', 'pubity', 'todayyearsold', 'epicfunnypage']
# for i in listof:
#     L = instaloader.Instaloader()
#     try:
#         instapostsdownload(i)
#     except Exception as e:    
#         print(e)

# # print("we have downloaded the posts and now we are going to ")
path=os.getcwd()
destination=os.path.join(path,"final")
# shutil.rmtree(destination,ignore_errors=True)
os.mkdir(destination)
# dest_text_file=os.path.join(destination,"data.txt")
# file=open(dest_text_file,"a+")
# file.close()



# for i in os.listdir(path):
#     # print(i)
#     if i.endswith(".py") or i.endswith(".txt") or i=="LICENSE" or i.endswith(".md") or i.endswith(".git") or i.endswith(".csv") or i=="final":
#         continue
#     else:
#         source=os.path.join(path,i)
#         os.chdir(source)
#         for j in os.listdir(source):
#             if j.endswith(".mp4"):
#                 account_name=source[source.rfind("\\")+1:]
#                 src_path = os.path.join(source, j)
#                 dst_path = os.path.join(destination, j)
#                 os.rename(src_path, dst_path)
#                 file_1=open(dest_text_file, 'r')
#                 if account_name in file_1.read():
#                     file_1.close()
#                     break
#                 file = open(dest_text_file, 'a+')
#                 file.write(account_name+"\n")
#                 file.close()

# for i in os.listdir(path):
#     if i.endswith(".py") or i.endswith(".txt") or i=="LICENSE" or i.endswith(".md") or i.endswith(".git") or i.endswith(".csv") or i=="final":
#         continue
#     else:
#         source=os.path.join(path,i)
#         shutil.rmtree(source,ignore_errors=True)


# # Set the target width and height
TARGET_WIDTH = 1920
TARGET_HEIGHT = 1080

# # Specify the directory containing the videos
video_dir = destination

# # Create an empty list to store the resized clips
resized_clips = []

# # Iterate through the files in the directory
for filename in os.listdir(video_dir):
    # Check if the file is a video
    if filename.endswith('.mp4'):
        # Create a VideoFileClip object
        clip = mp.VideoFileClip(os.path.join(video_dir, filename))
        # Resize the clip
        resized_clip = clip.resize(height=TARGET_HEIGHT, width=TARGET_WIDTH)
        # Add the resized clip to the list
        resized_clips.append(resized_clip)
print(resized_clips)
# Concatenate the clips in the list
final_clip = mp.concatenate_videoclips(resized_clips)

# Save the final clip
final_video_file=os.path.join(destination,"compiled_video.mp4")
final_clip.write_videofile(final_video_file)
