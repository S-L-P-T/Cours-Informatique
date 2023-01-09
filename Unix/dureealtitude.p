set terminal png size 500,500

set output 'dureealtitude.png'

set title 'Duree de vol en altitude en fonction de U0'

plot "dureealtitude.dat" u 1:2 w l