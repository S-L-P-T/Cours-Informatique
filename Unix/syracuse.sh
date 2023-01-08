#!/bin/bash

#Variables

d="synthese-min-max.txt"
e=$(find "$d" )

#Script

if [ -z "$e" ] ; then
    touch "$d"
else
    echo "non"
fi

if [ $z -eq 0 ] ; then
    echo "non"
else
    if [ -z "$2" ] ; then
        touch "$2"
    else
        echo "non"
    fi
    sed -i "s/syracuse(Changer)/syracuse($1)/g" Syracuse.py
    python3 Syracuse.py >> $2
    echo "n=$1" >> $d
    echo "" >> $d
    python3 Syracuse.py >> $d
    echo "" >> $d
    sed -i "s/syracuse($1)/syracuse(Changer)/g" Syracuse.py

    sed -i "s/Changer/$2/g" plot.p
    gnuplot plot.p
    sed -i "s/$2/Changer/g" plot.p
fi