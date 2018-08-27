#!/bin/bash


modifyfile(){
for FILENAME in `ls | grep ^[0-9][0-9][0-9].[jJ][pP][gG] -`; 
	do mv -v $FILENAME `echo $FILENAME | grep ^[0-9][0-9][0-9] - -o`.jpg ;
done
}

traverse(){
	for NAME in `ls`; do
		if is_directory "$NAME"; then 
			echo "Entering $NAME"
			cd "$NAME"
			traverse
			cd ..
		fi
		modifyfile
	done
}

is_directory()
{
  DIR_NAME=$1
  if [ ! -d $DIR_NAME ]; then
    return 1
  else
    return 0
  fi
}

traverse
