echo HelloWorld


snmpwalk -v 2c -c $COMMUNITY $IP $OID > snmpower.log
