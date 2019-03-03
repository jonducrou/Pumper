if [ ! -z "$(/sbin/ifconfig | grep wwan0)" ] ; 
then 
  sudo /sbin/ifconfig wlan0 down
else
  sudo /sbin/ifconfig wlan0 up
fi

