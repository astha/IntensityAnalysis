rm -f $1/positive_regression
rm -f $1/negative_regression

echo "Finding Positive Adjective Vectors ..."
while read word
do 
	name=$word
	echo "grep -i -m1 '^$name ' results >> $1/positive_regression" | /bin/bash	
done < $1/adj_pos

echo "Finding Negative Adjective Vectors ..."
while read word
do 
	name=$word
	echo "grep -i -m1 '^$name ' results >> $1/negative_regression" | /bin/bash
done < $1/adj_neg

python evaluate_regression.py $1/positive_regression 1 > $1/positive_regression_result
python evaluate_regression.py $1/negative_regression 0 > $1/negative_regression_result