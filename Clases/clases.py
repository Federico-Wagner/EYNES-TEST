from math import pi, sqrt

class circulo:
    def __init__(self, radio):
        """ Constructor method will evaluate if valid input were passed as arguments """
        if (radio <= 0):
            raise Exception('El radio debe ser mayor a cero')
        else:
            self.radio = radio
            self.editable =  True

    def __str__(self):
        def printPattern(radius):
            """ Implements the logic for printing the object representation """
            for i in range((2 * radius)+1):
                for j in range((2 * radius)+1):
                    dist = sqrt((i - radius) * (i - radius) +
                        (j - radius) * (j - radius))
                    if (dist > radius - 0.5 and dist < radius + 0.5):
                        print("*",end="")
                    else:
                        print(" ",end="")	
                print()
        printPattern(self.radio)
        return( 'Objeto Circulo: \n' +
                f' - Diametro: {self.radio}\n'+
                f' - Editable: {self.editable}\n')

    def __mul__(self, multiplier):
        """ Method returns an object of the same class with modified radius """
        if (multiplier > 0):
            return circulo(self.radio * multiplier)

    def area(self):
        """ Method returns the area of the object """
        return round(self.radio**2 * pi, 2)

    def perimetro(self):
        """ Method returns the perimeter of the object """
        return round(self.radio * 2 * pi, 2)

    def setRadius(self, newRadius):
        """ Set method to modify the radius object attribute """
        if (newRadius > 0 and self.editable):
            self.radio = newRadius
        else:
            self.editable = False
            print("El circulo no pudo ser modificado")


# circulo1 = circulo(3)         #TEST
# circulo2 = circulo1 * 2       #TEST
# print(circulo1.area())        #TEST
# print(circulo1.perimetro())   #TEST


# print(circulo1)               #TEST
# print(circulo2)               #TEST
