import math
def main():
    #escribe tu código abajo de esta línea
    x1 = int(input("x1= "))
    y1 = int(input("y1= "))
    x2 = int(input("x2= "))
    y2 = int(input("y2= "))

    dist_x = x2-x1
    dist_y = y2-y1
    distancia = round(math.sqrt(dist_x**2+dist_y**2),2)

    print(f"distancia= {distancia}")
    
if __name__ == '__main__':
    main()
