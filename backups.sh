#!/bin/bash

DATE=`date +%d-%m-%Y`
HOSTNAME=$(hostname)

mkdir /var/backup/$HOSTNAME/$DATE

exec > /var/backup/$HOSTNAME/$DATE/$DATE-backup.log 2>&1

xe vm-list | grep -P 'uuid' | sed -r 's/^[^:]+//' | sed 's/^..//' >> /var/backup/$HOSTNAME/$DATE/uuid-vms.txt

for UUID_VM in $(cat /var/backup/$HOSTNAME/$DATE/uuid-vms.txt)

do 
UUID_SNAPHOTS=$(xe vm-snapshot uuid="$UUID_VM" new-name-label=$DATE-"$UUID_VM") 
VM_NAMES=$(xe vm-param-list uuid="$UUID_VM" | grep name-label | sed -r 's/^[^:]+//' | sed 's/^..//') 

xe template-param-set is-a-template=false ha-always-run=false uuid="$UUID_SNAPHOTS" 
xe vm-export uuid="$UUID_SNAPHOTS" filename=/var/backup/$HOSTNAME/$DATE/"$DATE-$VM_NAMES.xva"
xe vm-uninstall uuid=$UUID_SNAPHOTS force=true
#echo $UUID_VM
echo $VM_NAMES
echo "========================================================================"

done

