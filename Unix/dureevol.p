set terminal png size 500,500

set output 'dureevol.png'

set title 'Duree de vol en fonction de U0'

plot "dureevol.dat" u 1:2 w l