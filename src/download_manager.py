import urllib.request
import urllib
import json
from pathlib import Path
import zipfile
import os
import sys
from email_manager import send_email
import shutil

# <-TODO->
# TODO: date range
# TODO: status tracker - i.e. count of how many done / how many
# TODO: post this on redit
# TODO: add actual metadata to files
# TODO: log of downloads in .txt file
# TODO: error handling for if the file uploaded is not correct
# TODO: add a page for status or something after user submits

# <-FIXME->
# FIXME: how does this work with multiple simultaneous requests?
# FIXME: security, i.e. plaintext password in email manager

# <-BUG->
# BUG: mp4 download doesn't work
# BUG: submitting with /#first, etc fails

# Path to uploaded json files
UPLOADS_PATH = "uploads/"

# Download the media file
def download_url(url, file_path, type, date, time):
    name = "Snapchat-{}__{}".format(date, time)
    if type == "PHOTO":
        name += ".jpg"
    elif type == "VIDEO":
        name += ".mp4"
    else:
        print("Type {} not supported.".format(type)) # Ideally doesn't happen lol

    try:
        urllib.request.urlretrieve(url, file_path + name)
        print("[.] Download success - {}".format(name))
    except:
        print("[x] Download failed - {}".format(name))

def check_duplicates():
    pass

def process_json(memories_path, FILE_PATH):
    with open(memories_path) as fd:
        data = json.load(fd)
        saved_media = data["Saved Media"]

        count = 0
        size = len(saved_media)
        print(size)

        for memory in saved_media:
            timestamp = memory["Date"]
            year, month, day = timestamp[0:4], timestamp[5:7], timestamp[8:10]
            date = "{}-{}-{}".format(year, month, day)
            time = "{}-{}-{}".format(timestamp[11:13], timestamp[14:16], timestamp[17:19])

            # Create nested file directory in FILE_PATH/year/month
            media_path = FILE_PATH + year + "/" + month + "/"
            Path(media_path).mkdir(parents=True, exist_ok=True)

            # Increment file count for status
            count += 1

            # Download file
            download_url(url = memory["Download Link"], file_path = media_path, type = memory["Media Type"], date = date, time = time)

# Zip directory of images
def zipdir(path, ziph):
    # Ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

# TODO: delete in upload folder too
def reset(FILE_PATH, ZIP_PATH):
    # Delete zip file
    try:
        os.remove(ZIP_PATH + 'snapchat_memories.zip')
    except:
        print("Error finding/deleting {}.".format(ZIP_PATH + 'snapchat_memories.zip'))

    # Delete downloaded media files
    try:
        shutil.rmtree(FILE_PATH)
        shutil.rmtree(ZIP_PATH)
    except:
        print("Error deleting directory")

def snapchat_downloader(memories_path, receiver_email):
    # Path to extracted images, initialized in snapchat_downloader w/ user email
    FILE_PATH = "downloads/"
    # Path to all the zip files ready to send
    ZIP_PATH = "zips/"
    # Create unique directories indexed by email for downloads and zip files
    FILE_PATH += "{}/".format(receiver_email)
    ZIP_PATH += "{}/".format(receiver_email)

    process_json(memories_path, FILE_PATH)


    Path(ZIP_PATH).mkdir(parents=True, exist_ok=True)

    # Create a zip file in the zips/ directory
    zipf = zipfile.ZipFile(ZIP_PATH + 'snapchat_memories.zip', 'w', zipfile.ZIP_DEFLATED)
    # Compress directory with downloaded files
    zipdir(FILE_PATH, zipf)
    zipf.close()

    # Send the email with the downloads
    send_email(receiver_email, ZIP_PATH + "snapchat_memories.zip")

    # Delete all data from this session and reset global vars
    reset(FILE_PATH, ZIP_PATH)
    FILE_PATH = "downloads/"
    ZIP_PATH = "zips/"

if __name__=="__main__":
    memories_path = input("Input path to memories: ")
    receiver_email = input("Input receiver email: ")
    snapchat_downloader(memories_path, receiver_email)
