#!/bin/bash
echo "git again start!"
echo "It will bring back everything that not added"
cd ..
echo "deleting new files..."
git clean -df
echo "restore modify and deleted files..."
git checkout .
echo "git again end!"