import yt_dlp # This line imports the yt_dlp library, which is a tool for downloading videos from YouTube and other sites.

def download_video(url): # This line defines a new function named download_video that takes one parameter, url, which is the URL of the YouTube video you want to download.
    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': 'D:/Project/%(title)s.%(ext)s',  # Change this to your desired folder
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # This line creates an instance of YoutubeDL with the options specified in ydl_opts. It uses a context manager (with statement) to ensure proper setup and teardown.
        ydl.download([url])  # This line downloads the video from the given URL.
        print("Download completed successfully.")  # This line prints a success message when the download is complete.

# Example usage
url = "https://www.youtube.com/watch?v=yryIJGVOovU"  # This is an example YouTube video URL.
download_video(url)  # This line calls the download_video function with the provided URL.
