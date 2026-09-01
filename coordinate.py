# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

class Point:

    def __init__(self,x,y):
        self.x_cor=x
        self.y_cor=y

    def __str__(self):
        return '<{},{}>'.format(self.x_cor,self.y_cor)

    def eculidean_distance(self,other):
        return ((other.x_cor-self.x_cor)**2 + (other.y_cor-self.y_cor)**2)**0.5

    def origin_distance(self):
        return self.eculidean_distance(Point(0,0))

class Line:
    def __init__(self,A,B,C):
        if A == 0 and B == 0:
            raise ValueError("Invalid line: A and B both cannot be zero.")
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return '{}X + {}Y + {}'.format(self.A,self.B,self.C)
    
    def point_check(line,Point):
        line.general_eq= line.A*Point.x_cor + line.B*Point.y_cor +line.C
        if line.general_eq == 0:
            return "Points lie on the same line"
        else:
            return "Points does not lie on the same line"

    def shortest_distance(line,Point):
        return abs(line.A*Point.x_cor + line.B*Point.y_cor +line.C)/((line.A**2)+(line.B**2))**0.5

    def line_intersect(line1,line2):
        det = (line1.A*line2.B - line2.A*line1.B)
        if  det!= 0:
            return 'The lines intersect at exactly one point'
        else:
            if (line1.A * line2.C == line2.A * line1.C and line1.B * line2.C == line2.B * line1.C):
                return 'lines are coincident, same line infinitely many intersections'
            else:
                return 'lines are parallel(no intersection)'
        

L=Line(1,1,-2)
print(L)
p=Point(1,1)
print(p)
print(L.point_check(p))
print(L.shortest_distance(p))

# h/w TWO lines intersect or not
l1=Line(2,3,-6)
l2=Line(1,-1,1)
print(l1.line_intersect(l2))
l1=Line(2,4,-8)
l2=Line(1,2,5)
print(l1.line_intersect(l2))
l1=Line(1,2,-4)
l2=Line(0,5,0)
print(l1.line_intersect(l2))
