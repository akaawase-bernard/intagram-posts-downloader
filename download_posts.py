import instaloader

def download_posts():
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Login if required (optional)
        # loader.login("your_username", "your_password")

        # Request the Instagram username from the user
        username = input("Enter the Instagram username: ")

        # Retrieve the profile object of the specified username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Iterate over the profile's posts and download them
        for post in profile.get_posts():
            loader.download_post(post, target=profile.username)

        print("Download complete!")

    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

# Usage
download_posts()
