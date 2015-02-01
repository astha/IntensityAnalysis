#!/bin/bash

# for file in ./RakshaList/*
# do
#   echo "python pre_process.py $file > astha" | /bin/bash
#   mv astha $file
# done


# rm -rf vectors
# mkdir vectors
# mkdir vectors/RakshaList
# for file in ./RakshaList/*
# do
#   echo "Finding Adjective Vectors : $file" 
#   while read word
#   do 
#     name=$word
#     echo "grep -i -m1 '^$name ' word_projections-1600.txt >> vectors/${file}"  | /bin/bash
#   done < $file
# done



# echo "Finding Negative Adjective Vectors ..."
# while read word
# do 
#   name=$word
#   echo "grep -i -m1 '^$name ' word_projections-1600.txt >> $1/negative" | /bin/bash
# done < $1/adj_neg

# echo "Running pagerank algorithm now ..."
# python pagerank.py $1/positive $1/negative > $1/results

for file in vectors/RakshaList/*
do
  echo "python matrix.py $file > astha" | /bin/bash
  mv astha final/$file
done

