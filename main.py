from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error: Could not download YouTube Video")
    print("Your download is complete.")

link = input("Insert YouTube link here: ")
Download(link)
