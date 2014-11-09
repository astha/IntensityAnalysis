#!/bin/bash

rm -f $1/positive
rm -f $1/negative

echo "Finding Positive Adjective Vectors ..."
while read word
do 
	name=$word
	echo "grep -i -m1 '^$name ' word_projections-1600.txt >> $1/positive" | /bin/bash
done < $1/adj_pos

echo "Finding Negative Adjective Vectors ..."
while read word
do 
	name=$word
	echo "grep -i -m1 '^$name ' word_projections-1600.txt >> $1/negative" | /bin/bash
done < $1/adj_neg

echo "Running pagerank algorithm now ..."
python pagerank.py $1/positive $1/negative > $1/results
