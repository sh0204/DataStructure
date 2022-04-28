def printPoly(p_x) :
    polyStr = "P(x) = "

    for i in range(len(p_x[0])) :
        term = p_x[0][i]
        coef = p_x[1][i]
        
        if (coef >= 0) :
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
            
    return polyStr

def calcPoly(xVal, p_x) :
    retValue = 0
    
    for i in range(len(p_x[0])) :
        term = p_x[0][i]
        coef = p_x[1][i]
        retValue += coef * xValue ** term
        term -= 1
        
    return retValue

px = [[300, 20, 0],
      [7, -4, 5]]

if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)
    
    xValue = int(input("X 값-->"))
    
    pxValue = calcPoly(xValue, px)
    print(pxValue)
        