import math
from math import sqrt
# from math import * - Don't use this
from math import sqrt as squareroot
import math as m

def main():
    print(math.sqrt(9))  # uses import math
    print(sqrt(16))      # uses from math import sqrt
    print(squareroot(25)) # uses from math import sqrt as squareroot
    print(m.sqrt(36))    # uses import math as m



if __name__ == '__main__':
    main()
