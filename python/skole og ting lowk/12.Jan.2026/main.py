import time

alder = input("Hvor gammel er du? ")

try:
    alder = int(alder)
    if alder >= 12 and alder != 14 and alder != 15 and alder != 29:
        print("Gamle faen, hvordan er det å ha beina sine bli om til olje? Dinosaur ahh")
    elif alder < 0:
        print("Du er fortsatt i ballene til faren din")
    elif alder == 15:
        print("kalkulerer...")
        time.sleep(5)
        print("Du heter Sverre")
    elif alder == 14:
        print("kalkulerer...")
        time.sleep(5)
        print("Du heter Anne")
    elif alder == 29:
        print("kalkulerer...")
        time.sleep(5)
        print("Du heter Stian")
    else:
        print("Js a bebeh #so_tuff")
except ValueError:
    print("Du må skrive inn et tall")
