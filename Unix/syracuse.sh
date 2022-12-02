#!/bin/bash

#Variables
n="$1"
z="$n"
a=0
b=0
c=0
altimax="$z"
altimin="$z"
altimoy="$z"
dureevolmoy="$a"
dureealtitudemin=''
dureealtitudemoy=0
nbdureealtitude=0
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
    touch "$2"
    echo "n Un" > "$2"
    echo "$a $z" >> "$2"
    while [ $z -ne 1 ]
    do
        if [ $(( z % 2 )) -eq 0 ] ; then
            z=$(( z / 2 ))
            a=$(( a + 1 ))
            dureevolmoy=$(( dureevolmoy + a ))
            altimoy=$(( altimoy + z ))
            echo "$a $z" >> "$2"
            if (( z > altimax )) ; then
                altimax="$z"
            fi
            if (( z < altimin )) ; then
                altimin="$z"
            fi
            if (( z >= n )) ; then
                b=$(( b + 1 ))
            else
                if (( b > c )) ; then
                    c="$b"
                    nbdureealtitude=$(( nbdureealtitude + 1 ))
                    dureealtitudemoy=$(( dureealtitudemoy + b ))
                elif [ -z "$dureealtitudemin" ] ; then
                    dureealtitudemin="$b"
                elif (( b < dureealtitudemin )) ; then
                    dureealtitudemin="$b"
                    nbdureealtitude=$(( nbdureealtitude + 1 ))
                    dureealtitudemoy=$(( dureealtitudemoy + b ))
                fi
                b=0
            fi
        else
            z=$(( z * 3 + 1 ))
            a=$(( a + 1 ))
            dureevolmoy=$(( dureevolmoy + a ))
            altimoy=$(( altimoy + z ))
            echo "$a $z" >> "$2"
            if (( z > altimax )) ; then
                altimax="$z"
            fi
            if (( z < altimin )) ; then
                altimin="$z"
            fi
            if (( z >= n )) ; then
                b=$(( b + 1 ))
            else
                if (( b > c )) ; then
                    c="$b"
                    nbdureealtitude=$(( nbdureealtitude + 1 ))
                    dureealtitudemoy=$(( dureealtitudemoy + b ))
                elif [ -z "$dureealtitudemin" ] ; then
                    dureealtitudemin="$b"
                elif (( b < dureealtitudemin )) ; then
                    dureealtitudemin="$b"
                    nbdureealtitude=$(( nbdureealtitude + 1 ))
                    dureealtitudemoy=$(( dureealtitudemoy + b ))
                fi
                b=0
            fi
        fi
    done
    dureevolmoy=$(( dureevolmoy / a ))
    altimoy=$(( altimoy / a ))
    if (( nbdureealtitude == 0 )) ; then
        dureealtitudemoy=0
    else
        dureealtitudemoy=$(( dureealtitudemoy / nbdureealtitude ))
    fi
    echo "n=$n" >> "$d"
    echo "" >> "$d"
    echo "altimax=$altimax" >> "$2"
    echo "altimax=$altimax" >> "$d"
    echo "altimin=$altimin" >> "$d"
    echo "altimoy=$altimoy" >> "$d"
    echo "dureevol=$a" >> "$2"
    echo "dureevolmax=$a" >> "$d"
    echo "dureevolmin=$a" >> "$d"
    echo "dureevolmoy=$dureevolmoy" >> "$d"
    echo "dureealtitude=$c" >> "$2"
    echo "dureealtitudemax=$c" >> "$d"
    echo "dureealtitudemin=$dureealtitudemin" >> "$d"
    echo "dureealtitudemoy=$dureealtitudemoy" >> "$d"
    echo "" >> "$d"

    sed -i "s/Changer/$2/g" plot.p
    gnuplot plot.p
    sed -i "s/$2/Changer/g" plot.p
fi
