import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

valor = 0
contador = 0

lista_tempos = []
lista_x = []
lista_pontos = []
lista_limite = []
lista_x.append(0)
lista_limite.append(0)
for i in range(1, 10):
    inicio = time.time()

    contador = 0
    valor = 0
    
    while contador < 10**i:
        contador = contador + 1 
        valor = valor + (1/(contador))
    
    lista_x.append(i)
    lista_pontos.append(valor);
    lista_limite.append(2-(1/contador));
        
    fim = time.time()
    lista_tempos.append(fim-inicio)

print(lista_tempos)
plt.plot(lista_x[1:10], lista_pontos, linestyle=' ', color='b', marker='p', label = 'Pontos')
plt.plot(lista_x, lista_limite, linestyle='-', color='g', label='Limite')
plt.legend()
plt.axis([0,10.1, 0, 25])
plt.show()
