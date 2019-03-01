aws cloudwatch put-metric-data --metric-name PumpPiUptime --namespace Pumper --value $(cat /proc/uptime | cut -d" " -f1)
