import datetime

def selection_sort(vetor):
  comp, trocas = 0, 0
  n = len(vetor)

  for i in range(n):
    id_minimo = i
    for j in range(i + 1, n):
      if vetor[id_minimo] > vetor[j]:
        comp += 1
        id_minimo = j
    temp = vetor[i]
    vetor[i] = vetor[id_minimo]
    vetor[id_minimo] = temp
    trocas += 1
  
  return comp, trocas

def arquivos():
    lista = []
    temp = ''
    
    with open('./lista_numeros/umMilhao.txt', 'r') as arq:
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

  arq = arquivos()
  list = []

  for i in arq:
      if i != "," :
        i = int(i)
        list.append(i)
            
  inicio = datetime.datetime.now()

  comparacao, trocas = selection_sort(arq)


  tempo = datetime.datetime.now() - inicio
  print(f'Tempo: {tempo.total_seconds():.5f} segundos. | Comparacao: {comparacao} | Trocas: {trocas}| Tamanho: {len(list)} ')
  print()

if __name__ == '__main__':
    main()


