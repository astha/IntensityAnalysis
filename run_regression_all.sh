#!/bin/bash

#$(python regression.py review rating >results)
for i in $(ls -d */ | cut  -d'/' -f1)
do
	echo "doing $i"
	echo "./run_regression.sh $i" | /bin/bash
done

