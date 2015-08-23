import string, sys
strr = sys.argv[1]
caesar = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "DEFGHIJKLMNOPdefghijklmnopQRSTUVWXYZABCqrstuvwxyzabc")
print strr.translate(caesar)