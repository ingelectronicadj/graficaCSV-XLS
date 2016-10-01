""" Autor : Diego Javier Mena Amado
Este es un comentario multilinea. La
obra se muestra con licencia MIT para
el reconocimiento Attribution-Share alike)"""
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime as dt
import matplotlib.dates as mdates

t = []
a = []
b = []
c = []
real = []

with open('data.tsv','r') as csvfile:
    rows = csv.DictReader(csvfile, delimiter="\t")
    for row in rows:
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
        real.append(medido)
        a.append(metodo1)
        b.append(metodo2)
        c.append(metodo3)
            
def main():
    fig, ax = plt.subplots()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    ax.plot(t,real, label='Parametro OBSERVADO')
    ax.plot(t,a, label='Parametro URRA')
    ax.plot(t,b, label='Parametro ARMA')
    ax.plot(t,c, label='Parametro CLAO')
   
    # bbox_to_anchor=(x,y) espaciado entre workspaces, ncol=#Columnas para fits
    ax.legend(loc='upper left', bbox_to_anchor=(0.05, 1), ncol=4, borderaxespad=0) 
    fig.subplots_adjust(right=0.9)
    fig.suptitle('Click derecho para ocultar todo & Click der+izq para mostrar todo', va='top', size='large')

    interactive_legend().show()

def interactive_legend(ax=None):
    if ax is None:
        ax = plt.gca()
    if ax.legend_ is None:
        ax.legend()

    return InteractiveLegend(ax.legend_)

class InteractiveLegend(object):
    def __init__(self, legend):
        self.legend = legend
        self.fig = legend.axes.figure

        self.lookup_artist, self.lookup_handle = self._build_lookups(legend)
        self._setup_connections()

        self.update()

    def _setup_connections(self):
        for artist in self.legend.texts + self.legend.legendHandles:
            artist.set_picker(10) # 10 points tolerance

        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def _build_lookups(self, legend):
        labels = [t.get_text() for t in legend.texts]
        handles = legend.legendHandles
        label2handle = dict(zip(labels, handles))
        handle2text = dict(zip(handles, legend.texts))

        lookup_artist = {}
        lookup_handle = {}
        for artist in legend.axes.get_children():
            if artist.get_label() in labels:
                handle = label2handle[artist.get_label()]
                lookup_handle[artist] = handle
                lookup_artist[handle] = artist
                lookup_artist[handle2text[handle]] = artist

        lookup_handle.update(zip(handles, handles))
        lookup_handle.update(zip(legend.texts, handles))

        return lookup_artist, lookup_handle

    def on_pick(self, event):
        handle = event.artist
        if handle in self.lookup_artist:
            artist = self.lookup_artist[handle]
            artist.set_visible(not artist.get_visible())
            self.update()

    def on_click(self, event):
        if event.button == 3:
            visible = False
        elif event.button == 2:
            visible = True
        else:
            return

        for artist in self.lookup_artist.values():
            artist.set_visible(visible)
        self.update()

    def update(self):
        for artist in self.lookup_artist.values():
            handle = self.lookup_handle[artist]
            if artist.get_visible():
                handle.set_visible(True)
            else:
                handle.set_visible(False)
        self.fig.canvas.draw()

    def show(self):
        #plt.xlabel('Eje x - Dominio temporal')
        plt.ylabel('Magnitud')
        plt.title('Grafica con leyendas interactivas')
        plt.show()

if __name__ == '__main__':
    main()
