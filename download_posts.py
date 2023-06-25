import instaloader
import os
import shutil

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_file(src, dst):
    shutil.move(src, dst)

def download_posts():
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Request the Instagram username from the user
        username = input("Enter the Instagram username: ")

        # Retrieve the profile object of the specified username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Create a folder based on the username
        create_folder(username)

        # Iterate over the profile's posts and download them
        for post in profile.get_posts():
            loader.download_post(post, target=profile.username)

        print("Download complete!")

        # Create folders for different file types
        create_folder(username + "/images")
        create_folder(username + "/videos")
        create_folder(username + "/other")

        # Move downloaded files to the appropriate folders
        for filename in os.listdir(username):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                move_file(os.path.join(username, filename), os.path.join(username, "images", filename))
            elif filename.endswith(".mp4"):
                move_file(os.path.join(username, filename), os.path.join(username, "videos", filename))
            else:
                move_file(os.path.join(username, filename), os.path.join(username, "other", filename))

        print("File sorting complete!")

    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

# Usage
download_posts()
