aws cloudwatch put-metric-data --metric-name PumpPiUptime.cron --namespace Pumper --unit Seconds --value $(cat /proc/uptime | cut -d" " -f1)
sudo hologram send --topic uptime "{\"uptime\": $(cat /proc/uptime | cut -d" " -f1)}"

