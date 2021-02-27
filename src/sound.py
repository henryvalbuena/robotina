import subprocess
import platform

from logger import logging

logger = logging.getLogger(f"robotina.{__name__}")
sound_lib_path = "/media/ext-drive/Roy/Downloads/sounds/"
sound_li_ls = {
    "sleep": sound_lib_path + "sl_eight_h_sound.mp4"
}


def play_song(audio_file):
    sys = platform.system()

    if sys == 'Darwin':
        process = subprocess.Popen(f"afplay {sound_li_ls[audio_file]}", shell=True)
    else:
        process = subprocess.Popen(
            f"ffplay -nodisp -autoexit {sound_li_ls[audio_file]} > /dev/null 2>&1", shell=True
        )

    logger.info(f"play_song subprocess {process}")

    return process


def stop_song(process):
    sys = platform.system()

    process.terminate()
    process.wait()

    if sys == "Linux":
        subprocess.Popen("pkill ffplay", shell=True)

    logger.info(f"Subprocess {process} ended")


def tts(text):
    if isinstance(text, str):
        msg = subprocess.run(
            f"espeak {text}", capture_output=True, shell=True
        )

        if msg.returncode < 1:
            return "speaking.."
        else:
            return msg.stderr.decode("utf-8")
