#coding: utf-8

import time
import subprocess

def main():
    subprocess.call("amixer set PCM 90%", shell=True)
    subprocess.call("mpg321 /home/pi/Alarm/soundFiles/Japanese_School_Bell01-2.mp3", shell=True)

    #speechString = "お昼休みの時間が終わりました"
    #command = "echo \"%s\"" % speechString
    #command += " | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/mei/mei_normal.htsvoice -ow /dev/stdout"
    #command += " | aplay --quiet"

    #prc = subprocess.Popen(
    #    command,
    #    shell = True,
    #    stdin = subprocess.PIPE,
    #    stdout = subprocess.PIPE,
    #    stderr = subprocess.PIPE)

if __name__ == "__main__":
    main()
