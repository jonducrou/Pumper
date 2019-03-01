aws cloudwatch put-metric-data --metric-name PumpPiUptime --namespace Pumper --unit Seconds --value $(cat /proc/uptime | cut -d" " -f1)
