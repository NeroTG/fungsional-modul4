# latihan 1
print("\nlatihan 1")
# curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# HOF
perkalian_dengan = perkalian(2) # ini adalah fungsi 'dengan'
hasil = perkalian_dengan(3) # ini adalah pemanggilan fungsi 'dengan'
print(hasil) 

def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# currying
hasil = perkalian(2)(3) # ini adalah pemanggilan fungsi 'dengan' dengan cara currying
print(hasil) 





# latihan 2
print("\nlatihan 2")

def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())  





# latihan 3
print("\nlatihan 3")

def tittle_decorator(function):
    def wrapper():
        func = function()
        make_tittle = func.title()
        print(make_tittle + " " +" - Data is convert to title case")
        return make_tittle
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string) + " " + " - Then Data is splitted")
        return splitted_string
    return wrapper

@split_string
@tittle_decorator
def say_hi():
    return 'hello there'

print(say_hi())  # Output: ['Hello', 'There']




# latihan 4
print("\nlatihan 4")

import math

def translasi(tx, ty):
    def operasi(point):
        x, y = point
        return (x + tx, y + ty)
    return operasi

def dilatasi(sx, sy):
    def operasi(point):
        x, y = point
        return (x * sx, y * sy)
    return operasi

def rotasi(sudut):
    sudut_radian = math.radians(sudut)
    def operasi(point):
        x, y = point
        return (x * math.cos(sudut_radian) - y * math.sin(sudut_radian), x * math.sin(sudut_radian) + y * math.cos(sudut_radian))
    return operasi

# Titik awal
P = (3, 5)

# Translasi
P_translasi = translasi(2, -1)(P)
print(f'Koordinat setelah translasi: {P_translasi}')

# Dilatasi
P_dilatasi = dilatasi(2, -1)(P)
print(f'Koordinat setelah dilatasi: {P_dilatasi}')

# Rotasi
P_rotasi = rotasi(30)(P)
print(f'Koordinat setelah rotasi: {P_rotasi}')





# latihan 5
print("\nlatihan 5")

def point(x,y):
    return x,y

# rumus y = mx+c

def line_equation_of(p1, p2):
    def calculate_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    M = calculate_slope(p1, p2)
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1,1),point(9,5)))



# latihan 6
print("\nlatihan 6")

def point(x,y):
    return x,y

# rumus  y - y1 = m(x - x1)
def line_equation_of(p1, M):
    x1, y1 = p1
    C = y1 - M * x1  # Menghitung nilai C
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (1,9) dan bergradien 5:")
print(line_equation_of(point(1,9), 5))
