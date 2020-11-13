# Commande de base pour requête SNMP à travers le JSON
cat /etc/snmpower/configuration/configuration.json | jq -r '.[] | 
{versionsnmp: .version, commusnmp: .communaute, ipmachines: .ip} | 
{version: .versionsnmp, communaute: .commusnmp, ip: .ipmachines } | 
.version +" -c "+.communaute+" "+.ip' | 
xargs -L 1 snmpwalk -v &>> ../Logs/all.json

#snmpwalk -v 2c -c $COMMUNITY $IP $OID