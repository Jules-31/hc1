import matplotlib.pyplot as plt
import numpy as np
def plot(h, metodo):
    t, yn, y, error = np.loadtxt(f'{metodo}_h{h}.dat', unpack=True)
    #Solución
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(t, y, 'k-', label='Solución')
    plt.plot(t, yn, 'r--', label=f'{metodo}')
    plt.legend()
    #Error
    plt.subplot(1,2,2)
    plt.plot(t, error, 'b-', label='Error')
    plt.xlabel('t')
    plt.ylabel('Error')
    plt.title(f'Error (h={h})')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f'{metodo}_h{h}-comparar.png')
    plt.close
def plot_error_comparison():
    plt.figure(figsize=(10, 6))
    
    for metodo, color in zip(['euler', 'rk4'], ['red', 'blue']):
        for h in ['0.1', '0.01']:
            try:
                t, _, _, error = np.loadtxt(f'{metodo}_h{h}.dat', unpack=True)
                plt.plot(t, error, '--' if h == '0.1' else '-', 
                        color=color, 
                        label=f'{metodo.upper()} h={h}')
            except FileNotFoundError:
                print(f"Warning: Missing data for {metodo} h={h}")
    
    plt.xlabel('Time (t)')
    plt.ylabel('Absolute Error')
    plt.title('Error Comparison Between metodos')
    plt.legend()
    plt.grid(True)
    plt.savefig('error_comparison.png')
    plt.close()

if __name__ == "__main__":
    # Generate individual plots
    for metodo in ['euler', 'rk4']:
        for h in ['0.1', '0.01']:
            plot(h, metodo)
    
    # Generate comparison plot
    plot_error_comparison()
    
    print("All plots generated successfully!")
    