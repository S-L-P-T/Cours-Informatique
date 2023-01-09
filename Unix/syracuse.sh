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
    python3 Syracuse.py > $2
    echo "n=$1" >> $d
    echo "" >> $d
    python3 Syracuse.py >> $d
    echo "" >> $d
    sed -i "s/syracuse($1)/syracuse(Changer)/g" Syracuse.py

    sed -i "s/Changer/$2/g" plot.p
    gnuplot plot.p
    sed -i "s/$2/Changer/g" plot.p





    sed -i "s/for g in range(Changer)/for g in range($1+1)/g" Syracuse2.py
    python3 Syracuse2.py > vols.dat
    sed -i "s/for g in range($1+1)/for g in range(Changer)/g" Syracuse2.py

    sed -i "s/Changer/$2/g" vols.p
    gnuplot vols.p
    sed -i "s/$2/Changer/g" vols.p





    sed -i "s/for g in range(Changer)/for g in range($1+1)/g" Syracuse3.py
    python3 Syracuse3.py > altitude.dat
    sed -i "s/for g in range($1+1)/for g in range(Changer)/g" Syracuse3.py

    sed -i "s/Changer/$2/g" altitude.p
    gnuplot altitude.p
    sed -i "s/$2/Changer/g" altitude.p





    sed -i "s/for g in range(Changer)/for g in range($1+1)/g" Syracuse4.py
    python3 Syracuse4.py > dureevol.dat
    sed -i "s/for g in range($1+1)/for g in range(Changer)/g" Syracuse4.py

    sed -i "s/Changer/$2/g" dureevol.p
    gnuplot dureevol.p
    sed -i "s/$2/Changer/g" dureevol.p






    sed -i "s/for g in range(Changer)/for g in range($1+1)/g" Syracuse5.py
    python3 Syracuse5.py > dureealtitude.dat
    sed -i "s/for g in range($1+1)/for g in range(Changer)/g" Syracuse5.py

    sed -i "s/Changer/$2/g" dureealtitude.p
    gnuplot dureealtitude.p
    sed -i "s/$2/Changer/g" dureealtitude.p
fi