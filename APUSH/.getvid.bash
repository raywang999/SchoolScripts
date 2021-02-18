#!/bin/bash
file=`cat playlist.m3u8`
#echo "${#file}"
IFS=$'\n'
read -rd '' -a ADDR <<< "$file"
currtime=0.0
for i in "${ADDR[@]}"; do
	if [ ${i:0:8} == "#EXTINF:" ];
	then
		currtime=($currtime+${i:8:8}))
		echo $currtime
	fi
done
IFS=' '
