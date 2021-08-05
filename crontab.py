CRON_TZ=Japan

25 12 * * 1-5 sh /home/pi/Alarm/lunchAlarm.sh
15 13 * * 1-5 sh /home/pi/Alarm/StartPM.sh

0 10,11,14-16 * * 1-5 sh /home/pi/Alarm/windowOpen.sh
5 10,11,14-16 * * 1-5 sh /home/pi/Alarm/windowClose.sh


