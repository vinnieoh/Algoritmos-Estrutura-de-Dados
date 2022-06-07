import datetime

def insertion_sort(vetor):
  comp, trocas = 0, 0
  n = len(vetor)

  for i in range(1, n):
    marcado = vetor[i]

    j = i - 1
    while j >= 0 and marcado < vetor[j]:
      comp += 1
      vetor[j + 1] = vetor[j]
      j -= 1
      trocas += 1

    vetor[j + 1] = marcado
    trocas += 1

  return  comp, trocas

def arquivos():
    lista = []
    temp = ''
    
    with open('./lista_numeros/dezMil.txt', 'r') as arq:
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

  comparacao, trocas = insertion_sort(arq)


  tempo = datetime.datetime.now() - inicio
  print(f'Tempo: {tempo.total_seconds():.5f} segundos. | Comparacao: {comparacao} | Trocas: {trocas}| Tamanho: {len(list)} ')
  print()

if __name__ == '__main__':
    main()
