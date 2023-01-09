set terminal png size 500,500

set output 'altitude.png'

set title 'Altitude maximum atteinte en fonction de U0'

plot "altitude.dat" u 1:2 w l