import datetime
import multiprocessing

def bubble_sort(lista):
    comp, trocas = 0, 0
    num = len(lista)

    for i in range(num):
        for j in range(0, num - i - 1):
            comp += 1
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                trocas += 1
            

    return comp, trocas


def arquivos():
    lista = []
    temp = ''
    
    with open('./lista_numeros/quinhentosMil.txt', 'r') as arq:
        data = arq.readline().replace(" ", ",")
        for i in data:
            if i != ',':
                temp +=i
            else:
                lista.append(temp)
                temp = ''

        arq.close()


    
    return lista



def main():
    
    
    cores = multiprocessing.cpu_count()
    arq = arquivos()
    list = []

    for i in arq:
        if i != "," :
            i = int(i)
            list.append(i)
            
    inicio = datetime.datetime.now()

    comparacao, trocas = bubble_sort(arq)


    tempo = datetime.datetime.now() - inicio
    print(f'Tempo: {tempo.total_seconds():.5f} segundos. | Comparacao: {comparacao} | Trocas: {trocas}| Tamanho: {len(list)}| Cores: {cores} ')
    print()

if __name__ == '__main__':
    main()
