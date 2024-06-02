import sys
from funcs import download, fetch, check_res
# link = "https://www.youtube.com/watch?v=y2BaTt1fxJU&t=17s"


if __name__=='__main__':
    input_link = str(input("Paste link Here:"))
    yt = fetch(link=input_link)

    avail_res, stream = check_res(yt=yt)
    if len(sys.argv)>2:
        raise IndexError("Multiple Arguments Given. Required 1 for resolution")
    res = sys.argv[-1]
    if res in avail_res:
        download(streams=stream, resolution=res)
    else:
        print(f"""Given argument for resolution not available. Enter from resulution available :{', '.join(avail_res)}""")