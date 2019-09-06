#!/bin/bash
echo "git push news start!"
cd ..
git add .
git commit -m "update news"
echo "submit comments : update news"
git push origin master
echo "git push news end!"