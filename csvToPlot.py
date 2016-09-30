import matplotlib.pyplot as plt
import csv
import datetime as dt
import matplotlib.dates as mdates

x = []
y = []

with open('data.tsv','r') as csvfile:
    rows = csv.DictReader(csvfile, delimiter="\t")
    for row in rows:
        #print(row)
        #tiempo = row['Fecha'].replace("/","")
        tiempo = row['Fecha']
        tiempo = dt.datetime.strptime(tiempo,'%d/%m/%Y').date()
        w = row['OBSERVADO'].replace(",",".")
        w = float(w)
        #x = row['URRA'].replace(",",".")
        #y = row['ARMA'].replace(",",".")
        #z = row['CLAO'].replace(",",".")
        x.append(tiempo)
        y.append(w)
#print(x,y)
#exit()
#dates = ['01/02/1991','01/03/1991','01/04/1991']
#x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
#y = range(len(x))
#print(len(x),len(y))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_locator(mdates.YearLocator())

plt.plot(x,y, label='Parametro OBSERVADO')
plt.xlabel('Rango temporal')
plt.ylabel('Magnitud')
plt.title('Representacion grafica de los datos\nCargando archivo .tsv')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
