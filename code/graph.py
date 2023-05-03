import math
import numpy as np
import matplotlib.pyplot as plt
p = 3

def complex_exp(k, ell):
    input = 2*math.pi*k*ell/p
    real = math.cos(input)
    img = math.sin(input)
    
    if abs(real) < 1e-5:
        real = 0
    if abs(img) < 1e-5:
        img = 0
    
    return (real, img)

def f_k(x, k):
    for ell in range(0, p):
        if ell/p <= x and x <= (ell+1)/p:
            return complex_exp(k, ell)
    return (0, 0)

def generate_graph():
    n = 500
    for k in range(1, p):
        x = np.linspace(-0.5, 1.5, n)
        y_real = []
        y_img = []
        
        for pt in x.tolist():
            p_1, p_2 = f_k(pt, k)
            y_real.append(p_1)
            y_img.append(p_2)
        
        y_real = np.asarray(y_real)
        y_img = np.asarray(y_img)
        
        plt.title("Real Part")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.plot(x, y_real, color ="red")
        plt.show()
        
        plt.title("Imaginary Part")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.plot(x, y_img, color ="red")
        plt.show()
    
if __name__ == "__main__":
    generate_graph()