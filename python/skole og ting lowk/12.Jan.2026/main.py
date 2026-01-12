alder = input("Hvor gammel er du? ")

try:
    alder = int(alder)
    if alder >= 12:
        print("Gamle faen, hvordan er det å ha beina sine bli om til olje? Dinosaur ahh")
    elif alder < 0:
        print("Du er fortsatt i ballene til faren din")
    else:
        print("Kult")
except ValueError:
    print("Du må skrive inn et tall")

