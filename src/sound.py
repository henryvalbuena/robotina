import subprocess

from logger import logging

logger = logging.getLogger(f"robotina.{__name__}")


def play_song(audio_file):
    try:
        process = subprocess.Popen("afplay ./src/sounds/synthwave_cool.mp3", shell=True)
    except:
        process = subprocess.Popen(
            "ffplay -nodisp -autoexit ./src/sounds/synthwave_cool.mp3", shell=True
        )

    logger.info(f"play_song subprocess {process}")

    return process


def stop_song(process):
    process.terminate()
    process.wait()

    logger.info(f"Subprocess {process} ended")
