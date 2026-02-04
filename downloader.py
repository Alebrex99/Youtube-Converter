from pytubefix import YouTube
import os
import csv

def Download(link, path= os.getcwd()):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Downloading...")
        youtubeObject.download(output_path=path)
        #skip_existing = True; default per evitare di riscaricare video già presenti
        print("Download completed!")
    except Exception as e:
        print("Error:", e)

def main():
    video_dir_out = "C:\\Users\\Alessandro\\VisualStudioCodeProjects\\Youtube-converter\\videos"
    csv_path = "C:\\Users\\Alessandro\\VisualStudioCodeProjects\\Youtube-converter\\prova_estrazione.csv"
    # create a directory to save the downloads if it doesn't exist; put the video inside videos
    if not os.path.exists(video_dir_out):
        os.makedirs(video_dir_out)
        
    #read all the shorts links ids from a csv file
    #for each id found in the csv file, create a right short url and download the video
    if not os.path.exists(csv_path):
        print(f"CSV file not found at {csv_path}. Please enter a YouTube link manually.")
        #create a csv file inserting in input the links, consider that each row has to contain just the short id found inside the url
        with open(csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            while True: #finchè non scrivi "done"
                link = input("Enter a YouTube video link (or type 'done' to finish): ")
                if link.lower() == 'done':
                    break
                writer.writerow([link])
    
    #READ AN EXISTING CSV FILE AND DOWNLOAD THE VIDEOS
    if os.path.exists(csv_path):
        with open(csv_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                #se la row è l'header del csv, saltala
                if row[0] == "videoId":
                    continue
                # the first element of the row is the link
                link = row[0].strip()
                #check if the link is a full link or just an id
                #if "youtube.com" not in link and "youtu.be" not in link: #ho solo l'id
                    #print(f"Detected video ID: {link}")
                link = f"https://www.youtube.com/shorts/{link}"
                Download(link, video_dir_out)
                #else: # è un link completo
                    #print(f"Detected full URL: {link}")
                #    Download(link, video_dir_out)
    
    #link = input("Enter the YouTube video link: ")
    #Download(link, video_dir_out)

if __name__ == "__main__":
    main()# downloader.py