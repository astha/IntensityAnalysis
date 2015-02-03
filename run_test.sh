#!/bin/bash

rm -f example_vectors
while read word
do 
	name=$word
	echo "grep -i -m1 '^$name ' word_projections-1600.txt >> example_vectors" | /bin/bash
done < example

# python try.py example_vectors