#coding: utf-8

import subprocess

def main():
    subprocess.call("amixer -c 0 sset PCM 100%", shell=True)
    subprocess.call("mpg321 /home/pi/Alarm/soundFiles/Chime-Announce06-3.mp3", shell=True)
    subprocess.call("amixer -c 0 sset PCM 90%", shell=True)

    speechString = "換気の時間です。窓を開けましょう。"
    command = "echo \"%s\"" % speechString
    command += " | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/mei/mei_normal.htsvoice -ow /dev/stdout"
    command += " | aplay --quiet"

    prc = subprocess.Popen(
        command,
        shell = True,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)

if __name__ == "__main__":
    main()
