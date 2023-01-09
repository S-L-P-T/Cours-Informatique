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
    if [ -z "$3" ] ; then
        touch "$3"
    else
        echo "non"
    fi

    sed -i "s/g=AChanger/g=$1/g" Syracuse.py
    sed -i "s/g!=Changer/g!=$2+1/g" Syracuse.py
    python3 Syracuse.py > $3
    python3 Syracuse.py >> $d
    echo "" >> $d
    sed -i "s/g=$1/g=AChanger/g" Syracuse.py
    sed -i "s/g!=$2+1/g!=Changer/g" Syracuse.py




    sed -i "s/g=AChanger/g=$1/g" Syracuse2.py
    sed -i "s/g!=Changer/g!=$2+1/g" Syracuse2.py
    python3 Syracuse2.py > vols.dat
    sed -i "s/g=$1/g=AChanger/g" Syracuse2.py
    sed -i "s/g!=$2+1/g!=Changer/g" Syracuse2.py

    sed -i "s/Changer1/$1/g" vols.p
    sed -i "s/Changer2/$2/g" vols.p
    gnuplot vols.p
    sed -i "s/$1/Changer1/g" vols.p
    sed -i "s/$2/Changer2/g" vols.p




    sed -i "s/g=AChanger/g=$1/g" Syracuse3.py
    sed -i "s/g!=Changer/g!=$2+1/g" Syracuse3.py
    python3 Syracuse3.py > altitude.dat
    sed -i "s/g=$1/g=AChanger/g" Syracuse3.py
    sed -i "s/g!=$2+1/g!=Changer/g" Syracuse3.py

    gnuplot altitude.p





    sed -i "s/g=AChanger/g=$1/g" Syracuse4.py
    sed -i "s/g!=Changer/g!=$2+1/g" Syracuse4.py
    python3 Syracuse4.py > dureevol.dat
    sed -i "s/g=$1/g=AChanger/g" Syracuse4.py
    sed -i "s/g!=$2+1/g!=Changer/g" Syracuse4.py

    gnuplot dureevol.p






    sed -i "s/g=AChanger/g=$1/g" Syracuse5.py
    sed -i "s/g!=Changer/g!=$2+1/g" Syracuse5.py
    python3 Syracuse5.py > dureealtitude.dat
    sed -i "s/g=$1/g=AChanger/g" Syracuse5.py
    sed -i "s/g!=$2+1/g!=Changer/g" Syracuse5.py

    gnuplot dureealtitude.p
fi