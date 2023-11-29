import numpy as np

# Titik awal
A = np.array([1, 9])

def transformation(A):
    def translasi(tx, ty):
        nonlocal A
        # (x+tx, y+ty)
        T = np.array([tx, ty])
        A = A + T
        return A

    def rotasi(theta):
        nonlocal A
        theta = np.radians(theta)  # Konversi derajat ke radian
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        A = np.dot(R, A)
        return A

    def skala(sx, sy):
        # (sx*x, sy*y)
        nonlocal A
        S = np.array([[sx, 0], [0, sy]]) 
        A = np.dot(S, A) 
        return A

    return translasi, rotasi, skala

def line_equation(m):
    # c = y - mx
    # y = mx + c
    def equation(A):
        c = A[1] - m * A[0]   
        return f"y = {m}x + {c}" 
    return equation

def decorator_function(func):
    def wrapper(A):
        print(f"Titik awal: {A}")
        translasi, rotasi, skala = func(A)
        A = translasi(9, 5)
        print(f"Setelah translasi: {A}")
        A = rotasi(60)
        print(f"Setelah rotasi: {A}")
        A = skala(5, 1)
        print(f"Setelah perbesaran skala: {A}")
        equation = line_equation(1)
        print(f"Persamaan garis baru: {equation(A)}")
    return wrapper

# Fungsi dekorator ini mengambil fungsi func sebagai argumen, dan mengembalikan fungsi baru wrapper(A) yang memperluas perilaku fungsi asli.


transform = decorator_function(transformation)
transform(A)
