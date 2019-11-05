import sys, string
# split strings by '.' and convert to numeric.  Append some zeros
# because we need at least 4 digits for the hex conversion.
minver = list(map(int, str.split('2.3', '.'))) + [0, 0, 0]
minverhex = 0
for i in range(0, 4): minverhex = (minverhex << 8) + minver[i]
if sys.hexversion >= minverhex:
    sys.exit( 0 )
else:
    sys.exit( 1 )
