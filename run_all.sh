#!/bin/bash

for i in $(ls -d */ | cut  -d'/' -f1)
do
	echo "doing $i"
	echo "./run.sh $i" | /bin/bash
done

