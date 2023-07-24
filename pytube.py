def Download(youtube,link):
    youtubeObject = youtube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the Youtube video URL: ")
Download(link)