
cat $FILMS_JOINED |
echo \"Comedy\"   | # replace with a jq command
python $TODO_SORT |
uniq -c           |
sort -r -n        |
head -n 5
