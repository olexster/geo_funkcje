import pandas as pd
from pyproj import Transformer
import math
#import csv

"""definicje trnasformacji   
    2180 - Poland CS92
    2178 - Poland CS2000 zone 7 
    """
transformacja = Transformer.from_crs(2180, 2178)
tt = transformacja.transform
trans2000na192 = Transformer.from_crs(2178, 2180)
tt2 = trans2000na192.transform
root_path = 'C:/Users/olexs/PycharmProjects/model_1992_na_2000/'


def godlo_2000_10k(u2000):
	"""funkcja oblicza godłu w układzie 2000
        (x2000, y2000)
        """
	godlo_1 = math.floor(u2000[0] / 1e6)
	godlo_2 = math.floor((u2000[0] / 1e3 - 4920) / 5)
	godlo_3 = math.floor(((u2000[1] - godlo_1 * 1e6) / 1e3 - 332) / 8)
	godlo = str(godlo_1) + '_' + str(godlo_2) + '_' + str(godlo_3)
	return godlo


""" petla, funkcja tylko  (plik wsadowy, 
        podczyt z pliku 
        przelicznie wsp
        zapis do pliku zgodnie z godłęm mapy 1:10 000"""


def x1992_do_x2000(xyh):
	""" przelicznie z układu 1992 na 2000
        i dodaje godło mapy jako text
        """
	xy = tt(xyh['X1992'], xyh['Y1992'])
	xyh['X2000'] = xy[0]
	xyh['Y2000'] = xy[1]
	xyh['godlo2000'] = godlo_2000_10k(xy)
	return xyh


def x2000_do_x1992(xyh):
	""" przelicznie z układu 1992 na 2000"""
	xy = tt2(xyh['X2000'], xyh['Y2000'])
	xyh['X1992'] = xy[0]
	xyh['Y1992'] = xy[1]
	return xyh


# with open('C:\Users\olexs\PycharmProjects\model_1992_na_2000\ouput\wyn.csv', 'w', newline='') as csvfile_w:
#    spamwriter = csv.writer(csvfile_w, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(f'{yx[0]:.3f}\t{yx[1]:.3f}\t{yx[2]}')

# 5695850+100 7570300+100
""" prostoką wybierający obszar"""
z = {'X2000': [5695850.00, 5695850.00, 5695950.00, 5695950.0], 'Y2000': [7570300.0, 7570400.0, 7570300.0, 7570400.0],
	 'X1992': 0, 'Y1992': 0}
xz = pd.DataFrame(data=z)
xz1992 = xz.apply(x2000_do_x1992, axis=1)  # przeliczenie prostokąta "z" z 2000 na 1992
# yx1 = pd.read_csv(root_path + dane, header=None, sep=None, engine='python', names=['X', 'Y', 'Z'])
# print (xz1992)

punkty = pd.read_csv(root_path + 'input/M-34-21-C-c-1-3_p.asc', header=None, sep=None, engine='python',names=['Y1992', 'X1992', 'Z'])
# punkty.describe()


wybrane = punkty[(punkty['X1992'] > min(xz1992['X1992'])) & (punkty['X1992'] < max(xz1992['X1992'])) & (punkty['Y1992'] > min(xz1992['Y1992'])) & (punkty['Y1992'] < max(xz1992['Y1992']))]
#    396116.2335273782           396218.9102330478
wybrane['X2000'] = 0
wybrane['Y2000'] = 0
wybrane['godlo2000'] = None
yx2000 = wybrane.apply(x1992_do_x2000, axis=1)
# wybrane.describe()
yx2000.describe()

wyn2000=yx2000[['Y2000','X2000','Z']]
wyn2000['X2000'] = wyn2000['X2000'] - 5695000
wyn2000['Y2000'] = wyn2000['Y2000'] - 7570000
wyn2000.to_csv(root_path + 'output/wyn.csv',sep='\t',date_format='%.4f')
"""with open(root_path + 'output/wyn.csv', 'w', newline='') as csvfile_w:
			spamwriter = csv.writer(yx2000, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #todo spamwriter.writerow(f'{yx2000['X2000']:.3f} \t {yx['Y2000']:.3f} \t {yx2000['godlo2000']}')
			spamwriter.writerow(yx2000['X2000'],yx2000['Y2000'],yx2000['godlo2000'])"""
