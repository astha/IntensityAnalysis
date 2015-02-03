#!/bin/bash

declare -A array
i=2
while read word
do 
	
	array[$word]=$i
	((i=$i+1))
done < word_list.csv

while read word
do 
	echo "head -n  ${array[$word]} word_projections-1600.txt | tail -n 1" | /bin/bash
done < example

#for K in "${!array[@]}"; do echo $K --- ${array[$K]}; done
