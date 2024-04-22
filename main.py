
# Video downloader for YouTube

from pytube import YouTube
import os

def download_video(url, output_path=None):
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"\rDownloading... {percentage:.2f}%", end="", flush=True)

    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        if resolution:
            stream = yt.streams.filter(
                res=resolution).first()
        else:
            stream = yt.streams.get_highest_resolution()

        output_path = os.path.join(os.path.expanduser("~"), "Downloads")

        filename = stream.default_filename
        filepath = os.path.join(output_path, filename)
        counter = 1
        while os.path.exists(filepath):
            counter += 1
            base_filename, file_extension = os.path.splitext(filename)
            filename = f"{base_filename} ({counter}){file_extension}"
            filepath = os.path.join(output_path, filename)
        print(f"* File will be downloaded in {output_path} folder")
        stream.download(output_path, filename=filename)
        print(" Video successfully downloaded!")
        os.startfile(filepath)

    except Exception as e:
        print("An error occurred while downloading the video:", e)

if __name__ == "__main__":
    url = input("Enter the URL of the YouTube video: ")
    resolution = input("Enter the desired video quality (144p/240p/360p/480p/720p/...)\n(or press Enter to select the highest quality): ")

    download_video(url)
