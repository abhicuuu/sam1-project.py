import instaloader

loader = instaloader.Instaloader()

username = input("Enter the Instagram username: ")

loader.download_profile(username,profile_pic_only=False)

for post in loader.get_profile_posts(username):
    loader.download_posts(post,target=username)


