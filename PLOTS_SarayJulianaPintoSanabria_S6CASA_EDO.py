import matplotlib.pyplot as plt
import numpy as np
#Diccionarios para que se vean más bonitas las gráficas
METODOS = {
    'euler': 'Euler',
    'rk4': 'Runge-Kutta 4'
}
COLORES = {
    'euler': 'seagreen',
    'rk4': 'midnightblue'    
}
#Gráfica de los métodos
def grafica(h, metodo):
    t, yn, y, error = np.loadtxt(f'{metodo}_h{h}.dat', unpack=True)
    #Asignar los diccionarios a las variables
    metodo_n = METODOS.get(metodo, metodo)
    colors = COLORES.get(metodo, 'red')
    #Solución
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(t, y, 'k-', label='Solución')
    plt.plot(t, yn, linestyle='--', color=colors, label=metodo_n)
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title(f'Solución (h={h})')
    plt.legend()
    #Error
    plt.subplot(1,2,2)
    plt.plot(t, error, color=colors, label='Error')
    plt.xlabel('t')
    plt.ylabel('Error')
    plt.title(f'Error (h={h})')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f'{metodo}_h{h}-comparar.png')
    plt.close()
    
#Gráfica de comparación de los errores de cada método
def comparacion_errores():
    plt.figure(figsize=(10, 6))
    
    h_values = ['0.1', '0.01']
    
    for metodo, metodo_n in METODOS.items():
        color = COLORES[metodo]
        h_idx = 0
        while h_idx < len(h_values):
            h = h_values[h_idx]
            t, _, _, error = np.loadtxt(f'{metodo}_h{h}.dat', unpack=True)
            plt.plot(t, error, '--' if h == '0.1' else '-',
                     color=color,
                     label=f'{metodo_n} h={h}')
            h_idx += 1
    plt.xlabel('t')
    plt.ylabel('Error')
    plt.title('Comparación errorres')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparacion.png')
    plt.close()

if __name__ == "__main__":
    #Gráficas separadas
    h_values = ['0.1', '0.01']
    
    for metodo_archivo in METODOS.keys():
        h_idx = 0
        while h_idx < len(h_values):
            h = h_values[h_idx]
            grafica(h, metodo_archivo)
            h_idx += 1
    #Gráfica comparación    
    comparacion_errores()
    
