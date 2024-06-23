#!/usr/bin/env python3
from pytube import YouTube
from rich.progress import SpinnerColumn, Progress, TextColumn
from time import sleep
import typer
import os
from typing_extensions import Annotated, Optional

def Download(link) -> str:
    try: 
        youtubeObject = YouTube(link)
        name = youtubeObject.title
        print("Retrieved Video:", name)
    except:
        print("link", link, "does not exist")

    video = youtubeObject.streams.get_highest_resolution()
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        desc = "Processing " + name + "..."
        progress.add_task(description=desc, total = None)
        video.download()
    return title

def main(
    link: Annotated[str, typer.Argument()],
    path: Annotated[Optional[str], typer.Argument] = os.getcwd(),
    fname: Annotated[Optional[str], typer.Argument] = None
    ):

    print("link", link)
    print("path", path)
    print("fname", fname)
    # title = Download(link)
    
    # download_fname= title + ".mp4"
    if fname != None:
        download_fname= fname + ".mp4"

    # os.rename(os.getcwd() + "/" +  download_fname, path + "/" + download_fname)

if __name__ == "__main__":
    typer.run(main)

