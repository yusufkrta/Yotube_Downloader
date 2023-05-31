import pytube

url = input("Yotube Download Url Enter: ")
storage_space = ""

pytube.YouTube(url).streams.get_audio_only().download(storage_space)


