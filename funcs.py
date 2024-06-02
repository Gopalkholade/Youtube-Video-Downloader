from pytube import YouTube
import getpass


def fetch(link):    
    try:
        yt = YouTube(link)
        return yt
    except:
        ("Connction Error! try again..")

def check_res(yt):
    streams = yt.streams.filter(file_extension='mp4')
    available_res = list(set([i.resolution for i in streams if i.resolution != None ]))
    return available_res,streams

def download(streams,resolution='360p',save_path=f"C:/Users/{getpass.getuser()}/Downloads"):
    try:
        for i in streams:
            if i.resolution==resolution:
                i.download(output_path=save_path)
                return save_path
    except:
        return ("Error!")