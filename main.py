import hashlib
from os import system
from time import time
n = []
hashes = []
comparaciones = []

def main():
    num = 1
    l = 110001
    t = time()
    rellenar_numeros(2)
    t = (time()-t)/100
    n = []
    t = int((t * 10 ** num + t * l)*2 + (t * 10 ** num + t * l) ** 2)
    system('cls')
    input(f'tiempo total requerido: {time_(t)}, dale a intro')
    rellenar_numeros(num)
    #rellenar_letras(111)
    rellenar_letras(l)
    generar_hashes()
    comparar_hashes()
    for i in comparaciones:
        print(f'{str(i)[1:-1]}\t')

#110001
def rellenar_numeros(num):
    for i in range(10 ** num):
        t = time()
        n.append(i)
        system('cls')
        print(f"Rellenando numeros, operaciones {i}/{10 ** num}, % {int(i / 10 ** num * 100)}, tiempo {time_(int((time() - t)*(10 ** num-i)))}")


def rellenar_letras(num):
    for i in range(num):
        t = time()
        n.append(chr(i))
        system('cls')
        print(f"Rellenando letras, operaciones {i}/{num}, % {int(i/num*100)}, tiempo {time_(int((time() - t)*(num-i)))}")


def generar_hashes():
    c = 0
    for i in n:
        t = time()
        c += 1
        hashes.append(hashlib.md5(str(i).encode('utf-8',errors='xmlcharrefreplace')).hexdigest())
        system('cls')
        print(f"Generando hashes, operaciones {c}/{len(n)}, % {int(c / len(n) * 100)}, tiempo {time_(int((time() - t)*(len(n)-c)))}")


def comparar_hashes():
    for i in range(len(n)):
        for x in range(len(n)):
            t = time()
            if hashes[i] == hashes[x] and str(i) != str(x):
                comparaciones.append({(hashes[x], hashes[i]):(n[x], n[i])})
                print('FOUND!')
            system('cls')
            print(f"Comparando hashes, operaciones {i*len(n)+x}/{len(n)**2}, % {int((i*len(n)+x)/len(n)**2*100)}, tiempo {time_(int((time() - t)*(len(n)**2-i*len(n)+x)))}")


def time_(s):
    m = s // 60
    s %= 60
    h = m // 60
    m %= 60
    return f"Horas: {h} Minutos: {m} Segundos: {s}"


if __name__ == '__main__':
    main()
