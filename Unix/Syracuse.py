def syracuse(n):
    a = 0
    b = n
    altimax = b
    altimin = b
    altimoy = b
    d = 0
    dureealtitudemax = 0
    dureealtitudemin = 0
    dureealtitudemoy = 0
    nbduree = 0
    if n == 0:
        print("non")
    elif n <= 0:
        print("non")
    else:
        print(a," ",n)
        while n != 1:
            if (n % 2) == 0:
                n = n//2
                a = a+1
                print(a," ",n)
                if altimax < n:
                    altimax = n
                if altimin > n:
                    altimin = n
                altimoy = altimoy + n
                if b < n:
                    d = d+1
                else:
                    if d > dureealtitudemax:
                        dureealtitudemax = d
                    elif dureealtitudemin > dureealtitudemax:
                        dureealtitudemin = dureealtitudemax
                    dureealtitudemoy = dureealtitudemoy + d
                    if d != 0:
                        nbduree = nbduree + 1
                    d = 0
                    d = 0
            else:
                n = (n*3)+1
                a = a+1
                print(a," ",n)
                if altimax < n:
                    altimax = n
                if altimin > n:
                    altimin = n
                altimoy = altimoy + n
                if b < n:
                    d = d+1
                else:
                    if d > dureealtitudemax:
                        dureealtitudemax = d
                    elif dureealtitudemin > dureealtitudemax:
                        dureealtitudemin = dureealtitudemax
                    dureealtitudemoy = dureealtitudemoy + d
                    if d != 0:
                        nbduree = nbduree + 1
                    d = 0

        altimoy = altimoy//a
        dureealtitudemoy = dureealtitudemoy//nbduree

        print("Durée de vol maximale = ",a)
        print("Durée de vol minimale = ",a)
        print("Durée de vol moyen = ",a//a)
        print("Altitude maximale = ",altimax)
        print("Altitude minimale = ",altimin)
        print("Altitude moyenne = ",altimoy)
        print("Durée de vol maximale en altitude = ",dureealtitudemax)
        print("Durée de vol minimale en altitude = ",dureealtitudemin)
        print("Durée de vol moyen en altitude = ",dureealtitudemoy)

syracuse(11)