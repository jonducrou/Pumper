if [ ! -z "$(ifconfig | grep wwan0)" ] ; 
then 
  sudo ifconfig wlan0 down
else
  sudo ifconfig wlan0 up
fi

