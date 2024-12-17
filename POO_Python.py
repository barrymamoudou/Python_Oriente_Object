#La programmation de oriente object des donnes en python:
class Point :
    #les constructeurs des objects
    nombreCompteur=0
    def __init__ (self ,X,Y) :
        self.x=X,
        self.y=Y

    def deplacer(self,dx,dy):
        self.x=self.x + dx,
        self.y= self.y + dy,


point_3=Point( 5,5 )
point_3.deplacer(2,3)
print(point_3.x)







