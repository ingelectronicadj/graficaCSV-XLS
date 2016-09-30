import matplotlib.pyplot as plt
import csv
import datetime as dt
import matplotlib.dates as mdates

t = []
x = []
y = []
z = []
w = []

with open('data.tsv','r') as csvfile:
    rows = csv.DictReader(csvfile, delimiter="\t")
    for row in rows:
        #print(row)
        #tiempo = row['Fecha'].replace("/","")
        tiempo = row['Fecha']
        tiempo = dt.datetime.strptime(tiempo,'%d/%m/%Y').date()
        medido = row['OBSERVADO'].replace(",",".")
        medido = float(medido)
        metodo1 = row['URRA'].replace(",",".")
        metodo1 = float(metodo1)
        metodo2 = row['ARMA'].replace(",",".")
        metodo2 = float(metodo2)
        metodo3 = row['CLAO'].replace(",",".")
        metodo3 = float(metodo3)
        t.append(tiempo)
        x.append(medido)
        y.append(metodo1)
        z.append(metodo2)
        w.append(metodo3)

#print(x,y)
#exit()
#dates = ['01/02/1991','01/03/1991','01/04/1991']
#x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
#y = range(len(x))
#print(len(x),len(y))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_locator(mdates.YearLocator())

plt.plot(t,x, label='Parametro OBSERVADO')
plt.plot(t,y, label='Parametro URRA')
plt.plot(t,z, label='Parametro ARMA')
plt.plot(t,w, label='Parametro CLAO')
plt.xlabel('Rango temporal')
plt.ylabel('Magnitud')
plt.title('Representacion grafica de los datos\nCargando archivo .tsv')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
