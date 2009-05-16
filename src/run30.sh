#!/bin/bash

while true
do
	LINE=`python main.py`
	LLINE=`tail -n1 "$1"`
	if [ "$LINE" != "$LLINE" ]
	then
		echo "$LINE" >> "$1"
	fi
	sleep 1800
done
