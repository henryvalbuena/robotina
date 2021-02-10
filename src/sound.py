import subprocess
import platform

from logger import logging

logger = logging.getLogger(f"robotina.{__name__}")


def play_song(audio_file):
    sys = platform.system()

    if sys == 'Darwin':
        process = subprocess.Popen("afplay ./src/sounds/synthwave_cool.mp3", shell=True)
    else:
        process = subprocess.Popen(
            "ffplay -nodisp -autoexit ./src/sounds/synthwave_cool.mp3", shell=True
        )

    logger.info(f"play_song subprocess {process}")

    return process


def stop_song(process):
    process.terminate()
    process.wait()

    logger.info(f"Subprocess {process} ended")
