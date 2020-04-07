import math

#ax^2+bx+c

def solve(input):
    try:
        input = str(input)
        
        #Get a
        a = int(input.split("x")[0])
        print ("a: ",a)

        #Get b
        b= input.split("x")[1].split("^2")[1]
        if(b[0]=="+"):
            b = int(str(input.split("x")[1].split("^2")[1].replace("+","")))
            print ("b: ",b)
        else:
            b = int(input.split("x")[1].split("^2")[1])
            print ("b: ",b)


        c = input.split("x")[2]
        if(c[0]=="+"):
            c = int(str(input.split("x")[2].replace("+","")))
            print ("c: ",c)
        else:
            c=int(c)
            print ("c: ",c)

        tempabovepos = int(-b+math.sqrt(b**2-4*a*c))
        tempaboveneg = int(-b-math.sqrt(b**2-4*a*c))

        xone = float(tempabovepos/(2*a))
        xtwo = float(tempaboveneg/(2*a))

        print(tempabovepos)
        print(tempaboveneg)

        if(".0" in str(xone)):
            xone = int(xone)
        if(".0" in str(xtwo)):
            xtwo = int(xtwo)

        if(isPos(xone)):
            xone = "+",xone
        if(isPos(xtwo)):
            xtwo = "+",xtwo

        xone = str(xone)
        xtwo = str(xtwo)

        xone = xone.replace("(","").replace(")","")
        xtwo = xtwo.replace("(","").replace(")","")

        xone = xone.replace("'","").replace("'","").replace(",","").strip()
        xtwo = xtwo.replace("'","").replace("'","").replace(",","").strip()

        print("(x",xone,") or (x",xtwo,")")

        
    except Exception as ex:
        print("Error: "+str(ex))
        pass

def isPos(inp):
    if(inp>0 and inp!=0):
        return True
    else:
        return False




inp = input("Please enter your equation: ")
solve(inp)

#3x^2+10x+8
