import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

inicio1 = time.time()
valor = 0
contador = 1

lista_tempos = []
lista_x = []
lista_pontos = []
for i in range(1,3):
    inicio = time.time()

    contador = 1
    valor = 0
    
    while contador < 10**i:
        contador = contador + 1 
        valor = valor + (1/(contador+10**i))
    
    lista_x.append(i)
    lista_pontos.append(valor);
        
    fim = time.time()
    lista_tempos.append(fim-inicio)

print(lista_tempos)
plt.plot(lista_x, lista_pontos, linestyle=' ', color='b', marker='p', label = 'Pontos')
plt.plot([0, i+0.1], [13/24,13/24], linestyle='-', color='g', label='Limite')
plt.legend()
plt.axis([0,9+0.1,0,0.72])
plt.show()