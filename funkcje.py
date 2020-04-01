import numpy

def sr_okr(xy):
    try:
        xy = numpy.array(xy,dtype=float)

        print(xy3)

    except ValueError as err:
        print('wystąpił błąd: ',err, xy)


#sr_okr([[1,2],['a',2]])
sr_okr([[1,2],[3,3],[4,6],[1,5],[2,6],[7,8]])