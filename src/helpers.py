import subprocess

from logger import logging

logger = logging.getLogger(f"robotina.{__name__}")


def load_module_bluetooth():
    msg = subprocess.run(
        "pactl load-module module-bluetooth-discover", capture_output=True, shell=True
    )
    logger.info(msg)
    if msg.returncode < 1:
        return "BT loaded"
    else:
        return msg.stderr.decode("utf-8")


def default_to_bluetooth():
    msg = subprocess.run(
        "pacmd set-default-sink bluez_sink.08_EB_ED_79_EF_8A.a2dp_sink",
        capture_output=True,
        shell=True,
    )
    logger.info(msg)
    if msg.returncode < 1:
        return "BT default"
    else:
        return msg.stderr.decode("utf-8")


def restart_pulseaudio():
    kill = subprocess.run("pulseaudio -k", capture_output=True, shell=True,)
    logger.info(kill)
    start = subprocess.run("pulseaudio --start", capture_output=True, shell=True,)
    logger.info(start)

    if kill.returncode < 1 and start.returncode < 1:
        return "pulseaudio restarted"
    elif kill.returncode > 0:
        return kill.stderr.decode("utf-8")
    else:
        return start.stderr.decode("utf-8")
