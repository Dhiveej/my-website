# SCREEN


from flask import Flask, request, render_template, redirect, url_for, flash
import yt_dlp
import validators
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')

    if not url:
        flash("Please enter a URL.")
        return redirect(url_for('index'))

    if not validators.url(url):
        flash("Invalid URL. Please enter a valid video URL.")
        return redirect(url_for('index'))

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best/bestvideo[ext=webm]/bestvideo', # Modified format string
        'outtmpl': 'D:/Project/%(title)s.%(ext)s',
        'nopart': True,
        'no_continue': True,
        'retries': 3,
        'merge_output_format': 'mp4', # Force output to mp4 after merge
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False) # Extract info first
            if info_dict is not None:
                ydl.download([url])
                flash('Download complete.')
            else:
                flash("Could not extract video information.")

    except yt_dlp.utils.DownloadError as e:
        flash(f"A download error occurred: {str(e)}")
    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)