from pytube import YouTube
import pyperclip
from termcolor import colored
from tkinter.filedialog import askdirectory


print('''-----------------
| PY-DOWN-TUBE  |
-----------------''')
      
lines = colored("-", "green", attrs=["bold"])
print(lines*80)

options = {
    "1" : "Paste Link From Clipboard",
    "2" : "Copy New Link To Clipboard"
}
print(colored("Choose Your Options:", "cyan", attrs=["bold"]))
for items in options:
    print(f"{items} : {options[items]}")
user_option = input(colored(">> ", "yellow", attrs=["bold"]))
if user_option == "1":
    vd_link = pyperclip.waitForPaste()
else:
    vd_link = pyperclip.waitForNewPaste()
print(lines*80)
video = YouTube(vd_link)
print(colored(f"{video.title}", "red", attrs=["bold", "reverse"]))
print(lines*80)
print(colored("Download video (Y / N):", "cyan", attrs=["bold"]))
do_download = input(colored(">> ", "yellow", attrs=["bold"])).lower()
if do_download == "y":
    video_save_path = askdirectory(title='Select Folder To Save')
